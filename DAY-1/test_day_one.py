import unittest
import challenge1
import challenge2


class TestChallenges(unittest.TestCase):
    def test_leapYear(self):
        self.assertEqual(challenge1.my_leap_year(2012), True)


    def test_lengthOfTheLastWord(self):
        self.assertEqual(challenge2.lengthOfTheLastWord('Geek of Geek'), 4)


    


if __name__ == '__main__':
    unittest.main()