

class Item:
    def __init__(self, id: int, name: str, MinQty: float):
        self.id = id
        self.name = name
        self.MinQty = MinQty


existing_Item = [
    Item(1, "Grapes", 1),
    Item(2, "Banana", 1)
]


class Memo:
    def __init__(self, product_details: list[Item], amount: float, retailer_name: str = "Ananomous"):
        self.retailer_name = retailer_name
        self.product_details = product_details
        self.amount = amount

    def bill(self):
        if (self.product_details):
            width = 44
            print("=" * width)
            print(f"{'SALES MEMO':^{width}}")
            print("=" * width)

            print(f" Seller Name : {self.retailer_name:<30}")
            print("-" * width)

            print(f"{' Item ID':<9}{'Item Name':<23}{'Qty':>8}")
            print("-" * width)

            for n in self.product_details:
                print(f" {n.id:<9}{n.name:<23.23}{n.MinQty:>8}")

            print("-" * width)
            print(f"{'Total Amount':<30}{self.amount:>14}")
            print("=" * width)
            print(f"{'Thank you for your purchase!':^{width}}")
            print("=" * width)
        else:
            print(
                "!!  Please purchase atleast one item from the store to create bill  !!")


class Product:
    name = str,
    price = float,


def main():
    seller_name = input("Enter Owner Name: ")
    session = True
    while (session):
        print("MENU ITEMS")
        for item in existing_Item:
            print(item.id, item.name, item.MinQty)
        bucket: list[Item] = []
        while (True):
            op = input(f"Operations:\n pick item(j) | quit(q) | go to cart(n)")
            if (op == 'q'):
                return
            elif (op == 'j'):
                picked_id = int(input("insert item id to pick: ").split()[0])
                # check with stock items to add quantity
                item = next(
                    (item for item in existing_Item if item.id == picked_id),
                    None
                )
                if (item):
                    qty = input("Select Quantity")
                else:
                    print("Select available products only !!")
                pick = Item(picked_id, item.name, qty)
                bucket.append(pick)
            elif (op == 'n'):
                break

        if (op == 'n' and bucket[0] == None):
            print("Nothing selected to purchase")

        # bucket: list[Item] = []
        print("Items selected are:")
        for pick in bucket:
            print(pick.name)

        # for item in bucket:
        #     print(item.name)
        amount = 200
        if (seller_name == ""):
            curr_memo = Memo(bucket, amount)
        else:
            curr_memo = Memo(bucket, amount, seller_name)
        isBill = input("Is bill required? ")
        if (isBill == 'y' or 'yes'):
            curr_memo.bill()
        ans = input("do you want to create another bill(b) or quit(q)").lower()
        session = False if ans == 'q' else True

    return


main()
