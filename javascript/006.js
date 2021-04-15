// Name:     Sum square difference
// Source:   https://projecteuler.net/problem=6


const sum_of_square = num => [...Array(num + 1).keys()].map(x => Math.pow(x, 2)).reduce((x, y) => x + y);

const square_of_sum = num => Math.pow([...Array(num + 1).keys()].reduce((x, y) => x + y), 2);

const difference = num => square_of_sum(num) - sum_of_square(num);


console.log(difference(100));