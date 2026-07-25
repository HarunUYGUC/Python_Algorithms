# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    # Verilen Singly Linked List => L0 -> L1 -> L2 -> ... -> L(n - 1) -> Ln
    # İstenen => L0 -> Ln -> L1 -> L(n - 1) -> L2 -> ...
    def reorderList(self, head):
        if not head or not head.next:
            return
        
        # 1. ORTAYI BUL
        slow = head
        fast = head

        # Birisi 1 adım atarken diğeri 2 adım atar bu sayede birisi
        # listenin sonuna ulaştığında diğeri tam ortasında olur.
        while fast and fast.next:
            slow = slow.next # 1 adım
            fast = fast.next.next # 2 adım

        # 2. İKİNCİ YARIYI TERS ÇEVİR
        second = slow.next
        slow.next = None # İlk yarının ikinci yarıyla olan bağı koparılır.

        prev = None
        current = second

        while current:
            nextNode = current.next
            current.next = prev
            prev = current
            current = nextNode
        
        # 3. İKİ YARIYI ÇAPRAZLAMA BİRLEŞTİR
        first = head
        second = prev # Ters çevrilmiş ikinci yarının başı.

        while second:
            tmp1 = first.next
            tmp2 = second.next

            first.next = second
            second.next = tmp1

            first = tmp1
            second = tmp2
