import unittest

from simpleLogicParser.cli import start

class TestSimpleLogicParser(unittest.TestCase):
    def test_true_or_true_is_true(self):
        result = start(inputFile=None,trues="a,b",expr="(a OR b)")
        self.assertEqual(result, True)
    
    def test_true_or_false_is_true(self):
        result = start(inputFile=None,trues="a",expr="(a OR b)")
        self.assertEqual(result, True)

    def test_false_or_false_is_false(self):
        result = start(inputFile=None,trues="",expr="(a OR b)")
        self.assertEqual(result, False)

    def test_true_and_true_is_true(self):
        result = start(inputFile=None,trues="a,b",expr="(a AND b)")
        self.assertEqual(result, True)
    
    def test_true_and_false_is_false(self):
        result = start(inputFile=None,trues="a",expr="(a AND b)")
        self.assertEqual(result, False)

    def test_false_and_false_is_false(self):
        result = start(inputFile=None,trues="",expr="(a AND b)")
        self.assertEqual(result, False)

    def test_sid_true(self):
        result = start(inputFile=None,trues="a",expr="a")
        self.assertEqual(result, True)

    def test_sid_false(self):
        result = start(inputFile=None,trues="",expr="a")
        self.assertEqual(result, False)

    def test_bool_true(self):
        result = start(inputFile=None,trues="",expr="TRUE")
        self.assertEqual(result, True)

    def test_bool_false(self):
        result = start(inputFile=None,trues="",expr="FALSE")
        self.assertEqual(result, False)

    def test_true_and_true_and_false_is_false(self):
        result = start(inputFile=None,trues="a,b",expr="(a AND (b AND c))")
        self.assertEqual(result, False)
    
    def test_true_and_true_or_false_is_true(self):
        result = start(inputFile=None,trues="a,b",expr="(a AND (b OR c))")
        self.assertEqual(result, True)

if __name__ == '__main__':
    unittest.main()