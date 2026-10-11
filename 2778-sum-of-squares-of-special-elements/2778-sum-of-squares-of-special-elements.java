class Solution {
    public int sumOfSquares(int[] nums) {
        int total=0;
        int n=nums.length;
        for (int i=1;i<n+1;i++){
            if (n%i==0){
                total+=nums[i-1]*nums[i-1];
            }
        }
        return total;
    }
}