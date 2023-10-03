"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, name, mnth, hrs, perHr, bnsComm, comm, perComm):
        self.name = name
        self.mnth = mnth
        self.hrs = hrs
        self.perHr = perHr
        self.bnsComm = bnsComm
        self.comm = comm
        self.perComm = perComm

    def get_pay(self):
        pay = 0
        if self.mnth != None:
            pay += self.mnth
        if self.hrs != None:
            pay += self.hrs * self.perHr
        if self.bnsComm != None:
            pay += self.bnsComm
        if self.comm != None:
            pay += self.comm * self.perComm
        return pay

    def __str__(self):
        explanation = self.name + " works on a "
        if self.mnth != None:
            explanation += "monthly salary of " + str(self.mnth)
        if self.hrs != None:
            explanation += "contract of " + str(self.hrs) + " hours at " + str(self.perHr) + "/hour"
        if self.bnsComm != None:
            explanation += " and recieves a bonus commission of " + str(self.bnsComm)
        if self.comm != None:
            explanation += " and recieves a commission for " + str(self.comm) + " contract(s) at " + str(self.perComm) + "/contract"
        explanation += ".  Their total pay is " + str(self.get_pay) + "."
        return explanation


# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie', 4000, None, None, None, None, None)

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie', None, 100, 25, None, None, None)

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee', 3000, None, None, None, 4, 200)

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan', None, 150, 25, None, 3, 220)

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie', 2000, None, None, 1500, None, None)

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel', None, 120, 30, 600, None, None)
