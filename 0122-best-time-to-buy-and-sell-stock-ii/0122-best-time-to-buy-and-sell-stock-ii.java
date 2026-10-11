class Solution {
    private int[][] dp;
    public int myProfit(int ind, int buy, int[] prices){
        int profit=0;
        if (ind==prices.length){
            return 0;
        }
        if (dp[ind][buy]!=-1){
            return dp[ind][buy];
        }
        if (buy==1){
            profit=Math.max(myProfit(ind+1,0,prices)-prices[ind],
                        myProfit(ind+1,1,prices)-0);
        } else {
            profit=Math.max(myProfit(ind+1,1,prices)+prices[ind],
                        myProfit(ind+1,0,prices)-0);
        }
        dp[ind][buy]=profit;
        return profit;
    }
    public int maxProfit(int[] prices) {
        int n = prices.length;
        dp = new int[n][2];
        for (int i=0;i<n;i++){
            for (int j=0;j<2;j++){
                dp[i][j]=-1;
            }
        }
        return myProfit(0,1,prices);
    }
}