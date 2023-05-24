# coding=utf-8
# import unittest
# from unittestreport import TestRunner
# # 测试用例存放路径
# case_path = '.'
# suite = unittest.defaultTestLoader.discover(case_path,pattern="test*.py")
# runner = TestRunner(suite,tester="百度QA____袁亮亮",title="问诊/搜索sdk统一")
# runner.run()
#
# -*- coding: UTF-8 -*-
"""
@Authors      : v_yuanliangliang
@Date         : 2023-3-9 10:51:48
@LastEditors  : v_yuanliangliang(v_yuanliangliang@baidu.com)
@LastEditTime : 2023-3-9 10:51:48
@Description  : 问诊/搜索sdk统一
@Copyright (c) 2021 Baidu.com, Inc. All Rights Reserved.
"""
import unittest
from unittestreport import TestRunner


def wz_diff_reports():
    """
    加载用例
    """
    case_path = '.'
    suite = unittest.defaultTestLoader.discover(case_path, pattern="test*.py")
    runner = TestRunner(suite, tester="百度QA--袁亮亮", title="问诊/搜索场景sdk统一", templates=2)
    runner.run()

wz_diff_reports()
