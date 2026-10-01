class Solution {
    public boolean isValid(String s) {
        Stack<Character> stk = new Stack<>();
        for (char c : s.toCharArray()) {
            if (c=='(' || c=='{' || c=='['){
                    stk.push(c);
            } else {
                if (stk.empty()==true){
                    return false;
                }
                char top = stk.pop();
                if (c==')' && top!='('){
                    return false;
                } else if (c=='}' && top!='{'){
                    return false;
                } else if (c==']' && top!='['){
                    return false;
                }
            }
        }
        for (char c : stk) {
            System.out.println(c);
        }
        return stk.empty() ? true : false;
    }
}