import unittest
import main as m

class Behavior(unittest.TestCase):
    def test_behavior(self):
        self.assertEqual(list(m.duplicates([{'supplier':'A','invoice':'Inv 1'},{'supplier':'a','invoice':'inv1'},{'supplier':'B','invoice':'inv1'}]).values()),[[1,2]])
