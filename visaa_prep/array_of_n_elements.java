import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;
public class Solution {
    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
         Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        int[] result = createArray(n);       
        System.out.println(Arrays.toString(result));
    }    
    public static int[] createArray(int n) {
        // Create an array of size n
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) {
            arr[i] = i;
        }
        return arr;
    }
}
