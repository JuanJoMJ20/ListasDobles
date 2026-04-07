from node import PCNode

class PCMasterInventory:
    def __init__(self):
        self.head = None
        self.tail = None
        self.current = None

    def insert_at_end(self, item_id, model, specs, price):
        new_pc = PCNode(item_id, model, specs, price)
        if not self.head:
            self.head = new_pc
            self.tail = new_pc
        else:
            new_pc.prev = self.tail
            self.tail.next = new_pc
            self.tail = new_pc
        return new_pc

    def remove_current(self):
        if not self.current:
            return
        
        node_to_remove = self.current
        
        if node_to_remove.prev:
            node_to_remove.prev.next = node_to_remove.next
        else:
            self.head = node_to_remove.next
            
        if node_to_remove.next:
            node_to_remove.next.prev = node_to_remove.prev
        else:
            self.tail = node_to_remove.prev

        # Reposicionar el puntero actual tras eliminar
        if node_to_remove.next:
            self.current = node_to_remove.next
        elif node_to_remove.prev:
            self.current = node_to_remove.prev
        else:
            self.current = None