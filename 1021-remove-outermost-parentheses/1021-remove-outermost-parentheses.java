class Solution {
    public String removeOuterParentheses(String s) {
        ArrayList<String> arr= new ArrayList<>();
        int open = 0;
        String sub = "";
        for (char c : s.toCharArray()){
            if (c=='(') open += 1;
            else open -=1;
            if (open==0){
                arr.add(sub.substring(1, sub.length()));
                sub="";
            } else {
                sub+=c;
            }
        }
        sub="";
        for (String c : arr){
            sub+=c;
        } 
        return sub;
    }
}