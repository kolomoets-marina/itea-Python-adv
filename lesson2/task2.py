class Shop:
    sum_of_products = 0

    def __init__(self, shop_name, count_of_product):
        self.name = shop_name
        self.product = count_of_product

    def __add__(self, other):
        sum_of_products = self.product + other.product
        return Shop(sum_of_products)


shop_1 = Shop("Flover", 200)
shop_2 = Shop("Vegetables", 100)
shop_3 = Shop("Milk", 30)

shop = shop_1.product + shop_2.product + shop_3.product
print(shop)

