import unittest

#follow this example to add questions b, c, and d for testing including their functions
from src.question_d.question_d import get_most_likely_ancestor_consensus

class Test_Config(unittest.TestCase):

    def test_question_d(self):
        positions = get_most_likely_ancestor_consensus("GATATATGCATATACTT", "ATAT")
        x = positions[0]
        y = positions[1]
        z = positions[2]
        self.assertEqual(x, 2)
        print(x)
        self.assertEqual(y, 4)
        print(y)
        self.assertEqual(z, 10)
        print(z)
        self.assertEqual(positions, (2,4,10))
        print(positions)


