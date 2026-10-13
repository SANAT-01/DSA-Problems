class Solution {
    public long maxAlternatingSum(int[] nums) {
        long sm=0;
        int n=nums.length;
        for (int i=0;i<n;i++){
            nums[i]=Math.abs(nums[i]);
        }
        int i=0,j=n-1;
        Arrays.sort(nums);
        System.out.println(nums);
        while (i<j){
            sm+=-nums[i]*nums[i]+nums[j]*nums[j];
            i++;
            j--;
        }
        if (n%2!=0) {
            sm+=nums[n/2]*nums[n/2];
        }
        return sm;
    }
}