
class ListNode:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    # TODO: not finished yet (e.g. no remove item method ...)
    def __init__(self):
        self.head = None
        self.tail = None

    def __int__(self, array):
        if len(array) > 0:
            for item in array:
                self.emplace_back(item)

    def emplace_back(self, item):
        item = ListNode(item)

        if self.head is None:
            self.head = item
        else:
            self.tail.next = item

        self.tail = item
        return item

