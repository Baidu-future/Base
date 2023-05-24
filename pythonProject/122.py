# test_demo2.py
import logging
import logging
logging.basicConfig(filename='example.log', level=logging.DEBUG)
logging.debug('this message should go to the log file')
logging.info('so should this')
logging.warning('and this, too')
class TestDome:

    def test_demo1(self):
        assert 11 == 12

    def test_demo(self):
        assert 22 == 21