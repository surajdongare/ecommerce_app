from account_file import Account
from customer_file import Customer, Address
from flipkart_file import Flipkart, Product


prod_obj_1 = Product(pid=1001, nm="Laptop", cat="Electronics", price=1515, qty=1)
prod_obj_2 = Product(pid=1002, nm="Denim", cat="Clothing", price=151, qty=10)
prod_obj_3 = Product(pid=1003, nm="Watch", cat="Accessories", price=5454, qty=25)
prod_obj_4 = Product(pid=1004, nm="BMW Car", cat="Toy", price=1215, qty=2)
prod_obj_5 = Product(pid=1005, nm="Pan", cat="Utensils", price=6451, qty=25)
prod_obj_6 = Product(pid=1006, nm="Basmati Rice", cat="Groceries", price=100, qty=50)

Product.list_of_prods.extend([prod_obj_1,prod_obj_2,prod_obj_3,prod_obj_4,prod_obj_5,prod_obj_6])
# print(Product.list_of_prods)

Customer.OrderedProds.extend([prod_obj_1,prod_obj_2,prod_obj_3,prod_obj_4,prod_obj_5,prod_obj_6])
# print(Customer.OrderedProds)

flip_acc_obj = Account("Current", 10000)
flip_obj = Flipkart(location="Mumbai", no_of_warehouse=4, products=Product.list_of_prods, acc=flip_acc_obj)


# print(flip_obj.FlipProducts)

# print(flip_obj)

ad_obj = Address("21-B", "Kothrud", 415426, "Pune", "MH")
# print(ad_obj)
acc_obj = Account("Saving", 3200000)
cust_obj_1 = Customer(cid=123456789, name="ABC", addr=ad_obj, acc=acc_obj, qty=2, mobile_no=+919541678455, email="abc@gmail.com", isplus_member=True)  # 


# print(cust_obj_1, "Before order")
# print("------------------------------------------------------------")
flip_obj.purchase_product("Basmati Rice", cust_obj_1, 10)



cust_obj_2 = Customer(cid=222222222, name="PQR", addr=ad_obj, acc=acc_obj, qty=2, mobile_no=+919941555555, email="pqr@gmail.com", isplus_member=True)


print("------------------------------------------------------------")
flip_obj.purchase_product("Watch", cust_obj_2, 6)

print(cust_obj_2, "After order")  

cust_obj_3 = Customer(cid=333333333, name="XYZ", addr=ad_obj, acc=acc_obj, qty=2, mobile_no=+918841666666, email="xyz@gmail.com",isplus_member=False)


print("------------------------------------------------------------")
flip_obj.purchase_product("Pan", cust_obj_3, 4)

print(cust_obj_3, "After order")  