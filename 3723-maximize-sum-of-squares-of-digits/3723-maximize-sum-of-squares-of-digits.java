import java.math.BigInteger;

class Solution {
    public String maxSumOfSquares(int num, int sum) {
        if (sum > num * 9 || sum < 1) return "";

        StringBuilder sb = new StringBuilder();
        int remaining = sum;

        for (int i = 0; i < num; i++) {
            int digit = Math.min(9, remaining);
            sb.append(digit);
            remaining -= digit;
        }

        String ans = sb.toString();
        int check=0;
        for (char c : ans.toCharArray()){
            check+=Character.getNumericValue(c);
        }
        return check==sum ? ans : "";
    }
}