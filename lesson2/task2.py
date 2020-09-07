class Shop:
    X=0
    def __init__(self, shop_name,count_of_product):
        self.name = shop_name
        self.product = count_of_product

    def change_x(self):
        self.X += self.product
        print(self.X)

shop_1=Shop("Flover",20)
shop_1.change_x()
shop_2=Shop("Vegetables",100)
shop_2.change_x()

