# -*- coding: utf-8 -*-

import pandas as pds
import re

from util.str_h import remove_html

def main():

    df = pds.read_csv('data/word/components.csv', encoding='utf-8')
    #regex = re.compile('<span\s+[^\>]+><font\s+[^\>]+>([^(span)|(font)]+)<\/font><\/span>', re.I)

    result = list()

    for index, row in df.iterrows():
        result.append(remove_html(row[0]))

    pds.DataFrame(data={'name': list(result)}).to_csv('data/word/components_handle.csv', index=False, encoding="utf-8")

def word():
    df = pds.read_csv('data/word/components_handle.csv', encoding='utf-8')

    regex = re.compile(u'(本品)?.?主要成[分|份](及其化学名称)?为?[：|:]?([\u4e00-\u9fa5]+)')
    regex_1 = re.compile(u'本品化学名称为[：:]?([\u4e00-\u9fa5]+)')

    re_step = re.compile(u'，|,|、|\s+|:|：|\t|。')

    re_num = re.compile(u'[\d.]{1,3}g|(毫克)|克|(ml)|(mg)')

    re_num_l = re.compile(u'[\d.]{1,3}$')

    #regex = re.compile(u'本品.?主要成分为：([^\s]+)')

    result = set()

    flag = set()

    for index, row in df.iterrows():
        m = re.search(regex, row[0])
        m_1 = re.search(regex_1, row[0])
        #print m
        if m:
            #print m.group(1)
            result.add(m.group(3))
        elif m_1:
            result.add(m_1.group(1))
        else:
            #pass
            print row[0]
            ls = re.split(re_step, row[0])
            print ';'.join(ls)
            ls = [re.sub(re_num, '', x) for x in ls]
            print ';'.join(ls)
            ls = [re.sub(re_num_l, '', x) for x in ls]
            flag = flag | set(ls)
            print '----->'

    print len(result)
    print len(flag)
    print ';'.join(flag)

    #pds.DataFrame(data={'name': list(result)}).to_csv('data/word/components_word.csv', index=False, encoding="utf-8")
    pds.DataFrame(data={'name': list(flag)}).to_csv('data/word/components_word_other.csv', index=False, encoding="utf-8")

def clean():

    df = pds.read_csv('data/word/components_word_other.csv', encoding='utf-8')

    regex = re.compile(u'本品[为含系]')
    regex_num = re.compile(u'(\d+.?)|等$')

    fill = re.compile(u'^([\u4e00-\u9fa5]{2,5})([(（][\u4e00-\u9fa5]+[）)])?$')

    result = set()

    for index, row in df.iterrows():

        if type(row[0]) is unicode:
            #m = re.search(regex, row[0])

            #if m:
            l = re.sub(regex, '', row[0])
            l = re.sub(regex_num, '', row[0])
            m = re.search(fill, l)

            if m:
                result.add(m.group(1))
                print m.group(0)
                print m.group(1)
                print '-------->'

            #else:
                #l = re.sub(regex_num, '', row[0])
            #print l


    print len(result)
    pds.DataFrame(data={'name': list(result)}).to_csv('data/word/components_word_chinese.csv', index=False, encoding="utf-8")
    #print ';'.join(result)


if __name__ == '__main__':
    #main()
    #word()
    clean()
