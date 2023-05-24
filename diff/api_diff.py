#*- coding: UTF-8 -*-


import logging
import sys
from typing import Any, Dict, Tuple, Union, List

logging.basicConfig(level=logging.INFO)


def data_equal_compare(A, B):
    """
    表达式: ==  含义: A等于B
    :param A:
    :param B:
    :return:
    """
    print(sys._getframe().f_code.co_name , "A:", A , "B:", B)
    if isinstance(A, str) or isinstance(B, str):
        if str(A) == str(B):
            return True
        return False
    elif A == B:
        return True
    return False

def data_bigger_compare(A, B):
    """
    表达式: > 含义: A大于B
    :param A:
    :param B:
    :return:
    """
    print(sys._getframe().f_code.co_name)
    if isinstance(A, str) or isinstance(B, str):
        if int(A) > int(B):
            return True
        return False
    if A > B:
        return True
    return False

def data_noless_compare(A, B):
    """
    表达式: >= 含义: A不小于B
    :param A:
    :param B:
    :return:
    """
    print(sys._getframe().f_code.co_name)
    if isinstance(A, str) or isinstance(B, str):
        if int(A) >= int(B):
            return True
        return False
    if A >= B:
        return True
    return False

def data_less_compare(A, B):
    """
    表达式: <  含义: A小于B
    :param A:
    :param B:
    :return:
    """
    print(sys._getframe().f_code.co_name)
    if isinstance(A, str) or isinstance(B, str):
        if int(A) < int(B):
            return True
        return False
    if A < B:
        return True
    return False

def data_nobigger_compare(A, B):
    """
    表达式: <= 含义: A不大于B
    :param A:
    :param B:
    :return:
    """
    print(sys._getframe().f_code.co_name)
    if isinstance(A, str) or isinstance(B, str):
        if int(A) <= int(B):
            return True
        return False
    if A <= B:
        return True
    return False

def data_type_compare(A, B):
    """
    :param A:
    :param B:
    :return: True 代表类型相同; False 代表类型不同
    """
    print(sys._getframe().f_code.co_name)
    if isinstance(A, str) and isinstance(B, str):
        return True
    elif isinstance(A, int) and isinstance(B, int):
        return True
    elif isinstance(A, dict) and isinstance(B, dict):
        return True
    elif isinstance(A, list) and isinstance(B, list):
        return True
    elif isinstance(A, tuple) and isinstance(B, tuple):
        return True
    return False

def data_len_compare(A, B):
    """
    支持 字符串 字典 列表
    :param A:
    :param B:
    :return:
    """
    print(sys._getframe().f_code.co_name)
    if len(A) == len(B):
        return True
    return False


def data_mapping_compare(A, B, maping_rule):
    """
    :param A:
    :param B:
    :param maping_rule 取值可以是1个元组也可以是多个
    例子参考: [("1", "115,116"), (2, [215, 216]), ([315, 316], 3),([412, 413],[456,457]), ("aaa", "bbb,ccc")]
    :return:
    """
    print(sys._getframe().f_code.co_name)
    for item in maping_rule:
        first_item, secode_item = item
        if isinstance(first_item, list) and not isinstance(secode_item, list):
            if A in first_item and B == secode_item:
                return True
        elif not isinstance(first_item, list) and isinstance(secode_item, list):
            if A == first_item and B in secode_item:
                return True
        elif isinstance(first_item, str) and "," in first_item and \
                isinstance(secode_item, str) and "," not in secode_item :
            if A in first_item.split(",") and B == secode_item:
                return True
        elif isinstance(first_item, str) and not "," in first_item and \
                isinstance(secode_item, str) and "," in secode_item:
            if A == first_item and B in secode_item.split(","):
                return True
        elif isinstance(first_item, list) and isinstance(secode_item, list):
            if A in first_item and B in secode_item:
                return True
        elif isinstance(first_item, str) and "," in first_item and \
                isinstance(secode_item, str) and "," in secode_item:
            if A in first_item.split(",") and B in secode_item.split(","):
                return True
        elif isinstance(first_item, int)  and isinstance(secode_item, int):
            if A == first_item and B == secode_item:
                return True
        elif isinstance(first_item, int)  and isinstance(secode_item, list):
            if A == first_item and B in secode_item:
                return True
    return False


