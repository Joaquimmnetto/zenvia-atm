import unittest

class BankNoteManagerTest(unittest.TestCase):

    def setup(self):
        pass

    def test_105_not_available_note(self):
        """
        Input: 105
        Expected: raise ValueException with message "Can't form 105 out of {10, 20, 50, 100}"
        """
        self.assertTrue(False)

    def test_10_1_note(self):
        """
        Input: 10
        Expected: return dictionary containing:
            value 1 in the key 10,
            value 0 in other keys
        """
        self.assertTrue(False)

    def test_20_1_note(self):
        """
        Input: 20
        Expected: return dictionary containing:
            value 1 in the key 20,
            value 0 in other keys
        """
        self.assertTrue(False)

    def test_30_2_notes(self):
        """
        Input: 30
        Expected: return dictionary containing:
            value 1 in the key 10,
            value 1 in the key 20,
            value 0 in all other keys.
        """
        self.assertTrue(False)

    def test_50_1_note(self):
        """
        Input: 50
        Expected: return dictionary containing:
            value 1 in the key 50,
            value 0 in other keys
        """
        self.assertTrue(False)

    def test_80_3_note(self):
        """
        Input: 80
        Expected: return dictionary containing:
            value 1 in the key 10,
            value 1 in the key 20,
            value 1 in the key 50,
            value 0 in all other keys.
        """
        self.assertTrue(False)

    def test_100_1_note(self):
        """
        Input: 100
        Expected: return dictionary containing:
            value 1 in the key 100,
            value 0 in other keys
        """
        self.assertTrue(False)

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
        self.assertTrue(False)

if __name__=='__main__':
    unittest.main()