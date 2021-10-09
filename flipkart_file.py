from parent_file import Base
from product_file import Product
from customer_file import *
from copy import deepcopy
from order_file import Order
import random

class Flipkart(Base):
    def __init__(self, location, no_of_warehouse, products, acc,  headq="Banglore"):
        self.FlipLocation = location
        self.FlipHeadQuarter = headq
        self.FlipNoOfWarehouse = no_of_warehouse
        self.FlipProducts = products
        self.FlipAcc = acc
        self.prods_names = list(map(lambda x : x.ProdName, self.FlipProducts))



    def purchase_product(self, productname, cust, qty):  # Laptop
        if productname in self.prods_names:  # product available or not
            for prod in self.FlipProducts:  #iterate single single product  # flipkart prods
                if productname == prod.ProdName:
                    if qty <= prod.ProdQty:
                        total_price =  qty * prod.ProdPrice  # 1000
                        # print(f"Total price for ur purchase is:- {total_price}")
                        if cust.CustAcc.AccBalance >= total_price:
                            print(prod, "Flipkart Stock before order")  # 25
                            # check if customer is plusmember, if yes then 5% discount on total price
                            if cust.IsPlusMember == False:
                                total_price = total_price - total_price*(5/100)
                                if cust.IsPlusMember == True:
                                    total_price = total_price - total_price*(10/100)
                                cust.CustAcc.AccBalance -=  total_price
                                self.FlipAcc.AccBalance += total_price
                                actual_qty = prod.ProdQty   # 25
                                prod.ProdQty = qty   # 1
                                cust.OrderedProds.append(deepcopy(prod))  # qty - 1
                                prod.ProdQty = actual_qty - qty  # 25 - 1  # update the stock
                                # create transaction id
                                trans_id = random.randint(1111111, 9999999)
                                print("Total Price after discount", total_price)
                                order_obj = Order(transcation_id=trans_id, cust=cust, amount=total_price)
                                Order.all_ordered_list.append(order_obj)
                                print(f"Thanks for purchasing product with Flipkart..Your generated transaction id is:- {trans_id}")
                                print(prod, "Flipkart Stock after order")  # 24
                        else:
                            print("Insufficient amount to purchase this product..!")
                            return
                    else:
                        print(f"Qty shud be less than or equal to {prod.ProdQty}")
                        return 
        else:
            print(f"Given product is not available. Available products are:- {self.prods_names}")



    def return_product(self, productname, cust, qty):  # Denim
        for i in cust.OrderedProds:
            if((i.ProdName)==productname):
                    if qty <= i.ProdQty:
                        print(i.ProdQty)
                        total_price =  qty * i.ProdPrice  # 2000
                        print(total_price)
                        if cust.IsPlusMember == False:
                                total_price = total_price - total_price*(5/100)
                                if cust.IsPlusMember == True:
                                    total_price = total_price - total_price*(10/100)
                                #print(cust.CustAcc.AccBalance,self.FlipAcc.AccBalance)
                                cust.CustAcc.AccBalance +=  total_price
                                self.FlipAcc.AccBalance -= total_price
                                #print(cust.CustAcc.AccBalance,self.FlipAcc.AccBalance)
                                actual_qty = i.ProdQty   
                                #print(actual_qty)
                                i.ProdQty -= qty   
                                #print(i.ProdQty)
                                for i in self.FlipProducts:
                                 if(i.ProdName==productname):
                                  i.ProdQty+=qty
                                trans_id = random.randint(1111111, 9999999)
                                print("Total Price after retrning item", total_price)
                                order_obj = Order(transcation_id=trans_id, cust=cust, amount=total_price)
                                Order.all_ordered_list.append(order_obj)
                                print(f"your product returned succesfully..Your generated transaction id is:- {trans_id}")
                                #print("Flipkart Stock after order")  # 2
                    else:
                        print(f"Qty shud be less than or equal to {i.ProdQty}")
                        return 
            else:
                print(f"For given product no purchase history available")
        



if __name__ == '__main__':
    prod_obj_1 = Product(pid=1001, nm="Laptop", cat="Electronics", price=45126, qty=1)
    prod_obj_2 = Product(pid=1002, nm="Denim", cat="Clothing", price=1000, qty=10)
    prod_obj_3 = Product(pid=1003, nm="Watch", cat="Accessories", price=500, qty=45)
    prod_obj_4 = Product(pid=1004, nm="BMW Car", cat="Toy", price=121525, qty=8)


    flip_acc_obj1 = Account("Current", 100000)
    flip_obj = Flipkart(location="Mumbai", no_of_warehouse=4, acc=flip_acc_obj1, products=[prod_obj_1, prod_obj_2,prod_obj_3,prod_obj_4])
    print(flip_obj)
    
    ad_obj = Address("45-A", "Hadapsar", 456566, "Pune", "MH")
    acc_obj = Account("Saving", 5000)
    cust_obj_1 = Customer(cid=123456789, name="ABC", addr=ad_obj, acc=acc_obj, qty= 5, mobile_no=+919541678455, email="abc@gmail.com",isplus_member=False)

    flip_obj.purchase_product("Denim",cust_obj_1, 5)

    flip_obj.return_product("Denim",cust_obj_1, 2)
    
    print(flip_obj)
    
    print(Order.all_ordered_list)


