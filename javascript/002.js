// Name:     Even Fibonacci numbers
// Source:   https://projecteuler.net/problem=2


function even_fibonacci_sum(num_below) {
    let a = 1;
    let b = 1;
    let n = 0;

    let even_fib = [];

    while (n < num_below) {
        n = a + b;
        a = b;
        b = n;

        if (n % 2 === 0) even_fib.push(n);
    }

    return even_fib.reduce((x, y) => x + y);
}


console.log(even_fibonacci_sum(4_000_000));
