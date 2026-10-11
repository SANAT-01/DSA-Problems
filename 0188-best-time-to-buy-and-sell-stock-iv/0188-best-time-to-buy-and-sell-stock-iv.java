class Solution {
    private int[][][] dp;
    public int myProfit(int ind, int buy, int cap, int[] prices){
        if (ind==prices.length | cap==0) return 0;
        int profit=0;
        if (dp[ind][buy][cap]!=-1){
            return dp[ind][buy][cap];
        }
        if (buy==1){
            profit=Math.max(myProfit(ind+1,0,cap,prices)-prices[ind],
                            myProfit(ind+1,1,cap,prices));
        } else {
            profit=Math.max(myProfit(ind+1,1,cap-1,prices)+prices[ind],
                            myProfit(ind+1,0,cap,prices));
        }
        dp[ind][buy][cap]=profit;
        return dp[ind][buy][cap];
    }
    public int maxProfit(int k, int[] prices) {
        int n=prices.length;
        dp = new int[n][2][k+1];
        for (int i=0;i<n;i++){
            for (int j=0;j<2;j++){
                for (int l=0;l<=k;l++){
                    dp[i][j][l]=-1;
                }
            }
        }
        return myProfit(0,1,k,prices);
    }
}