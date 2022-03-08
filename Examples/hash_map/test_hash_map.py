import unittest

# This is the class we want to test. So, we need to import it
from hash_map import HashTable


class TestHashTable(unittest.TestCase):
    """
    The basic class that inherits unittest.TestCase
    """
    HT = HashTable(5)

    # test case function to check the Person.set_name function
    def test_set_1(self):
        print("Start set_name test\n")
        """
        Any method which starts with ``test_`` will considered as a test case.
        """
        val = self.HT.set(1, "shankha")
        self.assertEqual(val, None)
        val = self.HT.set(2, "shuvro")
        self.assertEqual(val, None)
        val = self.HT.set(3, "sinha")
        self.assertEqual(val, None)
        print(self.HT.table)


unittest.main(argv=[''], verbosity=2, exit=False)
