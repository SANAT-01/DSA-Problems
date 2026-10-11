class Solution {
    private int[][][] dp;
    public int myProfit(int ind, int buy, int[] prices, int cap){
        if (ind==prices.length | cap==0) return 0;
        int profit=0;
        if (dp[ind][buy][cap]!=-1){
            return dp[ind][buy][cap];
        }
        if (buy==1){
            profit=Math.max(myProfit(ind+1,0,prices,cap)-prices[ind],
                            myProfit(ind+1,1,prices,cap));
        } else {
            profit=Math.max(myProfit(ind+1,1,prices,cap-1)+prices[ind],
                            myProfit(ind+1,0,prices,cap));
        }
        dp[ind][buy][cap]=profit;
        return dp[ind][buy][cap];
    }
    public int maxProfit(int[] prices) {
        int n=prices.length;
        dp=new int[n][2][3];
        for (int i=0;i<n;i++){
            for (int j=0;j<2;j++){
                for (int k=0;k<3;k++){
                    dp[i][j][k]=-1;
                }
            }
        }
        return myProfit(0,1,prices,2);
    }
}