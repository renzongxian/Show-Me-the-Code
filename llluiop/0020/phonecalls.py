#!/usr/bin/env python
#-*- coding: utf-8-*-


import xlrd


def phone_calls(file_path):
    xls = xlrd.open_workbook(file_path)
    sheet = xls.sheet_by_index(0)

    minutes = 0
    seconds = 0

    for i in range(1, sheet.nrows):
        call = str(sheet.row_values(i)[3].encode("gb2312"))
        if "��" in call:
            minute, second_phrase = call.split("��")
        else:
            minute = 0
            second_phrase = call

        second, tmp = second_phrase.split("��")

        minutes += int(minute)
        seconds += int(second)

    return minutes, seconds



if __name__ == '__main__':
    minutes, seconds = phone_calls("2015��05������ͨ��.xls")

    minutes += seconds / 60
    seconds = seconds % 60
    print "ͨ��ʱ���ܼƣ�", minutes, "��", seconds, "��"





