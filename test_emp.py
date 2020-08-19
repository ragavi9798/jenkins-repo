import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('setupClass')

    @classmethod
    def tearDownClass(cls):
        print('teardownClass')

    def setUp(self):
        print('setUp')
        self.emp_1 = Employee('Ragavi', 'Karthikeyan', 5000, 1.5)
        self.emp_2 = Employee('Sangavi', 'Karthikeyan', -6000, 1.5)

    def tearDown(self):
        print('tearDown\n')

    def test_email(self):
        print('test_email')
        self.assertTrue('self.emp_1.email'.islower())
        self.assertTrue('self.emp_2.email'.islower())
		
        self.assertEqual(self.emp_1.email, 'ragavi.karthikeyan@email.com')
        self.assertEqual(self.emp_2.email, 'sangavi.karthikeyan@email.com')

        self.emp_1.first = 'Jay'
        self.emp_2.first = 'Abhi'

        self.assertEqual(self.emp_1.email, 'jay.karthikeyan@email.com')
        self.assertEqual(self.emp_2.email, 'abhi.karthikeyan@email.com')

    def test_fullname(self):
        print('test_fullname')
        self.assertEqual(self.emp_1.fullname, 'Ragavi Karthikeyan')
        self.assertEqual(self.emp_2.fullname, 'Sangavi Karthikeyan')

        self.emp_1.first = 'Jay'
        self.emp_2.first = 'Abhi'

        self.assertEqual(self.emp_1.fullname, 'Jay Karthikeyan')
        self.assertEqual(self.emp_2.fullname, 'Abhi Karthikeyan')

    def test_apply_raise(self):
        print('test_apply_raise')
        self.emp_1.apply_raise()

        self.assertEqual(self.emp_1.pay, 7500)
        with self.assertRaises(ValueError):
            self.emp_2.apply_raise()

if __name__ == '__main__':
    unittest.main()
