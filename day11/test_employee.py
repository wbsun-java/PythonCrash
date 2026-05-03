import unittest
from employee import Employee


class TestEmployee(unittest.TestCase):
    """Tests for employee.py"""
    def setUp(self):
        self.employee = Employee('john', 'doe', 100000)

    def test_give_default_raise(self):
        self.employee.give_raise()
        self.assertEqual(self.employee.annual_salary, 105000)

    def test_give_custom_raise(self):
        self.employee.give_raise(10000)
        self.assertEqual(self.employee.annual_salary, 110000)


if __name__ == '__main__':
    unittest.main()
