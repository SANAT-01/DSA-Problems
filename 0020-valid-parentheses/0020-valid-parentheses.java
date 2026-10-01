class Solution {
    public boolean isValid(String s) {
        Stack<Character> stk = new Stack<>();
        for (char c : s.toCharArray()) {
            if (stk.empty() || c=='(' || c=='{' || c=='['){
                    stk.push(c);
            } else if (c==')'){
                if (stk.peek()=='(') stk.pop();
                else return false;
            } else if (c=='}'){
                if (stk.peek()=='{') stk.pop();
                else return false;
            } else if (c==']'){
                if (stk.peek()=='[') stk.pop();
                else return false;
            } else {
                return false;
            }
        }
        return stk.empty() ? true : false;
    }
}