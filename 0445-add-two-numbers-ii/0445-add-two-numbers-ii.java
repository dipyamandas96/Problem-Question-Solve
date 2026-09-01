class Solution {
    public ListNode addTwoNumbers(ListNode ll1, ListNode ll2) {

        ListNode curr = ll1;

        List<Integer> l1 = new ArrayList<>();
        List<Integer> l2 = new ArrayList<>();


        // Store first linked list values
        while (curr != null) {

            l1.add(curr.val);

            curr = curr.next;
        }


        curr = ll2;


        // Store second linked list values
        while (curr != null) {

            l2.add(curr.val);

            curr = curr.next;
        }


        int carry = 0;


        ListNode dummy = new ListNode(0);


        // Add digits from the end of both lists
        while (!l1.isEmpty() && !l2.isEmpty()) {

            int sum = l1.get(l1.size() - 1)
                    + l2.get(l2.size() - 1)
                    + carry;


            carry = sum / 10;

            sum = sum % 10;


            ListNode node = new ListNode(sum);

            node.next = dummy.next;

            dummy.next = node;


            l1.remove(l1.size() - 1);
            l2.remove(l2.size() - 1);
        }


        // Remaining digits of first list
        while (!l1.isEmpty()) {

            int sum = l1.get(l1.size() - 1) + carry;


            carry = sum / 10;

            sum = sum % 10;


            ListNode node = new ListNode(sum);

            node.next = dummy.next;

            dummy.next = node;


            l1.remove(l1.size() - 1);
        }


        // Remaining digits of second list
        while (!l2.isEmpty()) {

            int sum = l2.get(l2.size() - 1) + carry;


            carry = sum / 10;

            sum = sum % 10;


            ListNode node = new ListNode(sum);

            node.next = dummy.next;

            dummy.next = node;


            l2.remove(l2.size() - 1);
        }


        // Remaining carry
        if (carry != 0) {

            ListNode node = new ListNode(carry);

            node.next = dummy.next;

            dummy.next = node;
        }


        return dummy.next;
    }
}