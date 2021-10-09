from parent_file import Base

class Address(Base):
    def __init__(self, house_no, area, pin, city, state):
        self.AddrHouse = house_no
        self.AddrArea = area
        self.AddrPincode = pin
        self.AddrCity = city
        self.AddrState = state

        
 
if __name__ == '__main__':
    ad_obj = Address("21-B", "Kothrud", 415426, "Pune", "MH")
    print(ad_obj)
