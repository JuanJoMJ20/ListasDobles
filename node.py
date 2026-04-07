class PCNode:
    def __init__(self, item_id, model, specifications, price):
        self.item_id = item_id
        self.model = model
        self.specifications = specifications
        self.price = price
        self.next = None
        self.prev = None