def data_numb_value_compare(A, B):
    """
    :param A:intstr  or int
    :param B:intstr or int
    :param maping_rule: mapping_rule[("1","215,216")]
    :return:
    """
    print(sys._getframe().f_code.co_name)
    if isinstance(A, float) or isinstance(B, float):
        if float(A) == float(B):
            return True
    elif isinstance(A, str) and "." in A:
        if float(A) == float(B):
            return True
    elif isinstance(B, str) and "." in B:
        if float(A) == float(B):
            return True
    elif int(A) == int(B):
        return True
    """
    try:
        if isinstance(A, float) or isinstance(B, float):
            if float(A) == float(B):
                return True
        if isinstance(A, str) and "." in A:
            if float(A) == float(B):
                return True
        if isinstance(B, str) and "." in B:
            if float(A) == float(B):
                return True
        if int(A) == int(B):
            return True
    except Exception as e:
        logging.error(f"data_numb_vaule_compare:{e}")
        return False
    """
    return False


def data_json_key_equal_compare(A: Dict[str, Any], B: Dict[str, Any]):
    """
    @description: 断言两个json的key是否完全一致
    @param {*}
    @return {*}
    """
    if isinstance(A, Dict) and isinstance(B, Dict):
        for key_A in A:
            if key_A not in B:
                logging.error(f"{key_A} : {A[key_A]} not in Dict \n {B}")
                return False
            # 递归遍历
            if isinstance(A[key_A], Dict) or isinstance(A[key_A], List):
                return data_json_key_equal_compare(A[key_A], B[key_A])

    elif isinstance(A, List) and isinstance(B, List):
        for index in range(len(A)):
            # 递归遍历
            if isinstance(A[index], Dict) or isinstance(A[index], List):
                ret = data_json_key_equal_compare(A[index], B[index])
                if ret is False:
                    return False

            elif A[index] not in B:
                print(f"{A[index]} not in List B")
                return False
    else:
        return True

    return True


def data_json_key_and_value_type_equal_compare(A, B):
    """
    @description: Json的key 相同并且 value 类型是否一致
    @param {*}
    @return {*}
    """

    if isinstance(A, Dict) and isinstance(B, Dict):
        for key_A in A:
            if key_A not in B:
                logging.error(f"{key_A} no in {B}")
                return False

            if type(A[key_A]) != type(B[key_A]):
                logging.error(f"{key_A}:{A[key_A]} type != {key_A}:{B[key_A]} type")
                return False
            # 递归遍历
            if isinstance(A[key_A], Dict) or isinstance(A[key_A], List):
                return data_json_key_and_value_type_equal_compare(A[key_A], B[key_A])

    elif isinstance(A, List) and isinstance(B, List):
        for index in range(len(A)):
            # 递归遍历
            if isinstance(A[index], Dict) or isinstance(A[index], List):
                ret = data_json_key_and_value_type_equal_compare(A[index], B[index])
                if ret is False:
                    return False

            elif type(A[index]) != type(B[index]):
                logging.error(f"{key_A}:{A[key_A]} type != {key_A}:{B[key_A]} type")
                return False
    else:
        return True

    return True


def data_json_equal_compare(A, B):
    """
    @description: 这个断言是assertDictValueType进一步延伸，最严格校验
    @param {*}
    @return {*}
    """
    if isinstance(A, Dict) and isinstance(B, Dict):
        for key_A in A:
            if key_A not in B:
                logging.error(f"{key_A} not in dict \n  {B}")
                return False

            # 递归遍历
            if isinstance(A[key_A], Dict) or isinstance(A[key_A], List):
                return data_json_equal_compare(A[key_A], B[key_A])

            if A[key_A] != B[key_A]:
                logging.error(f"{key_A}:{A[key_A]} != {key_A}:{B[key_A]}")
                return False

    elif isinstance(A, List) and isinstance(B, List):
        for index in range(len(A)):
            # 递归遍历
            if isinstance(A[index], Dict) or isinstance(A[index], List):
                ret = data_json_equal_compare(A[index], B[index])
                if ret is False:
                    return False

            elif A[index] not in B:
                logging.error(f"{key_A} not in dict  \n {B}")
                return False
    else:
        return True

    return True

