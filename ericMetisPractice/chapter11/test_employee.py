from Employee import Employee;
import unittest;

class test_employee(unittest.TestCase):
   
    def setUp(self):
        self.defaulPayment = 200;
        self.employee = Employee('Fedor' , 'Kobak' , self.defaulPayment);
        self.riseValue = 4000;

    def test_give_default_raise(self):
        self.employee.give_raise();

        self.assertEqual(self.employee.year_payment , self.defaulPayment + 5000);

    def test_give_custom_payment(self):
        self.employee.give_raise(self.riseValue);
        self.assertEqual(self.employee.year_payment, self.defaulPayment + self.riseValue);
        
unittest.main();
