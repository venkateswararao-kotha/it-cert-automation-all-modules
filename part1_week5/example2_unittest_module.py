import unittest

import re

my_txt = "An investment in knowledge pays the best interest."


def LetterCompiler(txt):
    result = re.findall(r'([a-c]).', txt)
    return result


print(LetterCompiler(my_txt))

class TestCompiler(unittest.TestCase):

    def test_basic(self):
        testcase = "The best preparation for tomorrow is doing your best today."
        expected = ['b', 'a', 'a', 'b', 'a']
        print("This Code is Executed")
        self.assertEqual(LetterCompiler(testcase), expected)

if __name__ == '__main__':
    unittest.main()