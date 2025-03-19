class Employee:
    def __init__(self, HourlyPay, EmployeeNumber, JobTitle, PayYear2022):
        self.__HourlyPay = HourlyPay #of real
        self.__EmployeeNumber = EmployeeNumber #of string
        self.__JobTitle = JobTitle #of string
        self.__PayYear2022 = PayYear2022 #array[0:51] of real

    def GetEmployeeNumber(self):
        return self.__EmployeeNumber

    def SetPay(self, week_num, hours_worked):
        week_pay = hours_worked * self.__HourlyPay
        self.__PayYear2022[week_num] = week_pay

    def GetTotalPay(self):
        total = 0
        for ele in self.__PayYear2022:
            total += ele
        return total

class Manager(Employee):
    def __init__(self, HourlyPay, EmployeeNumber, JobTitle, PayYear2022, BonusValue):
        super.__init__(HourlyPay, EmployeeNumber, JobTitle, PayYear2022)
        self.BonusValue = BonusValue

    def SetPay(self, week_num, hours_worked):
        hours_worked += self.BonusValue
        Employee.SetPay(week_num, hours_worked)

