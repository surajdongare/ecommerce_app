from parent_file import Base

class Order(Base):
    all_ordered_list = []
    
    def __init__(self, transcation_id, cust, amount, type_of_order="Purchase", type_of_trans="buy"):
        self.OrderTransactionID = transcation_id
        self.OrderCust = cust
        self.OrderAmount = amount
        self.TypeOfOrder = type_of_order
        self.TypeOfTrans = type_of_trans
