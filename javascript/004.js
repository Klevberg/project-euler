// Name:     Largest palindrome product
// Source:   https://projecteuler.net/problem=4


function largest_palindrome_product(digits) {

    let array = [];
    const from = Number("9".repeat(digits));
    const to = Math.pow(10, digits - 1);

    for (let x = from; x > to; x--) {
        for (let y = from; y > to; y--) {
            let p = (x*y).toString();

            if (p.endsWith(p.substring(0, Math.floor(p.length/2)).split("").reverse().join(""))) {
                array.push(p);
            }
        }
    }

    return Math.max(...array);

}

console.log(largest_palindrome_product(3))
