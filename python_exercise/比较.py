import  deepdiff
import requests
import json
global false, null, true
false = null = true = ''
url = "https://jiankang-dev.baidu.com/wzcui/uiservice/zhenqian/zhusu/getMsgList?isDirected=1&expert_id=1208976&from_sf=1&referlid=2753174873&lid=8599770664"
payload = json.dumps({
  "isDirected": "1",
  "riskInfo": {
    "aid": "6810",
    "z": "",
    "jt": "0A9Z3A7+73N7zoZCUIX9ctqNtZghcyOjcIsFyBpHDomk4EpEwmTIjd6AoTNdQTcpPR8KZ2MgnGBIJOOEuwbWNj21c6HrFc/4BDg/N6fwxb6Pybd2u4RAiCMTYhdXEDu+zQZAG3QZ/01rRf5qRumZtjnUqWEQChcaWuKH2du1vX7OeckCvjl501qh8hPFRQeMs1soAC14eBWRaHumVuXg4UOfCVnV+rzRAjo+QQtC+4Ddli5PDbBZM031t8gweBaNHht7mN8L4VLU/HcymZ7T1S7SSBbrcB4VB+Ru5EuvRrLWST37yw3P6wsN8rXklJDxUYYOost+FW5DKfoH7LzANDOWMe4Ih3yuGI+ezqR/yRNPUQHn/ptpTV3ihn++8J/ULDQprQd0ViMHSSReCfvfW30hw0UBMIZwLrIpEAPslFHPCCEuhELU4Q96TDhoPh1NZSfCpMUI8Lm7E3i4OdeSKdy54Zc5La8dMeSCsKOoyvs1uMVcpyveLu6ZZqqyKyn0|t9DD3f0pbtfAuuTOqf4+94zu9EwFfQnZ7p9Y8fYQncQ=|10|f167ff268c971ef17b31f74a92d9c604",
    "ev": "page_enter",
    "to": "40$00001676457349108826519913181676457349108868619f58e5bce",
    "view": "02120d000000000000000000000000000000000000000000000000008401ff8000000000000000000000000000000000000000000000000000000000",
    "os": 0,
    "os_version": None,
    "model": "",
    "app": "universe",
    "zid": "",
    "mode": 2,
    "brand": "",
    "reso": "'1920x1080'",
    "v": ""
  },
  "page": {
    "size": 10,
    "viewType": "next"
  },
  "referlid": "6207785267",
  "applid": "",
  "lid": "2982943038",
  "v": "",
  "reqId": "DOAGLJIDBO"
})
headers = {
  'authority': 'jiankang-dev.baidu.com',
  'accept': '*/*',
  'accept-language': 'zh-CN,zh;q=0.9',
  'baggage': 'x-mesh-traffic-lane=base-stable',
  'content-type': 'application/json',
  'cookie': 'BIDUPSID=0C5E2DCA34A9A3298BAFC7452FDC24F7; BAIDUID=178EF30A517E95D6018581411F92FC3C:FG=1; PSTM=1673833326; UUAP_TRACE_TOKEN=0f0f2d1e52ab59859bcddce21f7ae5b30386ac84a2552071131342c67799643e; UUAP_P_TOKEN=PT-829354231689441280-ZkgxH9QZAr-uuap; SECURE_UUAP_P_TOKEN=PT-829354231689441280-ZkgxH9QZAr-uuap; BDUSS=01TdmtoclhRb0hLbDZjTFFESHhHYmxOZUI4Mklvb2NUclVVT1dveH5PdHN5QWxrSVFBQUFBJCQAAAAAAAAAAAEAAABWH-CidGltZdSswcHBwQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGw74mNsO-JjZ; BDUSS_BFESS=01TdmtoclhRb0hLbDZjTFFESHhHYmxOZUI4Mklvb2NUclVVT1dveH5PdHN5QWxrSVFBQUFBJCQAAAAAAAAAAAEAAABWH-CidGltZdSswcHBwQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGw74mNsO-JjZ; BSG_B_TOKEN=cjso21OjSg03M6SDes/YpCEfDq/DJRnmGieJiqjtoLqIqD4oQlC1nRPLoQkgj6lRQRIIkzJ57In3VUgbFDcqDX2fQKo2xOtZaJDb5sE1XFU=; SECURE_BSG_B_TOKEN=cjso21OjSg03M6SDes/YpCEfDq/DJRnmGieJiqjtoLqIqD4oQlC1nRPLoQkgj6lRQRIIkzJ57In3VUgbFDcqDX2fQKo2xOtZaJDb5sE1XFU=; UUAP_P_TOKEN_OFFLINE=PT-831929526824755200-8Zm018sntK-beta; SECURE_UUAP_P_TOKEN_OFFLINE=PT-831929526824755200-8Zm018sntK-beta; UUAP_TRACE_TOKEN_OFFLINE=00313a0c40ad408d93928b8b731e8ed1; delPer=0; BAIDUID_BFESS=178EF30A517E95D6018581411F92FC3C:FG=1; BA_HECTOR=25818g8hag2g25842005a1bf1huov9b1l; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; BDRCVFR[feWj1Vr5u3D]=I67x6TjHwwYf0; H_WISE_SIDS=219946_231979_234927_219623_238719_131861_231493_240447_213358_229967_214795_239101_219942_234782_204917_230288_239491_241795_242271_242312_241701_242547_242478_242453_242512_242620_242489_242754_242751_242545_238267_239307_243271_110085_227869_243510_236308_243745_243841_243706_243886_244039_244320_244007_239175_232628_244704_244726_244769_244830_240595_244955_245003_242382_242377_243208_245082_241737_245271_244445_244966_245412_245475_245520_245512_245509_245590_226006_245759_243386_243821_246046_245700_245495_245540_246324_242434_246319_246439_246424_246468_246477_242682_234296_234208_246584_245895_246613; H_WISE_SIDS_BFESS=219946_231979_234927_219623_238719_131861_231493_240447_213358_229967_214795_239101_219942_234782_204917_230288_239491_241795_242271_242312_241701_242547_242478_242453_242512_242620_242489_242754_242751_242545_238267_239307_243271_110085_227869_243510_236308_243745_243841_243706_243886_244039_244320_244007_239175_232628_244704_244726_244769_244830_240595_244955_245003_242382_242377_243208_245082_241737_245271_244445_244966_245412_245475_245520_245512_245509_245590_226006_245759_243386_243821_246046_245700_245495_245540_246324_242434_246319_246439_246424_246468_246477_242682_234296_234208_246584_245895_246613; BDPASSGATE=IlPT2AEptyoA_yiU4SO03lIN8eDEUsCD34OtVnti3ECGh67BmhH74cxHS680KyirB5Kh-YyfmqlPpjrFV6xjg0N_gRsQkSlxfFW7uq3Eq2D4Gc6MvgUZD04SGS2qxvXx8wlywOEYF3VEVFoKewPJpuo_mv3l8whwhPHGs5LJrK8Y2kWRA7r6nmapYIsJLHndN2SRyuinhSpAXymBT3LJLS87hFdGN7cEzgadgroQ3eD5rl9YIeHvYvAa1G85Jppa0ae8GPWUl1SnBE9YvCckYV1unEiV5tD6Mk9d_KvxfMxJG_rWPaL_UTrhBcs6xc01HbsnSQ3zmtkGDV9S98sUBplWC2bb088HO5sKLMibbw4TDkgVqlOEIwDLtIMQO10F_ddBL_53UCt-jyifq3PXhTi6_wPgi0FvM0wOCpePu89wdZVhHFfh88qzc7Jv-p_fT7afE5LICM0lT8Bs-weLDRLuVKr82VEbqUuloizSpSbh1QDSFt6HcFQB88V7TWiB9QePNo3XK3G_n1VA8rbB82bXu9SUqzaZwyqfRNWpZxofUZcBjKhm07rcu9ugeXx_O4GdvI4n_VDEei6xudOhpCBzlPA01NJKOtD0JPITqcOCgJk2CSYto_Sz3wFfZ7nDvwtfIdSkUIj0DFLh0WQgaqRPZTH2IJTzvtLgETVYEVCM_5n4G_xjwih2i8cEZ_bQLE8Jg3UhLFuSjxsKYOLTg8Bl_3EjEi25vXzJ3-8NCRHvcgVpwEg4sw-UOYbmRPjU7zwkgRohOzjB8rbUCreFoIIsxXf67d29LcS3X7iMxk7bHqIq-nnzEFyXiSrIuQq; PSCBD=31%3A1; SE_LAUNCH=5%3A27940922_0%3A27940922_16%3A27940925_31%3A27940925; ab_sr=1.0.1_YzQ4NTYwNTI0NGE0ZWExNTMwYzQyNDkwMzk3NDA1MGU0NTFkOTgxNWRjNWU4Y2E5ZTBmZmE1MzNiY2FlNTg2MjBkMzgzYThiYzkyYWI2ZDFhMDAyZWI2NThjNjgwZWQ2ZTYwNjUxYWQwZWZlM2ViOTI3MDVkMTExZjI0NTkzNWU2NWY0ZmMyMWY5ZmQzNzc4NmU5ZjRhYWJjMjJkOWRhYw==; X-Use-Search-BFF=1; rsv_i=a63ddaB3EoCyZkNZnQmCSFDIvfmEbJKnGFjMuBgwDN4pSGH8MFuL8gKD7Vr4GCmipauEeZ%2BZAdp9GMJ7Uj9PAK8LLGAjC%2B0; PSINO=2; H_PS_PSSID=38186_36556_37520_38093_38129_37911_38148_37990_38178_38173_37799_37937_38089_37900_26350_38120_38008_37881; BAIDUID=C0913CEC62E64C99E5F8950A0773642A:FG=1; BIDUPSID=C0913CEC62E64C99D410409F592E9FF2; PSTM=1676457306',
  'hcg-op': 'mesh',
  'origin': 'https://jiankang-dev.baidu.com',
  'referer': 'https://jiankang-dev.baidu.com/wenzhen/pages/triage/index?pd=med&openapi=1&from_sf=1&resource_id=5216&vn=med&atn=triage&title=%E5%8C%BB%E7%94%9F%E5%8A%A9%E6%89%8B&lid=8599770664&referlid=2753174873&isDirected=1&aibot=1&expert_id=1208976',
  'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"',
  'sec-ch-ua-mobile': '?1',
  'sec-ch-ua-platform': '"Android"',
  'sec-fetch-dest': 'empty',
  'sec-fetch-mode': 'cors',
  'sec-fetch-site': 'same-origin',
  'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Mobile Safari/537.36'
}

