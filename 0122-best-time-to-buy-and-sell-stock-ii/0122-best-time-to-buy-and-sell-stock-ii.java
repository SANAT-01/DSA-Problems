class Solution {
    public int maxProfit(int[] prices) {
        int total=0;
        int l=0,r=1;
        int n=prices.length;
        while (r<n){
            int val=prices[r]-prices[l];
            if (val>0){
                total+=val;
            }
            l=r;
            r+=1;
        }
        return total;
    }
}