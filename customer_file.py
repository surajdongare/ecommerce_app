from parent_file import Base
from account_file import Account
from address_file import Address


class Customer(Base):
    OrderedProds = []

    def __init__(self, cid, name, addr, acc, qty,  mobile_no, email, isplus_member=False):
        self.CustID = cid
        self.CustName = name
        self.CustAddress = addr  # class Address
        self.CustAcc = acc  # class Account
        self.quantity = qty
       
        str_mobile = str(mobile_no)
        if str_mobile[:2] == "91" and len(str_mobile[2:]) == 10:
            self.CustMobile = mobile_no
        else:
            raise ValueError("Mobile number shud have indian code and len shud be 10 digit..!")
        if "@" not in email:
            raise ValueError("Email id shud have @")
        self.CustEmail = email
        self.IsPlusMember = isplus_member
       



if __name__ == '__main__':
    
    ad_obj = Address("45-A", "Hadapsar", 456566, "Pune", "MH")
    acc_obj = Account("Saving", 5800)
    cust_obj_1 = Customer(cid=123456789, name="ABC", addr=ad_obj, acc=acc_obj, qty= 5, mobile_no=+919541678455, email="abc@gmail.com")
    print(cust_obj_1)
    # print(prod_obj_1, "\n", prod_obj_2)
    # cust_obj_2 = Customer(cid=222222222, name="PQR", addr=ad_obj, acc=acc_obj, qty= 5, mobile_no=+919941555555, email="pqr@gmail.com")
    # print(cust_obj_2)
    # cust_obj_3 = Customer(cid=333333333, name="XYZ", addr=ad_obj, acc=acc_obj, qty= 5, mobile_no=+918841666666, email="xyz@gmail.com")
    # print(cust_obj_3)

