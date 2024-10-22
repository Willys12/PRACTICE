const initialState = {
    grossSalary: 0,
    deductions: {
        paye: 0,
        nhif: 0,
        nssf: 0,
        housingLevy: 0,
        totalDeductions: 0,
        netSalary: 0
    }
};

export const payeReducer = (state=initialState, action) => {
    switch (action.type) {
        case 'CALCULATE_PAYE':
            const { grossSalary } = action.payload;
            let paye = 0, nhif = 0, nssf = 0, housingLevy = 0;

            //Paye calc
            if (grossSalary <= 24000) {
                paye = grossSalary * 0.1;
            } else if (grossSalary <= 32333) {
                paye = 2400 + (grossSalary - 24000) * 0.25;
            } else {
                paye = 4483.25 + (grossSalary - 32333) * 0.30;
            }

            nssf = Math.min(grossSalary * 0.06, 1080);

            if (grossSalary <= 5999) nhif = 150;
            else if (grossSalary <= 7999) nhif = 300;
            else if (grossSalary <= 11999) nhif = 400;
            else if (grossSalary <= 14999) nhif = 500;
            else if (grossSalary <= 19999) nhif = 600;
            else if (grossSalary <= 24999) nhif = 750;
            else nhif = 850;

            housingLevy = grossSalary * 0.015;

            const totalDeductions = paye + nssf + nhif + housingLevy;
            const netSalary = grossSalary - totalDeductions;

            return {
                ...state,
                grossSalary,
                deductions: {
                    paye,
                    nhif,
                    nssf,
                    housingLevy,
                    totalDeductions,
                    netSalary
                }
            };
            default:
                return state;

    }
};
