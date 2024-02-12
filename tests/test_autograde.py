import unittest
import os

class TestAutograder(unittest.TestCase):
    def test_result(self):
        # check if the file `wordcloud.png` exists
        self.assertTrue(os.path.exists("wordcloud.png"), "wordcloud.png does not exist")
        # check if the file `covasim.png` exists
        self.assertTrue(os.path.exists("covasim.png"), "covasim.png does not exist")

        # check if the file `wordcloud.png` is not empty
        self.assertTrue(os.stat("wordcloud.png").st_size > 10000)
        # check if the file `covasim.png` is not empty
        self.assertTrue(os.stat("covasim.png").st_size > 100000)