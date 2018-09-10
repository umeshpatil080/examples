#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      pumesh
#
# Created:     06/08/2017
# Copyright:   (c) pumesh 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------

class Employee:
    'Employee class description here'
    empCount = 0

    def __init__(self, id, name):
        self.name = name;
        self.id   = id;
        self.__fullname = name + " last name here"
        Employee.empCount += 1;

    @staticmethod
    def showEmpCount():
        print("Toatal employees:%d" % Employee.empCount);

    def showEmployeeDetails(self):
        print("Employee id:%d\tEmployee name:%s" % (self.id, self.name));


if __name__ == '__main__':
    emp = Employee(1, 'sam');
    Employee.showEmpCount();
    emp.showEmployeeDetails();
    emp.name ='sam1';
    emp.showEmployeeDetails();

    print("Name mangling:{}".format(emp._Employee__fullname))
