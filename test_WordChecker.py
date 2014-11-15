# -*- coding: utf-8 -*-

import unittest
import WordChecker


class WordCheckerTest(unittest.TestCase):

    def setUp(self):
        self.sut = WordChecker.WordChecker()

    def test_if_a_in_aligator(self):
        self.assertTrue(self.sut.contains("a", "aligator"))

    def test_if_b_in_abracadabra(self):
        self.assertTrue(self.sut.contains("b", "abracadabra"))

    def test_if_w_not_in_abracadabra(self):
        self.assertFalse(self.sut.contains("W", "abracadabra"))

    def test_if_a_in_abrac(self):
        self.assertTrue(self.sut.contains("ą", "ąbrać"))

    def test_raises_exception(self):
        with self.assertRaises(TypeError):
            self.sut.contains(1, 2)

    def test_if_a_in_list_of_words(self):
        self.assertEquals(
            [True, False],
            self.sut.words_contains("ą", "ąbrać", "aaaa"))


if __name__ == '__main__':
    unittest.main()
