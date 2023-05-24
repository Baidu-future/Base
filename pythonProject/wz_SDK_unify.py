FrameJsonTest的副本 (unittest.loader._FailedTest.FrameJsonTest的副本) ... ERROR
RSA加密 (unittest.loader._FailedTest.RSA加密) ... ERROR
cookie (unittest.loader._FailedTest.cookie) ... ERROR
python打开图片 (unittest.loader._FailedTest.python打开图片) ... ERROR
python打开音乐 (unittest.loader._FailedTest.python打开音乐) ... ERROR
wz_SDK_unify (unittest.loader._FailedTest.wz_SDK_unify) ... ERROR

======================================================================
ERROR: FrameJsonTest的副本 (unittest.loader._FailedTest.FrameJsonTest的副本)
----------------------------------------------------------------------
ImportError: Failed to import test module: FrameJsonTest的副本
Traceback (most recent call last):
  File "/Library/Frameworks/Python.framework/Versions/3.11/lib/python3.11/unittest/loader.py", line 407, in _find_test_path
    module = self._get_module_from_name(name)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Library/Frameworks/Python.framework/Versions/3.11/lib/python3.11/unittest/loader.py", line 350, in _get_module_from_name
    __import__(name)
  File "/Users/v_yuanliangliang/Desktop/pythonProject/FrameJsonTest的副本.py", line 13, in <module>
    import requests
ModuleNotFoundError: No module named 'requests'


======================================================================
ERROR: RSA加密 (unittest.loader._FailedTest.RSA加密)
----------------------------------------------------------------------
ImportError: Failed to import test module: RSA加密
Traceback (most recent call last):
  File "/Library/Frameworks/Python.framework/Versions/3.11/lib/python3.11/unittest/loader.py", line 407, in _find_test_path
    module = self._get_module_from_name(name)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Library/Frameworks/Python.framework/Versions/3.11/lib/python3.11/unittest/loader.py", line 350, in _get_module_from_name
    __import__(name)
  File "/Users/v_yuanliangliang/Desktop/pythonProject/RSA加密.py", line 1, in <module>
    import    rsa
ModuleNotFoundError: No module named 'rsa'


======================================================================
ERROR: cookie (unittest.loader._FailedTest.cookie)
----------------------------------------------------------------------
ImportError: Failed to import test module: cookie
Traceback (most recent call last):
  File "/Library/Frameworks/Python.framework/Versions/3.11/lib/python3.11/unittest/loader.py", line 407, in _find_test_path
    module = self._get_module_from_name(name)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Library/Frameworks/Python.framework/Versions/3.11/lib/python3.11/unittest/loader.py", line 350, in _get_module_from_name
    __import__(name)
  File "/Users/v_yuanliangliang/Desktop/pythonProject/cookie.py", line 1, in <module>
    import requests
ModuleNotFoundError: No module named 'requests'


======================================================================
ERROR: python打开图片 (unittest.loader._FailedTest.python打开图片)
----------------------------------------------------------------------
ImportError: Failed to import test module: python打开图片
Traceback (most recent call last):
  File "/Library/Frameworks/Python.framework/Versions/3.11/lib/python3.11/unittest/loader.py", line 407, in _find_test_path
    module = self._get_module_from_name(name)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Library/Frameworks/Python.framework/Versions/3.11/lib/python3.11/unittest/loader.py", line 350, in _get_module_from_name
    __import__(name)
  File "/Users/v_yuanliangliang/Desktop/pythonProject/python打开图片.py", line 1, in <module>
    from PIL import Image
ModuleNotFoundError: No module named 'PIL'


======================================================================
ERROR: python打开音乐 (unittest.loader._FailedTest.python打开音乐)
----------------------------------------------------------------------
ImportError: Failed to import test module: python打开音乐
Traceback (most recent call last):
  File "/Library/Frameworks/Python.framework/Versions/3.11/lib/python3.11/unittest/loader.py", line 407, in _find_test_path
    module = self._get_module_from_name(name)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Library/Frameworks/Python.framework/Versions/3.11/lib/python3.11/unittest/loader.py", line 350, in _get_module_from_name
    __import__(name)
  File "/Users/v_yuanliangliang/Desktop/pythonProject/python打开音乐.py", line 1, in <module>
    from playsound import  playsound
ModuleNotFoundError: No module named 'playsound'


======================================================================
ERROR: wz_SDK_unify (unittest.loader._FailedTest.wz_SDK_unify)
----------------------------------------------------------------------
ImportError: Failed to import test module: wz_SDK_unify
Traceback (most recent call last):
  File "/Library/Frameworks/Python.framework/Versions/3.11/lib/python3.11/unittest/loader.py", line 407, in _find_test_path
    module = self._get_module_from_name(name)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Library/Frameworks/Python.framework/Versions/3.11/lib/python3.11/unittest/loader.py", line 350, in _get_module_from_name
    __import__(name)
  File "/Users/v_yuanliangliang/Desktop/pythonProject/wz_SDK_unify.py", line 94
    Ran 5 tests in 0.001s
                       ^
SyntaxError: invalid decimal literal


----------------------------------------------------------------------
Ran 6 tests in 0.001s

FAILED (errors=6)
