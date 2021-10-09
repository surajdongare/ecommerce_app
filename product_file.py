from parent_file import Base


class Product(Base):
    list_of_prods = []
    
    def __init__(self, pid, nm, cat,price, qty):
        self.ProdID = pid
        self.ProdName = nm
        self.ProdCat = cat
        self.ProdPrice = price
        self.ProdQty = qty

if __name__ == '__main__':
    
    prod_obj_1 = Product(pid=1001, nm="Laptop", cat="Electronics", price=45126, qty=1)

    prod_obj_2 = Product(pid=1002, nm="Denim", cat="Clothing", price=1245, qty=40)

    prod_obj_3 = Product(pid=1002, nm="alchemist", cat="book", price=1600, qty=25)
    # Product.list_of_prods.extend([prod_obj_1, prod_obj_2])
    # print(Product.list_of_prods)
    # print(prod_obj_1, "\n", prod_obj_2)
    print([prod_obj_1, prod_obj_2,prod_obj_3])
    
    print(prod_obj_1.ProdName)

