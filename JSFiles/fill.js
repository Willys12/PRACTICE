// Append item to an array.
const fruits = ['banana', 'mango', 'apple', 'strawberry', 'kiwi', 'guava', 'melon'];
const start = 0;
const deleteCount = 3;

const removeItems = fruits.splice(start, deleteCount);
console.log(removeItems);
