"""
@Authors      : v_yuanliangliang
@Date         : 2023-02-24 11:21:00
@LastEditors  : v_yuanliangliang(v_yuanliangliang@baidu.com)
@LastEditTime : 2023-02-28 11:21:00
@Description  : 问诊/搜索策略场景切换统一SDK
@Copyright (c) 2021 Baidu.com, Inc. All Rights Reserved.
"""
import unittest
import pprint
import time
import requests
import deepdiff


class TestSearchDoctorListSdk(unittest.TestCase):
    """
    问诊/搜索场景切换sdk统一
    """

    def setUp(self):
        """
        A = 实验组
        B = 对照组
        """
        self.header_A = {
            'hcg-op': 'mesh',
            'baggage': 'x-mesh-traffic-lane=feature-baymax-search-new',
            'Cookie': 'BAIDUID=F9337E7DC2FCF704A926C8137F0D24F5:FG=1; UUAP_P_TOKEN=PT-834039015129583617-5rM3R9STZq-uuap; SECURE_UUAP_P_TOKEN=PT-834039015129583617-5rM3R9STZq-uuap; UUAP_TRACE_TOKEN=0f0f2d1e52ab59859bcddce21f7ae5b30386ac84a2552071131342c67799643e; BSG_B_TOKEN=cjso21OjSg03M6SDes/YpNr8sUzCjCh+1FAHJS9+X7iLrvhCEmdeGaeuCx7PkSUxCWAv1tlgU5TF1GkZwBG7eQnasmNozDrV0dPbCzib82o=; SECURE_BSG_B_TOKEN=cjso21OjSg03M6SDes/YpNr8sUzCjCh+1FAHJS9+X7iLrvhCEmdeGaeuCx7PkSUxCWAv1tlgU5TF1GkZwBG7eQnasmNozDrV0dPbCzib82o=; PSTM=1676873242; BIDUPSID=0C5E2DCA34A9A3298BAFC7452FDC24F7; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; BDUSS=EtuZjNYYkcwR0dIbVV1a3VTRU5aTjlrU1ZHQlhrT3FrNnozcXdYMDlkYjJveWRrRVFBQUFBJCQAAAAAAAAAAAEAAABWH-CidGltZdSswcHBwQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAPYWAGT2FgBkM; BDUSS_BFESS=EtuZjNYYkcwR0dIbVV1a3VTRU5aTjlrU1ZHQlhrT3FrNnozcXdYMDlkYjJveWRrRVFBQUFBJCQAAAAAAAAAAAEAAABWH-CidGltZdSswcHBwQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAPYWAGT2FgBkM; BDSFRCVID=T_uOJexroG0Alm5f0PBJ29PtZeKKvV3TDYLEOwXPsp3LGJLVc8u-EG0PtoaGdu_-ox8EogKK0mOTHUkF_2uxOjjg8UtVJeC6EG0Ptf8g0M5; H_BDCLCKID_SF=tRk8oI0aJDvDqTrP-trf5DCShUFs-pTdB2Q-XPoO3KJNDbCGb63J3TJXeJ3JXtQiW5cpoMbgylRp8P3y0bb2DUA1y4vp55vtHmTxoUJ2abjne-53qtnWeMLebPRiJPr9QgbPBhQ7tt5W8ncFbT7l5hKpbt-q0x-jLTnhVn0MBCK0hD0wD5thj6PVKgTa54cbb4o2WbCQ0h7m8pcN2b5oQT8FhMFtKjOM0e0HVxJ2yJ5vOPQKDpOUWfAkXpJvQnJjt2JxaqRCKKnhKq5jDh3MhP_1bhode4ROfgTy0hvctn6cShnaMUjrDRLbXU6BK5vPbNcZ0l8K3l02V-bIe-t2XjQhDHt8JT-tJJ3aQ5rtKRTffjrnhPF3BT_dXP6-hnjy3bRCWnCa5DJm85C4eq3MW4LUypjpJh3RymJ42-39LPO2hpRjyxv4-Tk0qtoxJpOJaK6x0P57HR7Wbh5vbURvD-ug3-7PaM5dtjTO2bc_5KnlfMQ_bf--QfbQ0hOhqP-jBRIEoC0XtI0hMCvPKITD-tFO5eT22-usHGnT2hcHMPoosIJqh-Fhb68rXh8HqlOJyDTia-QCtMbUoqRHXnJi0btQDPvxBf7pKbbtsl5TtUJMDnjjbborqt4be-oyKMnitIj9-pnG2hQrh459XP68bTkA5bjZKxtq3mkjbPbDfn028DKuDjtBD5b0jGRabK6aKC5bL6rJabC3SM7GXU6q2bDeQN3C2Put5JRT5qF-fxJMoR5oynj4Dp0vWtv4WbbvLT7johRTWqR4HInGqfonDh83hUQxKnQdHCOOVp5O5hvvhb6O3M7lMUKmDloOW-TB5bbPLUQF5l8-sq0x0bOte-bQXH_E5bj2qRA8oCKb3j; BDRCVFR[feWj1Vr5u3D]=I67x6TjHwwYf0; delPer=0; BAIDUID_BFESS=F9337E7DC2FCF704A926C8137F0D24F5:FG=1; BDSFRCVID_BFESS=T_uOJexroG0Alm5f0PBJ29PtZeKKvV3TDYLEOwXPsp3LGJLVc8u-EG0PtoaGdu_-ox8EogKK0mOTHUkF_2uxOjjg8UtVJeC6EG0Ptf8g0M5; H_BDCLCKID_SF_BFESS=tRk8oI0aJDvDqTrP-trf5DCShUFs-pTdB2Q-XPoO3KJNDbCGb63J3TJXeJ3JXtQiW5cpoMbgylRp8P3y0bb2DUA1y4vp55vtHmTxoUJ2abjne-53qtnWeMLebPRiJPr9QgbPBhQ7tt5W8ncFbT7l5hKpbt-q0x-jLTnhVn0MBCK0hD0wD5thj6PVKgTa54cbb4o2WbCQ0h7m8pcN2b5oQT8FhMFtKjOM0e0HVxJ2yJ5vOPQKDpOUWfAkXpJvQnJjt2JxaqRCKKnhKq5jDh3MhP_1bhode4ROfgTy0hvctn6cShnaMUjrDRLbXU6BK5vPbNcZ0l8K3l02V-bIe-t2XjQhDHt8JT-tJJ3aQ5rtKRTffjrnhPF3BT_dXP6-hnjy3bRCWnCa5DJm85C4eq3MW4LUypjpJh3RymJ42-39LPO2hpRjyxv4-Tk0qtoxJpOJaK6x0P57HR7Wbh5vbURvD-ug3-7PaM5dtjTO2bc_5KnlfMQ_bf--QfbQ0hOhqP-jBRIEoC0XtI0hMCvPKITD-tFO5eT22-usHGnT2hcHMPoosIJqh-Fhb68rXh8HqlOJyDTia-QCtMbUoqRHXnJi0btQDPvxBf7pKbbtsl5TtUJMDnjjbborqt4be-oyKMnitIj9-pnG2hQrh459XP68bTkA5bjZKxtq3mkjbPbDfn028DKuDjtBD5b0jGRabK6aKC5bL6rJabC3SM7GXU6q2bDeQN3C2Put5JRT5qF-fxJMoR5oynj4Dp0vWtv4WbbvLT7johRTWqR4HInGqfonDh83hUQxKnQdHCOOVp5O5hvvhb6O3M7lMUKmDloOW-TB5bbPLUQF5l8-sq0x0bOte-bQXH_E5bj2qRA8oCKb3j; BA_HECTOR=8g8k8l81242kag0g240h2h851i0amjb1m; ZFY=BspfeMrsojNPh:AM2jrW4WAqVmdPvpQaLSsj0wivralw:C; H_WISE_SIDS=247670; SE_LAUNCH=5:1678072918; H_WISE_SIDS_BFESS=247670; SECKEY_ABVK=IIHirHp1B/gbv04usSrzwaaMNuTGdaQpQlWYETlJ8+E=; ab_sr=1.0.1_NzAxODZjMTM1YzBmNmY5ZTI0NDFkOTQ4OTFlMjJhYmUwMTdmOGZmMTJkYzBlNzgzZmVmY2ExMTFiNDZkMzcxMjkzNjM2OGE0YmZkODQwNGQwNTg0MmRhMDkwZmNjOWJhNDM3YWYxNDZlMmRmM2Q0Y2RlYzI0NDQ5Y2M1MGFlZDM3ZDE0Njg3ZDE3NDM0ZGJiNWQ5ZWQ2MDE2MzU0ZWQ5NmFhZjg1MjI2NWZmNTZkNTA2ZmVhOTQyMzEwODU5NTE1; BMAP_SECKEY=IYzmAsW98dyi-UctlZCrJGfVUYdPlvP_zP9gi_ebfvf77jKCxofzKh0BL6qmxSUFHx6w0jL1t0hWimdDqcjfr2EzgQAyh_6FId62muooGWDMzvisuExOkNAaeCFmzjAAEduqWQGS3lcSnG6aGGsEK5lXPitF0cGOpWrf2y_r7eZnnoh_6txSQ2xp-NUx8GMM; RT="z=1&dm=baidu.com&si=4ba4e5a3-565a-48d9-91fc-d34a1da04bdb&ss=lew8zzzu&sl=2&tt=2m5&bcn=https://fclog.baidu.com/log/weirwood?type=perf&ld=3w7c&ul=ovrs&hd=ovse"; BAIDUID=B6998891775EE7E0D764D25231AD5ECA:FG=1'
        }

        self.header_B = {
            'Cookie': 'BAIDUID=B6998891775EE7E0D764D25231AD5ECA:FG=1'
        }

    def test_0_1_yishengliebiaoye(self):
        """
        医生列表页
        """
        url_A_yishengliebiaoye = "https://jiankang-dev.baidu.com/med/api/expertlist?from_sf=1&lid=5116863475&need_tab=1&openapi=1&page=1&pageSize=5&pd=med&ref=search5041&referlid=5116863475&resource_id=5216&search=%E7%BB%8F%E5%B8%B8%E6%84%9F%E5%86%92%E5%BA%94%E8%AF%A5%E6%80%8E%E4%B9%88%E5%8A%9E&search_channel=wz&search_mode=res&search_section=all&sf_ref=search5041&top_expert_ids=580187%2C2192798%2C1519329%2C2274121&tpl=feed_wenzhen&vn=med&word=%E7%BB%8F%E5%B8%B8%E6%84%9F%E5%86%92%E5%BA%94%E8%AF%A5%E6%80%8E%E4%B9%88%E5%8A%9E&uadcode=110100&hospital_name=&department_id=&template_type=&tpName=&clk_loc=search5041_module2_dxwz&referlid=5116863475&applid=2166588195&reqId=AIGOBBLFGE\""
        response_A_yishengliebiaoye = requests.request("GET", url_A_yishengliebiaoye, headers=self.header_A).json()
        # print(type(response_A_yishengliebiaoye))
        time.sleep(2)
        url_B_yishengliebiaoye = "https://expert.baidu.com/med/api/expertlist?from_sf=1&lid=5116863475&need_tab=1&openapi=1&page=1&pageSize=5&pd=med&ref=search5041&referlid=5116863475&resource_id=5216&search=%E7%BB%8F%E5%B8%B8%E6%84%9F%E5%86%92%E5%BA%94%E8%AF%A5%E6%80%8E%E4%B9%88%E5%8A%9E&search_channel=wz&search_mode=res&search_section=all&sf_ref=search5041&top_expert_ids=580187%2C2192798%2C1519329%2C2274121&tpl=feed_wenzhen&vn=med&word=%E7%BB%8F%E5%B8%B8%E6%84%9F%E5%86%92%E5%BA%94%E8%AF%A5%E6%80%8E%E4%B9%88%E5%8A%9E&uadcode=110100&hospital_name=&department_id=&template_type=&tpName=&clk_loc=search5041_module2_dxwz&referlid=5116863475&applid=2166588195&reqId=AIGOBBLFGE"
        response_B_yishengliebiaoye = requests.request("GET", url_B_yishengliebiaoye, headers=self.header_B).json()
        time.sleep(2)
        diff = deepdiff.DeepDiff(response_B_yishengliebiaoye, response_A_yishengliebiaoye)
        print("A = 实验组，B = 对照组")
        print("1.医生列表页老接口")
        print('url_A_yishengliebiaoye:', url_A_yishengliebiaoye)
        print('url_B_yishengliebiaoye:', url_B_yishengliebiaoye)
        print("1--B--A  diff")
        pprint.pprint(diff)

    def test_0_2_nankezhongxin(self):
        """
        男科中心
        """
        url_A_nankezhongxin = "https://jiankang-dev.baidu.com/wz/diseasecenter/page/nanke?sf_ref=search5041&clk_loc=search5041_module2_dxwz&referlid=1774768822&applid=&lid=1774768822&reqId=IDLOJHAENC&hcg-op=mesh&baggage=x-mesh-traffic-lane=feature-baymax-search-new"
        response_A_nankezhongxin = requests.request("GET", url_A_nankezhongxin, headers=self.header_A).json()
        time.sleep(2)
        url_B_nankezhongxin = "https://expert.baidu.com/wz/diseasecenter/page/nanke?sf_ref=search5041&clk_loc=search5041_module2_dxwz&referlid=1774768822&applid=&lid=1774768822&reqId=IDLOJHAENC"
        response_B_nankezhongxin = requests.request("GET", url_B_nankezhongxin, headers=self.header_B).json()
        time.sleep(2)
        diff = deepdiff.DeepDiff(response_B_nankezhongxin, response_A_nankezhongxin)
        print("2.男科中心")
        print('url_A_nankezhongxin:', url_A_nankezhongxin)
        print('url_B_nankezhongxin:', url_B_nankezhongxin)
        print("2--B--A  diff")
        pprint.pprint(diff)

        self.assertEqual(1,2,3)
        self.assertTrue(diff(True))


    def test_0_3_sanwensandayizheng(self):
        """
        三问三答义诊
        """
        url_A_sanwensandayizhen = "https://jiankang-dev.baidu.com/wz/api/uiservice/zhenqian/expert_list_yizhen?search=&pageNo=1&pageSize=10&ranktype=%E6%8C%89%E4%BB%B7%E6%A0%BC%E5%8D%87%E5%BA%8F&department=&sf_ref=&adcode=&referlid=0295952910&applid=2190865261&lid=4370098844&v=&reqId=KEKONJOOFB"
        response_A_sanwensandayizhen = requests.request("GET", url_A_sanwensandayizhen, headers=self.header_A).json()
        time.sleep(2)
        url_B_sanwensandayizhen = "https://jiankang.baidu.com/wz/api/uiservice/zhenqian/expert_list_yizhen?search=&pageNo=1&pageSize=10&ranktype=%E6%8C%89%E4%BB%B7%E6%A0%BC%E5%8D%87%E5%BA%8F&department=&sf_ref=&adcode=&referlid=0295952910&applid=2190865261&lid=4370098844&v=&reqId=KEKONJOOFB"
        response_B_sanwensandayizhen = requests.request("GET", url_B_sanwensandayizhen, headers=self.header_B).json()
        time.sleep(2)
        diff = deepdiff.DeepDiff(response_B_sanwensandayizhen, response_A_sanwensandayizhen)
        print("3.三问三答义诊")
        print('url_A_sanwensandayizhen:', url_A_sanwensandayizhen)
        print('url_B_sanwensandayizhen:', url_B_sanwensandayizhen)
        print("3--B--A  diff")
        pprint.pprint(diff)

    def test_0_4_dingxiangIM(self):
        """
        定向IM/互医轻咨询（老）
        """
        url_A_dingxiangIM = "https://jiankang-dev.baidu.com/wz/direct/aitriage?pd=med&openapi=1&from_sf=1&resource_id=5216&vn=med&expert_id=593376&title=%E7%8E%8B%E7%8F%8F%E5%8C%BB%E7%94%9F&isDirected=1&word=%E9%97%AE%E5%8C%BB%E7%94%9F&from=jingxuandoctor&recallfrom=pageId%253D2207147640%2526rec_phase%253Dzhuanqu%2526queue%253Djingxuan%2526qtag%253Djingxuan&atn=triage&sf_ref=search5041&lid=9295726334&referlid=2207139395&clk_loc=search5041_module2_dxwz&applid=&reqId=CAHKINLCNN&aid=6810&z=&jt=a9iUjnJblv%2BQu3Rz%2BVQ6kZwEPfNq32xrVncjTRR2cEXvTkAp5c%2FyCxttG5EuFVw3Qwiu7eUe71M8CbfL7nuP7vZJJJYMaZ%2ByCVsTZ9lCEiqiZb9RnfnBJ4lKV67kz9T94e8XGywOh8OyRaSp4yYzv7G006J7ofG%2BaAxd6eyHdfogm%2FRty5iq%2FDML7L0Abfb%2FrruOj%2F1zKsBwefWcVdHgmCcRTI1G4MggBWWt8okgaeccuhhhg6omJraW0sh%2BLTr4PvEstVCN8hjWRJoZyVDLrR9HM7kkX5F84uKShtbFe83kj%2BEjOh%2BTzNVzMx%2F28c%2FY2q1OW3DevjqRqkso9kNl7Jfca99iiWWMwR1%2FXS8QgjyQo%2BabBrY3412tXIYnZVPOG2gIOUYEbHrp0J4r47EtLYM%2Ftj9ROmIgQXFk6r91RvSxxrrgYikQGrtInXDC2lTVM9LbNSXnGE13okO7DJsorv%2Fk5%2Bh7KHlXqCEzzIwIFHyYaH3188qrbjyEqaoi43cZA5E8UxzdB4PCQGg1QYBMyWEak0t0rktt31ArVw3xbFc%3D%7CVecN%2B%2BIBgvlVzFYMGiTYMG4PiSnCW%2BypYA2uNXuv5q4%3D%7C10%7C182400c7940d45fb6095bf78139d3184&ev=page_enter&to=40%24000016764551939182951618596416764551939182438ff187dae27&view=02120d000000000000000000000000000000000000000000000000008401ff8000000000000000000000000000000000000000000000000000000000&os=1&os_version=iOS%2013.2.3&model=iPhone%20X&app=universe&zid=&mode=2&brand=iPhone%20X&reso=%27390x844%27"
        response_A_dingxiangIM = requests.request("GET", url_A_dingxiangIM, headers=self.header_A).json()
        url_B_dingxiangIM = "https://expert.baidu.com/wz/direct/aitriage?pd=med&openapi=1&from_sf=1&resource_id=5216&vn=med&expert_id=593376&title=%E7%8E%8B%E7%8F%8F%E5%8C%BB%E7%94%9F&isDirected=1&word=%E9%97%AE%E5%8C%BB%E7%94%9F&from=jingxuandoctor&recallfrom=pageId%253D2207147640%2526rec_phase%253Dzhuanqu%2526queue%253Djingxuan%2526qtag%253Djingxuan&atn=triage&sf_ref=search5041&lid=9295726334&referlid=2207139395&clk_loc=search5041_module2_dxwz&applid=&reqId=CAHKINLCNN&aid=6810&z=&jt=a9iUjnJblv%2BQu3Rz%2BVQ6kZwEPfNq32xrVncjTRR2cEXvTkAp5c%2FyCxttG5EuFVw3Qwiu7eUe71M8CbfL7nuP7vZJJJYMaZ%2ByCVsTZ9lCEiqiZb9RnfnBJ4lKV67kz9T94e8XGywOh8OyRaSp4yYzv7G006J7ofG%2BaAxd6eyHdfogm%2FRty5iq%2FDML7L0Abfb%2FrruOj%2F1zKsBwefWcVdHgmCcRTI1G4MggBWWt8okgaeccuhhhg6omJraW0sh%2BLTr4PvEstVCN8hjWRJoZyVDLrR9HM7kkX5F84uKShtbFe83kj%2BEjOh%2BTzNVzMx%2F28c%2FY2q1OW3DevjqRqkso9kNl7Jfca99iiWWMwR1%2FXS8QgjyQo%2BabBrY3412tXIYnZVPOG2gIOUYEbHrp0J4r47EtLYM%2Ftj9ROmIgQXFk6r91RvSxxrrgYikQGrtInXDC2lTVM9LbNSXnGE13okO7DJsorv%2Fk5%2Bh7KHlXqCEzzIwIFHyYaH3188qrbjyEqaoi43cZA5E8UxzdB4PCQGg1QYBMyWEak0t0rktt31ArVw3xbFc%3D%7CVecN%2B%2BIBgvlVzFYMGiTYMG4PiSnCW%2BypYA2uNXuv5q4%3D%7C10%7C182400c7940d45fb6095bf78139d3184&ev=page_enter&to=40%24000016764551939182951618596416764551939182438ff187dae27&view=02120d000000000000000000000000000000000000000000000000008401ff8000000000000000000000000000000000000000000000000000000000&os=1&os_version=iOS%2013.2.3&model=iPhone%20X&app=universe&zid=&mode=2&brand=iPhone%20X&reso=%27390x844%27"
        response_B_dingxiangIM = requests.request("GET", url_B_dingxiangIM, headers=self.header_B).json()
        diff = deepdiff.DeepDiff(response_B_dingxiangIM, response_A_dingxiangIM)
        print("4.定向IM/互医轻咨询（老）")
        print('url_A_dingxiangIM:', url_A_dingxiangIM)
        print('url_B_dingxiangIM:', url_B_dingxiangIM)
        print("4--B--A  diff")
        pprint.pprint(diff)

    def test_0_5_jingxuanyishengzhuanqu(self):
        """
        精选医生专区
        """
        url_A_jingxuanyishengzhuanqu = "https://jiankang-dev.baidu.com/med/api/jingxuan?pd=med&openapi=1&from_sf=1&resource_id=5216&vn=med&source=zhuanqu&uiType=green&department=%E7%83%AD%E9%97%A8%E7%A7%91%E5%AE%A4&pageSize=5&page=1&word=&ref=sigma&lid=5313902412&referlid=2459621671"
        response_A_jingxuanyishengzhuanqu = requests.request("GET", url_A_jingxuanyishengzhuanqu,
                                                             headers=self.header_A).json()
        url_B_jingxuanyishengzhuanqu = "https://expert.baidu.com/med/api/jingxuan?pd=med&openapi=1&from_sf=1&resource_id=5216&vn=med&source=zhuanqu&uiType=green&department=%E7%83%AD%E9%97%A8%E7%A7%91%E5%AE%A4&pageSize=5&page=1&word=&ref=sigma&lid=5313902412&referlid=2459621671"
        response_B_jingxuanyishengzhuanqu = requests.request("GET", url_B_jingxuanyishengzhuanqu,
                                                             headers=self.header_B).json()
        diff = deepdiff.DeepDiff(response_B_jingxuanyishengzhuanqu, response_A_jingxuanyishengzhuanqu)
        print("5.精选医生专区")
        print('url_A_jingxuanyishengzhuanqu:', url_A_jingxuanyishengzhuanqu)
        print('url_B_jingxuanyishengzhuanqu:', url_B_jingxuanyishengzhuanqu)
        print("5--B--A  diff")
        pprint.pprint(diff)

    def test_0_6_wenzhenchonggou(self):
        """
        千分之一流量-问诊重构
        """
        url_A_wenzhenchonggou = "https://jiankang-dev.baidu.com/wzcui/uiservice/zhenqian/zhusu/getMsgList?isDirected=1&expert_id=593376&from_sf=1&word=%E9%97%AE%E5%8C%BB%E7%94%9F&sf_ref=search5041&from=jingxuandoctor&referlid=2200226140&lid=1774768822&recallfrom=pageId%3D2200239124%26rec_phase%3Dzhuanqu%26queue%3Djingxuan%26qtag%3Djingxuan"
        response_A_wenzhenchonggou = requests.request("GET", url_A_wenzhenchonggou, headers=self.header_A).json()
        url_B_wenzhenchonggou = "https://expert.baidu.com/wzcui/uiservice/zhenqian/zhusu/getMsgList?isDirected=1&expert_id=593376&from_sf=1&word=%E9%97%AE%E5%8C%BB%E7%94%9F&sf_ref=search5041&from=jingxuandoctor&referlid=2200226140&lid=1774768822&recallfrom=pageId%3D2200239124%26rec_phase%3Dzhuanqu%26queue%3Djingxuan%26qtag%3Djingxuan"
        response_B_wenzhenchonggou = requests.request("GET", url_B_wenzhenchonggou, headers=self.header_B).json()
        diff = deepdiff.DeepDiff(response_B_wenzhenchonggou, response_A_wenzhenchonggou)
        print("6.千分之一流量-问诊重构")
        print('url_A_wenzhenchonggou:', url_A_wenzhenchonggou)
        print('url_B_wenzhenchonggou:', url_B_wenzhenchonggou)
        print("6--B--A  diff")
        pprint.pprint(diff)

    def test_0_7_cmsyemian(self):
        """
        cms页面
        """
        url_A_cmsyemian = "https://jiankang-dev.baidu.com/wzcui/uiservice/zhenqian/zhusu/getMsgList?isDirected=1&expert_id=593376&from_sf=1&word=%E9%97%AE%E5%8C%BB%E7%94%9F&sf_ref=search5041&from=jingxuandoctor&referlid=2200226140&lid=1774768822&recallfrom=pageId%3D2200239124%26rec_phase%3Dzhuanqu%26queue%3Djingxuan%26qtag%3Djingxuan"
        response_A_cmsyemian = requests.request("GET", url_A_cmsyemian, headers=self.header_A).json()
        url_B_cmsyemian = "https://expert.baidu.com/wzcui/uiservice/zhenqian/zhusu/getMsgList?isDirected=1&expert_id=593376&from_sf=1&word=%E9%97%AE%E5%8C%BB%E7%94%9F&sf_ref=search5041&from=jingxuandoctor&referlid=2200226140&lid=1774768822&recallfrom=pageId%3D2200239124%26rec_phase%3Dzhuanqu%26queue%3Djingxuan%26qtag%3Djingxuan"
        response_B_cmsyemian = requests.request("GET", url_B_cmsyemian, headers=self.header_B).json()
        diff = deepdiff.DeepDiff(response_B_cmsyemian, response_A_cmsyemian)
        print("7.cms页面")
        print('url_A_cmsyemian:', url_A_cmsyemian)
        print('url_B_cmsyemian:', url_B_cmsyemian)
        print("7--B--A  diff")
        pprint.pprint(diff)

    def test_0_8_yishengliebiaoqianru_iframe(self):
        """
        自建页-嵌入医生列表iframe
        """
        url_A_yishengliebiaoqianru_iframe = "https://jiankang-dev.baidu.com/med/api/expertlist?from_sf=1&lid=4.288510184e%252B09&need_tab=1&openapi=1&page=1&pageSize=5&pd=med&ref=landingTopic&referlid=4.288510184e%252B09&resource_id=5216&search=%E8%82%BA%E7%99%8C%E6%99%9A%E6%9C%9F%E8%83%BD%E6%B4%BB%E5%A4%9A%E4%B9%85%E5%91%A2&search_channel=wz&search_mode=res&search_section=all&sf_ref=landingTopic&tpl=feed_wenzhen&vn=med&word=%E8%82%BA%E7%99%8C%E6%99%9A%E6%9C%9F%E8%83%BD%E6%B4%BB%E5%A4%9A%E4%B9%85%E5%91%A2&originalQuery=%E8%82%BA%E7%99%8C%E6%99%9A%E6%9C%9F%E8%83%BD%E6%B4%BB%E5%A4%9A%E4%B9%85%E5%91%A2%EF%BC%9F&rec_from=wenzhen_self_disease_center&self_user_tag=%5B%5B%7B%22id%22%3A388937185878272%2C%22name%22%3A%22%E5%91%BC%E5%90%B8%E7%B3%BB%E7%BB%9F%E7%96%BE%E7%97%85%22%7D%2C%7B%22id%22%3A388937325924608%2C%22name%22%3A%22%E8%82%BA%E7%99%8C%22%7D%2C%7B%22id%22%3A388938605068544%2C%22name%22%3A%22%E7%96%BE%E7%97%85%E5%88%86%E5%9E%8B%22%7D%2C%7B%22id%22%3A388938890148096%2C%22name%22%3A%22%E5%B0%8F%E7%BB%86%E8%83%9E%E8%82%BA%E7%99%8C%22%7D%5D%2C%5B%7B%22id%22%3A388937185878272%2C%22name%22%3A%22%E5%91%BC%E5%90%B8%E7%B3%BB%E7%BB%9F%E7%96%BE%E7%97%85%22%7D%2C%7B%22id%22%3A388937325924608%2C%22name%22%3A%22%E8%82%BA%E7%99%8C%22%7D%2C%7B%22id%22%3A388938605253888%2C%22name%22%3A%22%E7%96%BE%E7%97%85%E9%98%B6%E6%AE%B5%22%7D%2C%7B%22id%22%3A388938910919936%2C%22name%22%3A%22%E6%97%A9%E6%9C%9F%22%7D%5D%5D&uadcode=110100&hospital_name=&department_id=&template_type=&tpName=&screen=authorityDoctor%2Ciscanguahao&searchID=42885102477569&referlid=4.288510184e%252B09&applid=4289034862&reqId=DJPMEFCIGH"
        response_A_yishengliebiaoqianru_iframe = requests.request("GET", url_A_yishengliebiaoqianru_iframe,
                                                                  headers=self.header_A).json()

        url_B_yishengliebiaoqianru_iframe = "https://expert.baidu.com/med/api/expertlist?from_sf=1&lid=4.288510184e%252B09&need_tab=1&openapi=1&page=1&pageSize=5&pd=med&ref=landingTopic&referlid=4.288510184e%252B09&resource_id=5216&search=%E8%82%BA%E7%99%8C%E6%99%9A%E6%9C%9F%E8%83%BD%E6%B4%BB%E5%A4%9A%E4%B9%85%E5%91%A2&search_channel=wz&search_mode=res&search_section=all&sf_ref=landingTopic&tpl=feed_wenzhen&vn=med&word=%E8%82%BA%E7%99%8C%E6%99%9A%E6%9C%9F%E8%83%BD%E6%B4%BB%E5%A4%9A%E4%B9%85%E5%91%A2&originalQuery=%E8%82%BA%E7%99%8C%E6%99%9A%E6%9C%9F%E8%83%BD%E6%B4%BB%E5%A4%9A%E4%B9%85%E5%91%A2%EF%BC%9F&rec_from=wenzhen_self_disease_center&self_user_tag=%5B%5B%7B%22id%22%3A388937185878272%2C%22name%22%3A%22%E5%91%BC%E5%90%B8%E7%B3%BB%E7%BB%9F%E7%96%BE%E7%97%85%22%7D%2C%7B%22id%22%3A388937325924608%2C%22name%22%3A%22%E8%82%BA%E7%99%8C%22%7D%2C%7B%22id%22%3A388938605068544%2C%22name%22%3A%22%E7%96%BE%E7%97%85%E5%88%86%E5%9E%8B%22%7D%2C%7B%22id%22%3A388938890148096%2C%22name%22%3A%22%E5%B0%8F%E7%BB%86%E8%83%9E%E8%82%BA%E7%99%8C%22%7D%5D%2C%5B%7B%22id%22%3A388937185878272%2C%22name%22%3A%22%E5%91%BC%E5%90%B8%E7%B3%BB%E7%BB%9F%E7%96%BE%E7%97%85%22%7D%2C%7B%22id%22%3A388937325924608%2C%22name%22%3A%22%E8%82%BA%E7%99%8C%22%7D%2C%7B%22id%22%3A388938605253888%2C%22name%22%3A%22%E7%96%BE%E7%97%85%E9%98%B6%E6%AE%B5%22%7D%2C%7B%22id%22%3A388938910919936%2C%22name%22%3A%22%E6%97%A9%E6%9C%9F%22%7D%5D%5D&uadcode=110100&hospital_name=&department_id=&template_type=&tpName=&screen=authorityDoctor%2Ciscanguahao&searchID=42885102477569&referlid=4.288510184e%252B09&applid=4289034862&reqId=DJPMEFCIGH"
        response_B_yishengliebiaoqianru_iframe = requests.request("GET", url_B_yishengliebiaoqianru_iframe,
                                                                  headers=self.header_B).json()
        diff = deepdiff.DeepDiff(response_B_yishengliebiaoqianru_iframe, response_A_yishengliebiaoqianru_iframe)
        print("8.自建页-嵌入医生列表iframe")
        print('url_A_yishengliebiaoqianru_iframe:', url_A_yishengliebiaoqianru_iframe)
        print('url_B_yishengliebiaoqianru_iframe:', url_B_yishengliebiaoqianru_iframe)
        print("8--B--A  diff")
        pprint.pprint(diff)

    def test_0_9_yiyuantiaozhuanyishengluodiye(self):
        """
        医院跳转医生落地页
        """
        url_A_yiyuantiaozhuanyishengluodiye = "https://jiankang-dev.baidu.com/med/api/expertlist?from_sf=1&lid=4.288510184e%252B09&need_tab=1&openapi=1&page=1&pageSize=5&pd=med&ref=landingTopic&referlid=4.288510184e%252B09&resource_id=5216&search=%E8%82%BA%E7%99%8C%E6%99%9A%E6%9C%9F%E8%83%BD%E6%B4%BB%E5%A4%9A%E4%B9%85%E5%91%A2&search_channel=wz&search_mode=res&search_section=all&sf_ref=landingTopic&tpl=feed_wenzhen&vn=med&word=%E8%82%BA%E7%99%8C%E6%99%9A%E6%9C%9F%E8%83%BD%E6%B4%BB%E5%A4%9A%E4%B9%85%E5%91%A2&originalQuery=%E8%82%BA%E7%99%8C%E6%99%9A%E6%9C%9F%E8%83%BD%E6%B4%BB%E5%A4%9A%E4%B9%85%E5%91%A2%EF%BC%9F&rec_from=wenzhen_self_disease_center&self_user_tag=%5B%5B%7B%22id%22%3A388937185878272%2C%22name%22%3A%22%E5%91%BC%E5%90%B8%E7%B3%BB%E7%BB%9F%E7%96%BE%E7%97%85%22%7D%2C%7B%22id%22%3A388937325924608%2C%22name%22%3A%22%E8%82%BA%E7%99%8C%22%7D%2C%7B%22id%22%3A388938605068544%2C%22name%22%3A%22%E7%96%BE%E7%97%85%E5%88%86%E5%9E%8B%22%7D%2C%7B%22id%22%3A388938890148096%2C%22name%22%3A%22%E5%B0%8F%E7%BB%86%E8%83%9E%E8%82%BA%E7%99%8C%22%7D%5D%2C%5B%7B%22id%22%3A388937185878272%2C%22name%22%3A%22%E5%91%BC%E5%90%B8%E7%B3%BB%E7%BB%9F%E7%96%BE%E7%97%85%22%7D%2C%7B%22id%22%3A388937325924608%2C%22name%22%3A%22%E8%82%BA%E7%99%8C%22%7D%2C%7B%22id%22%3A388938605253888%2C%22name%22%3A%22%E7%96%BE%E7%97%85%E9%98%B6%E6%AE%B5%22%7D%2C%7B%22id%22%3A388938910919936%2C%22name%22%3A%22%E6%97%A9%E6%9C%9F%22%7D%5D%5D&uadcode=110100&hospital_name=&department_id=&template_type=&tpName=&screen=authorityDoctor%2Ciscanguahao&searchID=42885102477569&referlid=4.288510184e%252B09&applid=4289034862&reqId=DJPMEFCIGH"
        response_A_yiyuantiaozhuanyishengluodiye = requests.request("GET", url_A_yiyuantiaozhuanyishengluodiye,
                                                                    headers=self.header_A).json()
        time.sleep(2)
        url_B_yiyuantiaozhuanyishengluodiye = "https://expert.baidu.com/med/api/expertlist?from_sf=1&lid=4.288510184e%252B09&need_tab=1&openapi=1&page=1&pageSize=5&pd=med&ref=landingTopic&referlid=4.288510184e%252B09&resource_id=5216&search=%E8%82%BA%E7%99%8C%E6%99%9A%E6%9C%9F%E8%83%BD%E6%B4%BB%E5%A4%9A%E4%B9%85%E5%91%A2&search_channel=wz&search_mode=res&search_section=all&sf_ref=landingTopic&tpl=feed_wenzhen&vn=med&word=%E8%82%BA%E7%99%8C%E6%99%9A%E6%9C%9F%E8%83%BD%E6%B4%BB%E5%A4%9A%E4%B9%85%E5%91%A2&originalQuery=%E8%82%BA%E7%99%8C%E6%99%9A%E6%9C%9F%E8%83%BD%E6%B4%BB%E5%A4%9A%E4%B9%85%E5%91%A2%EF%BC%9F&rec_from=wenzhen_self_disease_center&self_user_tag=%5B%5B%7B%22id%22%3A388937185878272%2C%22name%22%3A%22%E5%91%BC%E5%90%B8%E7%B3%BB%E7%BB%9F%E7%96%BE%E7%97%85%22%7D%2C%7B%22id%22%3A388937325924608%2C%22name%22%3A%22%E8%82%BA%E7%99%8C%22%7D%2C%7B%22id%22%3A388938605068544%2C%22name%22%3A%22%E7%96%BE%E7%97%85%E5%88%86%E5%9E%8B%22%7D%2C%7B%22id%22%3A388938890148096%2C%22name%22%3A%22%E5%B0%8F%E7%BB%86%E8%83%9E%E8%82%BA%E7%99%8C%22%7D%5D%2C%5B%7B%22id%22%3A388937185878272%2C%22name%22%3A%22%E5%91%BC%E5%90%B8%E7%B3%BB%E7%BB%9F%E7%96%BE%E7%97%85%22%7D%2C%7B%22id%22%3A388937325924608%2C%22name%22%3A%22%E8%82%BA%E7%99%8C%22%7D%2C%7B%22id%22%3A388938605253888%2C%22name%22%3A%22%E7%96%BE%E7%97%85%E9%98%B6%E6%AE%B5%22%7D%2C%7B%22id%22%3A388938910919936%2C%22name%22%3A%22%E6%97%A9%E6%9C%9F%22%7D%5D%5D&uadcode=110100&hospital_name=&department_id=&template_type=&tpName=&screen=authorityDoctor%2Ciscanguahao&searchID=42885102477569&referlid=4.288510184e%252B09&applid=4289034862&reqId=DJPMEFCIGH"
        response_B_yiyuantiaozhuanyishengluodiye = requests.request("GET", url_B_yiyuantiaozhuanyishengluodiye,
                                                                    headers=self.header_B).json()
        diff = deepdiff.DeepDiff(response_B_yiyuantiaozhuanyishengluodiye, response_A_yiyuantiaozhuanyishengluodiye)
        print("9.医院跳转医生落地页")
        print('url_A_yiyuantiaozhuanyishengluodiy:', url_A_yiyuantiaozhuanyishengluodiye)
        print('url_B_yiyuantiaozhuanyishengluodiy:', url_B_yiyuantiaozhuanyishengluodiye)
        print("9--B--A  diff")
        pprint.pprint(diff)


if __name__ == "__main__":
    unittest.main()