def table_key_exist_compare(A, B, key_name_list):
    """
    :param A:intstr  or int
    :param B:intstr or int
    :param maping_rule: mapping_rule[("1","215,216")]
    :return:
    """
    print(sys._getframe().f_code.co_name)

    if isinstance(A, list) and isinstance(B, list):
        data_a = {}
        data_b = {}
        for item in key_name_list:
            for indexA in range(len(A)):
                if item not in data_a:
                    data_a[item] = set([A[indexA][item]])
                else:
                    data_a[item] = set([A[indexA][item]]) | data_a[item]

            for indexB in range(len(B)):
                if item not in data_b:
                    data_b[item] = set([B[indexB][item]])
                else:
                    data_b[item] = set([B[indexB][item]]) | data_b[item]

            only_in_A = data_a[item] - data_b[item]
            if len(only_in_A) > 0:
                logging.error(f"{item}:{only_in_A} not in B {item}:{data_b[item]}")

            only_in_B = data_b[item] - data_a[item]
            if len(only_in_B) > 0:
                logging.error(f"{item}:{only_in_B} not in A {item}:{data_a[item]}")

            if len(only_in_A) >0 or len(only_in_B):
                return False

        return True

    if isinstance(A, dict) and isinstance(B, dict):
        for item in key_name_list:
            if item not in A:
                logging.error(f"{item} not in dict  \n {A}")
                return False
            elif item not in B:
                logging.error(f"{item} not in dict  \n {B}")
                return False
            elif A[item] != B[item]:
                logging.error(f"{item}:{A[itme]} != {item}:{B[itme]} ")
                return False
        return True

    return True

operators = {
    "==": data_equal_compare,
    ">": data_bigger_compare,
    ">=": data_noless_compare,
    "<": data_less_compare,
    "<=": data_nobigger_compare,
    "type_cmp": data_type_compare,
    "len_cmp": data_len_compare,
    "mapping_cmp": data_mapping_compare,
    "numb_equal": data_numb_value_compare,
    "json_key_equal": data_json_key_equal_compare,
    "json_k_v_type_equal": data_json_key_and_value_type_equal_compare,
    "json_equal": data_json_equal_compare,
    "table_key_exist": table_key_exist_compare,
    }

def get_left_value(steps, value):
    """
    :param steps:左移的位数
    :param value:要被左移数
    :return:value左移steps的结果 int 64位的结果
    """
    if value > 18446744073709551615:
        value = value & 18446744073709551615
    return value << steps

def get_right_value(steps, value):
    """
    :param steps:右移的位数
    :param value:要被右移数
    :return:value右移steps的结果 int 64位的结果
    """
    if value > 18446744073709551615:
        value = value & 18446744073709551615
    return value >> steps

def EncrypQid(id, key):
    """
    参数的含义：id = qid  key=uid 返回int64的加密后的qid
    id: 1234567  key: 757177820  加密qid: 2044719760670720
    id: 78675423  key: 757177820 加密qid: 1952424470396928
    id: 166237807358  key: 757177820 加密qid: 1547175319978003
    """
    if id <= 0:
        return 0
    if key < 32:
        key = 13466169
    cov = get_left_value(11, 1) - 1
    p0 = get_left_value(50, 1)
    p1 = get_left_value(39, id & cov)
    p2 = get_left_value(37, 3 & get_right_value(4, key))
    p3 = get_left_value(26, cov & get_right_value(11, id))
    p4 = get_left_value(24, 3 & get_right_value(2, key))
    p5 = get_left_value(13, cov & get_right_value(22, id))
    p6 = get_left_value(1, 3 & key)
    p7 = cov & get_right_value(33, id)

    ret = p0 | p1 | p2 | p3 | p4 | p5 | p6 | p7
    #print(cov, p0, p1, p2, p3, p4, p5, p6, p7)
    return ret


def DecryptQid(eid, key):
    """Decryption qid解密函数 返回int64的解密后的qid，eid=加密后的qid  key=uid
    加密qid: 2044719760670720 key: 757177820 id: 1234567
    加密qid: 1952424470396928 key: 757177820 id: 78675423
    加密qid: 1547175319978003 key: 757177820 id: 166237807358
    """
    if eid <= 1125899906842624 :
        return eid, false

    if key == 0 :
        key = 13466169
    cov = get_left_value(11, 1) - 1

    p0  = get_left_value(33, eid & cov)
    p1  = get_right_value(11, eid)  & 3
    p2  = get_left_value(22, get_right_value(13, eid) & cov )
    p3  = get_left_value(2, get_right_value(24, eid) & 3 )
    p4  = get_left_value(11, get_right_value(26, eid) & cov )
    p5  = get_left_value(4, get_right_value(37, eid) & 3 )
    p6  = get_right_value(39,eid) & cov
    skey = p1 | p3 | p5
    if (skey ^ (key & 63)) != 0 :
        return p0 | p2 | p4 | p6

    return p0 | p2 | p4 | p6

if __name__ == "__main__":
    pass