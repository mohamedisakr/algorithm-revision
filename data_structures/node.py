class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def __str__(self) -> str:
        return f'{self.val}'

    def show_node_list(self, head):
        while head is not None:
            print(f'{head} ', end='-> ')
            head = head.next
        print(f'{None}', end='')

    def find(self, head, value):
        while head is not None:
            if head.val == value:
                return head
            head = head.next
        return None


def main():
    node1 = Node(10)
    node2 = Node(20)
    node3 = Node(30)
    node4 = Node(40)

    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = None

    # node1.show_node_list(node1)
    val = 30  # 50
    found_node = node1.find(node1, val)
    print(found_node)


if __name__ == '__main__':
    main()
