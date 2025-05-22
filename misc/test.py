# EmployeeArray = [None for i in range(8)] #array[0:7] of type Employee
# try:
#     FileHandle = open("Employees.txt", 'r')
#     for i in range(8):
#         hourly_pay = float(FileHandle.readline().strip())
#         employee_number = FileHandle.readline().strip()
#         bonus_or_job = FileHandle.readline().strip()
#         if bonus_or_job.replace('.', '', 1).isdigit():
#             job = FileHandle.readline.strip()
#             EmployeeArray[i] = Manager(hourly_pay, employee_number, float(bonus_or_job), job)
#         else:
#             EmployeeArray[i] = Employee(hourly_pay, employee_number, bonus_or_job)

#     FileHandle.close()
# except:
#     print("File not found.")


# def ReturnAllData():
#     retstring = ""
#     pointer = TheQueue.HeadPointer
#     while pointer != TheQueue.TailPointer:
#         retstring += f"{TheQueue.QueueArray[pointer]} "
#         if pointer == 99:
#             pointer = 0
#         else:
#             pointer += 1
#     return retstring