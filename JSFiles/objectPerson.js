#!/usr/bin/node

const car = {
  wheels: 4,
  doors: 5,
  engine: '2000cc',
  sound: function () {
    return 'vooooom!';
  }
};

// console.log(car.sound());

const truck = Object.create(car);
truck.wheels = 6;
truck.engine = function () {
  return 'ng\'aaaaang!';
};
//console.log(truck.engine());

const coachTruck = Object.create(truck);
coachTruck.doors = 6;
coachTruck.seats = 64;
coachTruck.boot = 'sits on chasis';
coachTruck.engine = function () {
  return {
    size: '6000cc',
    HP: '700hp',
    sound: function () {
      return 'uuuuuuuum! pchhhhhhhhhhhhhhhhh!';
    }
  };
};

//console.log(coachTruck.wheels);

const trailerB = Object.create(coachTruck);
trailerB.doors = 2;
trailerB.wheels = 24;
trailerB.chasisNo = '65XXD01';
trailerB.warningSound = function () {
    return 'Pooooooooom!';
};

console.log(trailerB.warningSound());
