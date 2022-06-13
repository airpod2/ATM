import unittest
from unittest.mock import patch
from ATM_project import ATM

class TddTest(unittest.TestCase):
    def setUp(self):
        self.cardNum = 1234567890123456
        self.balance = 10000
        self.accounts = [1,2,4]
    
    def test_read_card(self):
        atm = ATM()
        result = atm.read_card(self.cardNum)
        self.assertEqual(result, self.cardNum)
    
    def test_read_invalid_card(self):
        atm = ATM()
        with self.assertRaises(SystemExit):
            # len(cardNum) != 16 or a cardNum contains any chars but numbers
            atm.read_card(123456789) #examples : -123456789 / 1112

    @patch('builtins.input', side_effect=['1234'])
    def test_PIN(self, user_input):
        atm = ATM()
        result = atm.PIN()
        self.assertEqual(result, 1234)

    def test_verify_PIN_true(self):
        atm = ATM()
        isTrue = atm.verify_PIN(True)
        self.assertTrue(isTrue)
    
    def test_verify_PIN_false(self):
        atm = ATM()
        with self.assertRaises(SystemExit):
            for _ in range(5): #user has 5 chances to enter a PIN
                atm.verify_PIN(False)
    
    @patch('builtins.input', side_effect=['1'])
    def test_select_account(self, user_input):
        atm = ATM()
        result = atm.select_account(self.accounts)
        self.assertEqual(result, 1)
    
    @patch('builtins.input', side_effect=['3'])
    def test_select_invalid_account(self, invalid_user_input):
        atm = ATM()
        result = atm.select_account(self.accounts)
        self.assertEqual(result, "error")
    
    def test_load_account(self):
        atm = ATM()
        atm.load_account(self.balance)
        self.assertEqual(atm.balance, self.balance)

    @patch('builtins.input', side_effect=['1'])
    def test_show_menu_balance(self, user_input):
        atm = ATM()
        with patch.object(atm, 'check_balance') as mock:
            atm.show_menu()
        
        mock.assert_called_once()

    @patch('builtins.input', side_effect=['2'])
    def test_show_menu_deposit(self, user_input):
        atm = ATM()
        with patch.object(atm, 'deposit') as mock:
            atm.show_menu()
        
        mock.assert_called_once()

    @patch('builtins.input', side_effect=['3'])
    def test_show_menu_withdrawal(self, user_input):
        atm = ATM()
        with patch.object(atm, 'withdraw') as mock:
            atm.show_menu()

        mock.assert_called_once()

    @patch('builtins.input', side_effect=['4'])
    def test_show_menu_exit(self, user_input):
        atm = ATM()
        with patch.object(atm, 'exit_menu') as mock:
            atm.show_menu()
        
        mock.assert_called_once()
    
    @patch('builtins.input', side_effect=['5'])
    def test_show_menu_invalid(self, invalid_user_input):
        atm = ATM()
        '''
        [1] Balance Inquiry"
        [2] Deposit"
        [3] Withdrawal"
        [4] Exit"
        '''
        with patch.object(atm, 'another_transaction') as mock:
            atm.show_menu()
        
        mock.assert_called_once()

    def test_check_balance(self):
        atm = ATM()
        atm.balance = self.balance
        self.result = atm.check_balance()
        self.assertEqual(self.result, self.balance)
    
    @patch('builtins.input', side_effect=['5000'])
    def test_deposit(self, user_input):
        atm = ATM()
        atm.balance = self.balance
        result = atm.deposit()
        self.assertEqual(result, 15000)
    
    @patch('builtins.input', side_effect=['-5000'])
    def test_invalid_deposit(self, invalid_user_input):
        atm = ATM()
        atm.balance = self.balance
        # negative
        with patch.object(atm, 'another_transaction') as mock:
            atm.deposit()

        mock.assert_called_once()

    @patch('builtins.input', side_effect=['5000'])
    def test_withdraw(self, user_input):
        atm = ATM()
        atm.balance = self.balance
        result = atm.withdraw()
        self.assertEqual(result, 5000)
    
    @patch('builtins.input', side_effect=['15000']) 
    def test_invalid_withdraw(self, invalid_user_input):
        atm = ATM()
        atm.balance = self.balance
        # user_input > balance or negative
        with patch.object(atm, 'another_transaction') as mock:
            atm.withdraw()

        mock.assert_called_once()
    
    def test_exit_menu(self):
        atm = ATM()
        with self.assertRaises(SystemExit):
            atm.exit_menu()

    @patch('builtins.input', side_effect=['y'])
    def test_another_transaction_no(self, user_input):
        atm = ATM()
        with patch.object(atm, 'show_menu') as mock:
            atm.another_transaction()

        mock.assert_called_once()

    @patch('builtins.input', side_effect=['n']) 
    def test_another_transaction_no(self, user_input):
        atm = ATM()
        # Everything is possible except 'y'
        with self.assertRaises(SystemExit):
            atm.another_transaction()
             

if __name__ == '__main__':
    unittest.main()