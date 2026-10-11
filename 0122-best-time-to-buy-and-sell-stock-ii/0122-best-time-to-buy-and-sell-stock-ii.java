class Solution {
    public int maxProfit(int[] prices) {
        int total=0;
        int n=prices.length;
        int r=1;
        while (r<n){
            int val=prices[r]-prices[r-1];
            if (val>0){
                total+=val;
            }
            r++;
        }
        return total;
    }
}