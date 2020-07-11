"""
pushFront
newNode
newNode <- key
newNode <- head.next
head <- newNode
if tail == None:
    tail <- head

popFront
if not head:
    :return
head = head.next
if head is None:
    tail == None


pushFront  O(1)
topFront    O(1)
popFront    O(1)
PushBack    O(1)
topBack O(1)
popBack O(1)
FindKey(key)    O(n)
eraseKey(key)   O(n)
empty() O(1)
addBefore(node, key) O(n)
addAfter(node, key) O(n)

"""