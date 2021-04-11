let sum_of_multiples = 0;
for (let n = 1; n < 1000; n++)
    if (n % 3 === 0 || n % 5 === 0)
        sum_of_multiples += n;
console.log(sum_of_multiples);
