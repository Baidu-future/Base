import unittest
from unittest import defaultTestLoader

class Test_01(unittest.TestCase):
    loader= unittest.defaultTestLoader.discover("./wz_search_sdk_test",pattern="*.py")
    print(loader)




