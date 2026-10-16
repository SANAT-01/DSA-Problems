class Solution {
    public boolean isPalindrome(int x) {
        if (x<0) return false;
        int org=x;
        int reversed=0;
        while (x>0){
            int last=x%10;
            reversed=reversed*10+last;
            x/=10;
        }
        return org==reversed ? true : false;
    }
}