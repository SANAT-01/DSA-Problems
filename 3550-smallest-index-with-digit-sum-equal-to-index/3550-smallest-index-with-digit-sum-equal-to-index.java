class Solution {
    public int smallestIndex(int[] nums) {
        for (int i=0;i<nums.length;i++){
            int val=nums[i];
            int ans=0;
            while (val>0){
                ans+=val%10;
                val=val/10;
            }
            if (ans==i){
                return i;
            }
        }
        return -1;
    }
}