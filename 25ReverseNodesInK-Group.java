/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode reverseLinkedList(ListNode head, int k){
        ListNode newHead = null;
        ListNode prev = head;
        
        while(k > 0){
            
            ListNode next = prev.next;
            
            prev.next = newHead;
            
            newHead = prev;
            
            prev = next;
            
            k--;
        }
        return newHead;
    }
    
    public ListNode reverseKGroup(ListNode head, int k) {
        
        int count = 0;
        ListNode pointer = head;
        
        while(count < k && pointer != null){
            pointer = pointer.next;
            count++;
        }
        
        if(count == k){
            ListNode reverseHead = this.reverseLinkedList(head,k);
            head.next = this.reverseKGroup(pointer,k);
            return reverseHead;
        }
        return head;
    }
}
