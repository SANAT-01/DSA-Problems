class Solution {
    public int sumCounts(List<Integer> nums) {
        int n=nums.size();
        int total=0;
        for (int i=0;i<n;i++){
            Set<Integer> num = new HashSet<>();
            int distinct = 0;
            for (int j=i;j<n;j++){
                if (!num.contains(nums.get(j))) {
                    distinct+=1;
                    num.add(nums.get(j));
                }
                total+=distinct*distinct;
            }
        }
        return total;
    }
}