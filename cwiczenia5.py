def zD5():
    class Node:
        def __init__(self, data=None):
            self.data = data
            self.next = None

    class LinkedList:
        def __init__(self):
            self.head = None

        def append(self, data):
            if not self.head:
                self.head = Node(data)
            else:
                current = self.head
                while current.next:
                    current = current.next
                current.next = Node(data)

        def remove_and_count(self):
            if not self.head:
                return 0
            count = 0
            current = self.head
            prev = None
            index = 0
            while current:
                if index % 2 == 0 and current.data[0].islower():
                    count += 1
                    if prev:
                        prev.next = current.next
                    else:
                        self.head = current.next
                else:
                    prev = current
                current = current.next
                index += 1
            return count

        def move_to_front(self):
            if not self.head or not self.head.next or not self.head.next.next:
                return
            current = self.head
            prev = None
            while current and current.next and current.next.next:
                if len(current.data) > len(current.next.data) + len(
                        current.next.next.data):
                    if prev:
                        prev.next = current.next
                        current.next = self.head
                        self.head = current
                        return
                    else:
                        self.head = current.next
                        current.next = current.next.next
                        current.next.next = current
                        return
                prev = current
                current = current.next

        def print_list(self):
            current = self.head
            while current:
                print(current.data)
                current = current.next


def main():
    zD5()


if __name__ == "__main__":
    main()

#pylance krzyczy ale funkcja dziala