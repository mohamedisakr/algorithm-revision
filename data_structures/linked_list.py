class LinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def show_node_list(self):
        temp_head = self.head
        while temp_head is not None:
            print(f'{temp_head}', end=' -> ')
            temp_head = temp_head.next
        print(f'{None}', end='')
