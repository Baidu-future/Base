"""
@Authors      : v_yuanliangliang
@Date         : 2023-03-06 11:21:00
@LastEditors  : v_yuanliangliang(v_yuanliangliang@baidu.com)
@LastEditTime : 2023-03-06 11:21:00
@Description  : 问诊/搜索策略场景切换统一SDK
@Copyright (c) 2021 Baidu.com, Inc. All Rights Reserved.
"""
import pprint
import unittest
import deepdiff
import yaml
class TestSearchDoctorListSdk(unittest.TestCase):
    def setUp(self):
        """
        setup
        """
        yamlPath = './payload.yaml'
        with open(yamlPath, 'r', encoding="utf-8") as f:
            self.temp = yaml.load(f.read(), Loader=yaml.FullLoader)

    def test_0_1_yishengliebiao(self):
        """
        # 定向医生
        """
        result_A_dingxiangyisheng = self.temp["result_A_dingxiangyisheng"]
        result_B_dingxiangyisheng = self.temp["result_B_dingxiangyisheng"]
        diff = deepdiff.DeepDiff(result_B_dingxiangyisheng, result_A_dingxiangyisheng)
        print("1.定向医生")
        pprint.pprint(diff)

    def test_0_2_wenyishengka(self):
        """
        5192-问医生卡
        """
        result_A_wenyishengka = self.temp["result_A_wenyishengka"]
        result_B_wenyishengka = self.temp["result_B_wenyishengka"]
        diff = deepdiff.DeepDiff(result_B_wenyishengka, result_A_wenyishengka)
        print("2.5192-问医生卡")
        pprint.pprint(diff)

    def test_0_3_guahaopinpaika(self):
        """

        #5589-挂号品牌卡
        """
        result_A_guahaopinpaika = self.temp["result_A_guahaopinpaika"]
        result_B_guahaopinpaika = self.temp["result_B_guahaopinpaika"]
        diff = deepdiff.DeepDiff(result_B_guahaopinpaika, result_A_guahaopinpaika)
        print("3.5589-挂号品牌卡")
        pprint.pprint(diff)

    def test_0_4_nakepinpaika(self):
        """
        男科品牌卡
        """
        result_A_nakepinpaika = self.temp["result_A_nakepinpaika"]
        result_B_nakepinpaika = self.temp["result_B_nakepinpaika"]
        diff = deepdiff.DeepDiff(result_B_nakepinpaika, result_A_nakepinpaika)
        print("4.男科品牌卡")
        pprint.pprint(diff)


if __name__ == "__main__":
    unittest.main()
