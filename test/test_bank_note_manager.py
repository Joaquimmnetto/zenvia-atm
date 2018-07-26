from src.bank_note_manager import BankNoteManager
import unittest

class BankNoteManagerTest(unittest.TestCase):

    def setUp(self):
        self.available_notes = [100, 50, 20, 10]

    def test_105_not_available_note(self):
        """
        Input: 105
        Expected: raise ValueError"
        """
        manager = BankNoteManager()
        raised = False
        try:
            manager.sort_notes(105, self.available_notes)
        except ValueError:
            raised = True
        self.assertTrue(raised)

    def test_10_1_note(self):
        """
        Input: 10
        Expected: return dictionary containing:
            value 1 in the key 10,
            value 0 in other keys
        """
        manager = BankNoteManager()
        result = manager.sort_notes(10, self.available_notes)
        self.assertTrue(result[100]==0 and result[50]==0 and result[20]==0 and result[10]==1)

    def test_20_1_note(self):
        """
        Input: 20
        Expected: return dictionary containing:
            value 1 in the key 20,
            value 0 in other keys
        """
        manager = BankNoteManager()
        result = manager.sort_notes(20, self.available_notes)
        self.assertTrue(result[100]==0 and result[50]==0 and result[20]==1 and result[10]==0)

    def test_30_2_notes(self):
        """
        Input: 30
        Expected: return dictionary containing:
            value 1 in the key 10,
            value 1 in the key 20,
            value 0 in all other keys.
        """
        manager = BankNoteManager()
        result = manager.sort_notes(30, self.available_notes)
        self.assertTrue(result[100]==0 and result[50]==0 and result[20]==1 and result[10]==1)

    def test_50_1_note(self):
        """
        Input: 50
        Expected: return dictionary containing:
            value 1 in the key 50,
            value 0 in other keys
        """
        manager = BankNoteManager()
        result = manager.sort_notes(50, self.available_notes)
        self.assertTrue(result[100]==0 and result[50]==1 and result[20]==0 and result[10]==0)

    def test_80_3_note(self):
        """
        Input: 80
        Expected: return dictionary containing:
            value 1 in the key 10,
            value 1 in the key 20,
            value 1 in the key 50,
            value 0 in all other keys.
        """
        manager = BankNoteManager()
        result = manager.sort_notes(80, self.available_notes)
        self.assertTrue(result[100]==0 and result[50]==1 and result[20]==1 and result[10]==1)

    def test_100_1_note(self):
        """
        Input: 100
        Expected: return dictionary containing:
            value 1 in the key 100,
            value 0 in other keys
        """
        manager = BankNoteManager()
        result = manager.sort_notes(100, self.available_notes)
        self.assertTrue(result[100]==1 and result[50]==0 and result[20]==0 and result[10]==0)

    def test_2080_23_note(self):
        """
        Input: 2080
        Expected: return dictionary containing:
            value 20 in the key 100,
            value 1 in the key 50,
            value 1 in the key 20,
            value 1 in the key 10,
            value 0 in other keys
        """
        manager = BankNoteManager()
        result = manager.sort_notes(2080, self.available_notes)
        self.assertTrue(result[100]==20 and result[50]==1 and result[20]==1 and result[10]==1)

if __name__=='__main__':
    unittest.main()