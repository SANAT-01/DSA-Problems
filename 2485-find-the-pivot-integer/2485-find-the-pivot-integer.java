class Solution {
    public int pivotInteger(int n) {
        int total=n*(n+1)/2;
        for (int i=1;i<=n;i++){
            int curr=i*(i+1)/2;
            int left=total-curr+i;
            if (curr==left) return i;
        }
        return -1;
    }
}