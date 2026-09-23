class Solution {
    public int minOperations(int[] nums, int x) {
        int sm=0;
        for (int n: nums){
            sm+=n;
        }
        if (sm==x) return nums.length;
        int t=sm-x, left=0, curr=0, maxi=0;
        for (int right=0;right<nums.length;right++){
            curr+=nums[right];
            while (left<=right && curr>t){
                curr-=nums[left];
                left++;
            }
            if (curr==t){
                maxi=Math.max(maxi,right-left+1);
            }
        }
        return maxi>0 ? nums.length-maxi : -1;
    }
}