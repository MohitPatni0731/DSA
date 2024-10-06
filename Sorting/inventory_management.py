class Item:
    def __init__(self, item_name, item_price) -> None:
        self.item_name = item_name
        self.item_price = item_price


class InventoryMngSys:
    def __init__(self) -> None:
        self.inventoryy = []

    def add_new_item_to_inventory(self, item: Item) -> None:
        self.inventoryy.append(item)

    def find_remaining_item(self, item_name) -> int:
        pass

    def profit_report(self, item: Item) -> int:
        pass
