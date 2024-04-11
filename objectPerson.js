#!/usr/bin/node

const Person1 = {
  firstName: 'Ben',
  secondName: 'Willys',
  age: 30,
  isEmployed: true,
  sayHello: function () { console.log('Hi! I am Ben!'); },
  eat: function () { console.log('I am Eating a Chips'); }
};

Person1.sayHello();

const Person2 = {
    firstName: 'Allan',
    secondName: 'Paul',
    age: 37,
    isEmployed: false,
    play: () => console.log('I play chess')
};

Person2.play();
