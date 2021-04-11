// Name:     Multiples of 3 and 5
// Source:   https://projecteuler.net/problem=1


let sum_of_multiples = 0
for (let n = 1; n < 1000; n++) if (n % 3 === 0 || n % 5 === 0) sum_of_multiples += n

console.log(sum_of_multiples)
