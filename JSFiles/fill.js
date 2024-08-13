// Append item to an array.
const fruits = ['banana', 'mango', 'apple', 'strawberry', 'kiwi', 'guava', 'melon'];
const start = -2;
const deleteCount = 2;

const removeItems = fruits.splice(start, deleteCount, 'bitrut', 'lemon');
console.log(fruits);

// separator
console.log('***********SEPARATOR**************');
console.log(removeItems);

// sep 2
console.log('***********SEPARATOR**************');

for (const fruit of fruits) {
    console.log(fruit);
}
