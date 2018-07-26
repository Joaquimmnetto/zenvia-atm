import unittest
from test.test_bank_note_manager import BankNoteManagerTest


if __name__=='__main__':
    test_dir = 'test'
    suite = unittest.TestLoader().discover(test_dir)
    runner = unittest.TextTestRunner()
    result = runner.run(suite)