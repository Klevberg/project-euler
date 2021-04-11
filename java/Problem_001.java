class Problem_001 {

    public static void main(String[] args) {

        int sum_of_multiples = 0;
        for (int i = 1; i < 1000; i++) if (i % 3 == 0 || i % 5 == 0) sum_of_multiples += i;

        System.out.println(sum_of_multiples);
        
    }

}
