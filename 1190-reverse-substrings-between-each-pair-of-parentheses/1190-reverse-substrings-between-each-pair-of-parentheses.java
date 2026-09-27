class Solution {
    public String reverseParentheses(String s) {
        Stack<StringBuilder> stack= new Stack<>();
        StringBuilder curr = new StringBuilder();
        for (int i=0;i<s.length();i++){
            char ch=s.charAt(i);
            if (ch=='('){
                stack.push(curr);
                curr=new StringBuilder();
            } else if (ch==')'){
                curr=curr.reverse();
                curr=stack.pop().append(curr);
            } else {
                curr.append(ch);
            }
        }
        return curr.toString();
    }
}