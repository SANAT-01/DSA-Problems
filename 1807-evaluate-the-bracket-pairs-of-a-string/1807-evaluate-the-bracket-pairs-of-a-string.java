class Solution {
    public String evaluate(String s, List<List<String>> knowledge) {
        ArrayList<String> arr = new ArrayList<>();
        int l=0;
        int r=0;
        HashMap<String, String> k = new HashMap<>();
        for (int idx=0; idx<knowledge.size(); idx++){
            k.put(knowledge.get(idx).get(0), knowledge.get(idx).get(1));
        }
        while (r<s.length()){
            if (s.charAt(r)=='(' && r>l){
                while (s.charAt(l)=='('){
                    l++;
                }
                arr.add(s.substring(l,r));
                l=r;
            }
            else if (s.charAt(r)==')'){
                while (s.charAt(l)=='('){
                    l++;
                }
                String val=s.substring(l,r);
                arr.add(k.getOrDefault(val,"?"));
                l=r+1;
            } 
            r+=1;
        }
        arr.add(s.substring(l,r));
        String ans="";
        for (String x : arr){
            ans+=x;
        }
        return ans;
    }
}