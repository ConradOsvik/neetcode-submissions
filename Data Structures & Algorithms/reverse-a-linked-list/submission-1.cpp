/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */

ListNode* inner(ListNode* last, ListNode* rest) {
    if (rest != nullptr) {
        auto rr = rest->next;
        rest->next = last;
        return inner(rest, rr);
    } else {
        return last;
    }
}

class Solution {
public:
    ListNode* reverseList(ListNode* head) {
        if (head == nullptr) {
            return nullptr;
        };

        ListNode* rest = head->next;
        head->next = nullptr;
        return inner(head, rest);
    }
};