response = requests.request("POST", url, headers=headers, data=payload)
ww=response.json()
# print(type(ww))
# print(ww)
# type(response.json())
# print(type(response.json()))
# print(response.json())
aa={'status': 0, 'msg': '', 'toast': '', 'applid': '3041356263', 'lid': '', 'data': {'toolData': {'lineTools': [{'type': 'historyInfo', 'clickDisable': 0, 'optionsKey': 'entities.zhusu', 'aiParams': {'intent': 'zhusu', 'entities': {'zhusu': ''}}}, {'type': 'uploadImg', 'clickDisable': 0, 'optionsKey': 'entities.image_list', 'aiParams': {'intent': 'zhusu', 'entities': {'image_list': '', 'type': 'images'}}}]}, 'actionData': {'interaction': 'popup', 'interactionInfo': {'url': '/wzcui/uiservice/zhenqian/captcha/checkcode', 'method': 'post'}, 'actionType': 'antipass'}, 'msgData': {'1625831973265657856': {'msgId': '1625831973265657856', 'msgKey': '1625831973265657856', 'ownerType': 1, 'createTime': '1676463523580', 'updateTime': '1676463523580', 'sendTime': '1676463523580', 'contentType': 221, 'posterInfo': {'name': '', 'avatar': '', 'title': '', 'disableClickOut': False}, 'content': {'cardId': 11407, 'cardName': 'ImSystemMsg', 'data': {'cardStyle': {'renderType': 4}, 'content': {'list': [[{'type': 'icon', 'value': 'https://med-fe.cdn.bcebos.com/wechatIcon.png'}, {'type': 'text', 'value': '关注微信公众号 在线问诊低至'}, {'type': 'redText', 'value': '0 元'}], [{'type': 'secondaryText', 'value': '去关注', 'interaction': 'openLink', 'interactionInfo': {'url': '/pages/wz/followgzh/index?platform=zt_wzBdFollow_youhui'}}, {'type': 'icon', 'value': 'https://med-fe.cdn.bcebos.com/imSystemMsgRArrow.png', 'interaction': 'openLink', 'interactionInfo': {'url': '/pages/wz/followgzh/index?platform=zt_wzBdFollow_youhui'}}]]}}}, 'isCancel': 0, 'isUnread': 0, 'contentMD5': 'a156984fe3a5fdffbd80da7c2bad4e63'}, 'U_0a7723b5-165a-45d6-9c35-0c6ed57ef6b7': {'msgId': 'U_0a7723b5-165a-45d6-9c35-0c6ed57ef6b7', 'msgKey': 'U_0a7723b5-165a-45d6-9c35-0c6ed57ef6b7', 'ownerType': 1, 'createTime': '1676463524211', 'updateTime': '1676463524211', 'sendTime': '1676463524211', 'contentType': 410, 'posterInfo': {'name': '', 'avatar': '', 'title': '', 'disableClickOut': False}, 'content': {'cardId': 11502, 'cardName': 'ImFocusDoctor', 'data': {'content': {'consultCount': {}, 'replySpeed': {}, 'serviceIndicators': {}, 'assistants': {}}, 'actionInfo': {'interaction': 'openLink', 'interactionInfo': {'method': 'Get'}}}}, 'isCancel': 0, 'isUnread': 0, 'contentMD5': '9640255bb5a3b070e5b3a8234fffd7a0'}, 'U_0ff02f35-53dd-46c5-8694-eb86a7040ce2': {'msgId': 'U_0ff02f35-53dd-46c5-8694-eb86a7040ce2', 'msgKey': 'U_0ff02f35-53dd-46c5-8694-eb86a7040ce2', 'ownerType': 1, 'createTime': '1676463524211', 'updateTime': '1676463524211', 'sendTime': '1676463524211', 'contentType': 201, 'posterInfo': {'name': '', 'avatar': '', 'title': '', 'disableClickOut': False}, 'content': {'cardId': 11407, 'cardName': 'ImSystemMsg', 'data': {'cardStyle': {'renderType': 0}, 'content': {'list': [[{'type': 'text', 'value': '您的信息仅接诊医生可见，百度健康为您提供隐私保护'}]]}, 'actionInfo': {'interaction': 'request', 'interactionInfo': {'method': 'post', 'params': {'aiParams': {'entities': {'zhusu': None}, 'intent': 'zhusu'}}}}}}, 'isCancel': 0, 'isUnread': 0, 'contentMD5': 'f31417bebea9528db609e6915f4e0194'}, 'U_783c46e6-48da-46b5-8642-82f512b83d16': {'msgId': 'U_783c46e6-48da-46b5-8642-82f512b83d16', 'msgKey': 'U_783c46e6-48da-46b5-8642-82f512b83d16', 'ownerType': 2, 'createTime': '1676463524201', 'updateTime': '1676463524201', 'sendTime': '1676463524201', 'contentType': 301, 'posterInfo': {'name': '', 'avatar': 'https://med-fe.cdn.bcebos.com/wz/assistant.png', 'title': '', 'disableClickOut': False}, 'content': {'cardId': 11406, 'cardName': 'ImChoose', 'data': {'cardStyle': {'needHead': True, 'renderType': 0}, 'content': {'extendedMsg': None, 'options': [], 'optionsKey': '', 'optionsTitle': '', 'optionsType': 'radio', 'title': '请您尽可能详细地描述您的问题（具体症状、患病时长、用药情况等，10-500字）'}, 'actionInfo': {'interaction': 'request', 'interactionInfo': {'method': 'post', 'params': {'aiParams': {'entities': None, 'intent': ''}}}}}}, 'isCancel': 0, 'isUnread': 0, 'contentMD5': 'a96d1b79825127a9ece1a0aac6c83897'}, 'U_ed77756d-5916-47f0-8315-448cdb8d8f61': {'msgId': 'U_ed77756d-5916-47f0-8315-448cdb8d8f61', 'msgKey': 'U_ed77756d-5916-47f0-8315-448cdb8d8f61', 'ownerType': 2, 'createTime': '1676463524201', 'updateTime': '1676463524201', 'sendTime': '1676463524201', 'contentType': 301, 'posterInfo': {'name': '', 'avatar': 'https://med-fe.cdn.bcebos.com/wz/assistant.png', 'title': '', 'disableClickOut': False}, 'content': {'cardId': 11406, 'cardName': 'ImChoose', 'data': {'cardStyle': {'needHead': True, 'renderType': 0}, 'content': {'extendedMsg': None, 'options': [], 'optionsKey': '', 'optionsTitle': '', 'optionsType': 'radio', 'title': '您好，我是您的医生助手，需要了解您的情况辅助医生更好地诊断。'}, 'actionInfo': {'interaction': 'request', 'interactionInfo': {'method': 'post', 'params': {'aiParams': {'entities': None, 'intent': ''}}}}}}, 'isCancel': 0, 'isUnread': 0, 'contentMD5': '0e5a3be60140bfafd929eb1bc5077785'}}, 'msgIds': ['U_0a7723b5-165a-45d6-9c35-0c6ed57ef6b7', '1625831973265657856', 'U_ed77756d-5916-47f0-8315-448cdb8d8f61', 'U_783c46e6-48da-46b5-8642-82f512b83d16', 'U_0ff02f35-53dd-46c5-8694-eb86a7040ce2'], 'userMsgIds': None, 'servicerMsgIds': ['U_ed77756d-5916-47f0-8315-448cdb8d8f61', 'U_783c46e6-48da-46b5-8642-82f512b83d16'], 'inputData': {'placeholder': '请尽量详细描述，充分利用机会', 'status': 1, 'optionsKey': 'entities.zhusu', 'aiParams': {'intent': 'zhusu', 'entities': {'zhusu': None}}}, 'chatData': {'qid': '2218239579335820', 'sessionId': '2218239579335820', 'chatType': 'zhuSu', 'chatId': '0', 'expertId': 1208976, 'provCode': '110000', 'cityCode': '110100'}}}
# print(type(aa))
if aa['applid'] != ww['applid']:
  print("PASS")
else:
  print("FAil")


if __name__=="__main__":

  # print(json.dumps(deepdiff.DeepDiff(ww,aa,exclude_paths={"root['data']"}),indent=6))
  print(deepdiff.DeepDiff(ww, aa,view='tree'))
