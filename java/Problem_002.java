// Name:     Even Fibonacci numbers
// Source:   https://projecteuler.net/problem=2


import java.util.ArrayList;

public class Problem_002 {

    public static void main(String[] args) {

        System.out.println(even_fibonacci_sum(4_000_000));

    }

    public static int even_fibonacci_sum(int num_below) {

        int a = 1;
        int b = 1;
        int n = 0;

        ArrayList<Integer> even_fib = new ArrayList<>();

        while (n < num_below) {
            n = a + b;
            a = b;
            b = n;

            if (n % 2 == 0) even_fib.add(n);
        }

        return even_fib.stream().mapToInt(i -> i).sum();

    }
    
}
