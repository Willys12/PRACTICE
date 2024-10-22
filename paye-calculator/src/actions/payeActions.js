//import { grossSalary } from '../reducers/payeReducer';

export const calculatePAYE = (grossSalary) => {
    return {
        type: 'CALCULATE_PAYE',
        payload: { grossSalary }
    };
};
