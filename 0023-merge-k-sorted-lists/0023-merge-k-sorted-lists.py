# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        while len(lists)>1:
            merged_lists = []
            for i in range(0,len(lists),2):
                first_list = lists[i]
                second_list = lists[i+1] if (i+1)<len(lists) else None
                merged_lists.append(self.merge(first_list,second_list))
            lists = merged_lists
        return lists[0]
    
    def merge(self,first_list,second_list):
        dummy = res = ListNode()
        while first_list and second_list:
            if first_list.val<=second_list.val:
                dummy.next = first_list
                dummy=dummy.next
                first_list=first_list.next
            else:
                dummy.next=second_list
                dummy=dummy.next
                second_list=second_list.next
        dummy.next = first_list or second_list
        return res.next