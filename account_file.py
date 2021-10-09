from parent_file import Base
import random

# min - 3000
class Account(Base):
    def __init__(self, acctype, balance=3000):
        self.AccountNo = random.randint(11111, 99999)
        self.AccType = acctype
        if balance < 3000:
            raise ValueError("Account balance shud be more than or equal to 3000")
        self.AccBalance = balance


if __name__ == '__main__':
    acc_obj = Account("Saving", 32000)
    print(acc_obj)




