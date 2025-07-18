class Company:

    def __init__(self, name, designation, subnet):
        self.name = name
        self.designation = designation
        self.subnet = subnet

    def getInfo(self):
        print(f"The Name = {self.name}")
        print(f"The Designation = {self.designation}")
        print(f"The Subnet = {self.subnet}")

c1 = Company("Pankaj", "Data Analyst", "Student")
c1.getInfo()