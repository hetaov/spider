# -*- coding: utf-8 -*-

import re
#from util.str_h import remove_special_character

regex_1 = re.compile(u'（')
regex_2 = re.compile(u'）')
regex_3 = re.compile(u'　')
regex_4 = re.compile(u'\r|\n')

regex_l = re.compile(u'[,，。]?分子量：([\d.]{1,5})[。]?')
regex = re.compile(u'，?本品为无?色(或黄色)?(或微黄色)?的澄明液体[。]?')
regex_n = re.compile(u'，?无[。]?')

def remove_all_html(s):
    regex_1 = re.compile(u'<[\w:]{1,8}\s+[^>]*>')
    regex_2 = re.compile(u'<\/[\w:]{1,8}\s*>')
    regex_3 = re.compile(u'<[\w:]{1,8}\s+[^>]*/>')
    regex_4 = re.compile(u'　')
    regex_5 = re.compile(u'\r|\n')
    regex_6 = re.compile(u'\??\/\w{1,5}[>(\&gt;)]')
    regex_7 = re.compile(u'<[\w:]{1,8}\s+[^>]*$')

    s = re.sub(regex_5, '', s)
    s = re.sub(regex_4, '', s)
    s = re.sub(regex_1, '', s)
    s = re.sub(regex_2, '', s)
    s = re.sub(regex_3, '', s)
    s = re.sub(regex_6, ',', s)
    s = re.sub(regex_7, '', s)
    s = re.sub(u'"', '\\"', s)
    return s

def remove_html(s):
    regex = re.compile('<span\s+[^\>]+><font\s+[^\>]+>([^(span)|(font)]+)<\/font><\/span>', re.I)
    m = re.search(regex, s)

    if m:
        return re.sub(regex, m.group(1), s)

    return s

def remove_special_character(s):

    flag = re.sub(regex_1, '(', s)
    flag = re.sub(regex_2, ')', flag)
    flag = re.sub(regex_3, ' ', flag)
    flag = re.sub(regex_4, '', flag)

    return flag

def format_formula(s):

    flag = re.sub(regex_l, '', s)

    if re.search('^[\d.]{1,7}\s*$', flag):
        flag = re.sub('^[\d.]{1,7}\s*$', '', flag)

    flag = re.sub(regex, '', flag)
    flag = re.sub(regex_n, '', flag)
    flag = remove_special_character(flag)
    flag = re.sub(',|，$', '', flag)

    return flag
