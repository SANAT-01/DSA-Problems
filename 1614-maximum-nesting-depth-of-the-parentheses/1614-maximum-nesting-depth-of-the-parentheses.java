class Solution {
    public int maxDepth(String s) {
        Stack<String> stack=new Stack<>();
        int ans=0;
        for (int i=0;i<s.length();i++){
            if (s.charAt(i)=='('){
                stack.push(Character.toString(s.charAt(i)));
            }else if (s.charAt(i)==')') {
                stack.pop();
                ans=Math.max(ans,stack.size()+1);
            }
        }
        return ans;
    }
}