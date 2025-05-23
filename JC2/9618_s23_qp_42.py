class Employee:
    def __init__(self, HourlyPay, EmployeeNumber, JobTitle):
        self.__HourlyPay = HourlyPay #of real
        self.__EmployeeNumber = EmployeeNumber #of string
        self.__JobTitle = JobTitle #of string
        self.__PayYear2022 = [0.0 for i in range(51)] #array[0:51] of real

    def GetEmployeeNumber(self):
        return self.__EmployeeNumber

    def SetPay(self, week_num, hours_worked):
        self.__PayYear2022[week_num] = hours_worked * self.__HourlyPay

    def GetTotalPay(self):
        total = 0
        for ele in self.__PayYear2022:
            total += ele
        return total

class Manager(Employee):
    def __init__(self, HourlyPay, EmployeeNumber, JobTitle, BonusValue):
        super.__init__(HourlyPay, EmployeeNumber, JobTitle)
        self.BonusValue = BonusValue

    def SetPay(self, week_num, hours_worked):
        hours_worked += self.BonusValue
        Employee.SetPay(week_num, hours_worked)

