/*
// Definition for a Node.
class Node {
    int val;
    Node next;
    Node random;

    public Node(int val) {
        this.val = val;
        this.next = null;
        this.random = null;
    }
}
*/

class Solution {
    public Node copyRandomList(Node head) {
        if (head==null){
            return null;
        }
        Map<Node,Node> dic = new HashMap<>();
        Node curr = head;
        while (curr!=null){
            dic.put(curr,new Node(curr.val));
            curr=curr.next;
        }
        curr = head;
        while (curr!=null){
            Node temp=dic.get(curr);
            temp.next=dic.get(curr.next);
            temp.random=dic.get(curr.random);
            curr=curr.next;
        }
        return dic.get(head);
    }
}