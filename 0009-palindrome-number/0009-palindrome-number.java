class Solution {
    public boolean isPalindrome(int x) {
        String arr=String.valueOf(x);
        if (arr.charAt(0)=='-') return false;
        int i=0,j=arr.length()-1;
        while (i<j){
            if (arr.charAt(i)!=arr.charAt(j)) return false;
            i++;
            j--;
        }
        return true;
    }
}