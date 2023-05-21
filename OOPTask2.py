class Person:
    no_of_persons=0
    def __init__(self,emp_id,emp_name,emp_salary,emp_department):
        self.emp_id=emp_id
        self.emp_name=emp_name
        self.emp_salary=emp_salary
        self.__emp_department=emp_department
        Person.no_of_persons +=1
        
    def print_employee_details(self):
        return "This person name is {} with an ID {} get this salary {} in department {}".format(self.emp_name,self.emp_id, self.emp_salary, self.__emp_department)
        
    def set_emp_department(self, new_department):
        self.__emp_department= new_department
        return "This person name is {} with an ID {} get this salary {} in department {}".format(self.emp_name,self.emp_id, self.emp_salary, self.__emp_department)
    
    def calculate_emp_salary(self,hours_work):
        if hours_work >50:
            overtime= hours_work-50
            amount=(overtime * (self.emp_salary/50))
            return amount
        else:
            return self.emp_salary

p1=Person("ADAMS","E7876",50000,"ACCOUNTING")
p2=Person("JONS","E7499",45000,"RESEARCH")
p3=Person("MARTIN","E7900",50000,"SALES")
p4=Person("SMITH","E7698",55000,"OPERATIONS")

print(p3.print_employee_details())
print(p1.set_emp_department("IT"))
print(p2.calculate_emp_salary(180)) #set hour work to get yearly salary

