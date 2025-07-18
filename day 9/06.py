class Train:
    def __init__(self, TrainName, tkt_number):
        self.TrainName = TrainName
        self.tkt_number = tkt_number

    def getStatus(self):
        print(f"The Train Name = {self.TrainName}")
        print(f"The Number of Tickets = {self.tkt_number}")
        print("============================\n")


    def tickets(self, bookings):
        self.tkt_number -= bookings
        print(f"Tickets Booked = {bookings}")

    def remaining(self):
        print(f"Remaining Tickets = {self.tkt_number}")
        print("============================\n")



b1 = Train ("Vande Bharat", 100)
b1.getStatus()

b1.tickets(int(input("Enter the number of tickets to book: ")))
b1.getStatus()

b1.remaining()
b1.getStatus()

