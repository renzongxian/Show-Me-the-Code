# -*- coding: cp936 -*-
import random
#����200�鳤��Ϊ8���Ż��룬�ֵ伯�����ּ���ĸ
def generate_key(number=200,length=8):
    char_set="abcdefghijklmnopqrstuvwxyz0123456789"
    result=""
    for i in range(0, number):
        temp=""
        while(temp==""):
            for j in range(0,length):
                temp=temp+char_set[random.randint(0,35)]
#�ж������ɵ��Ż����Ƿ���֮ǰ���ظ�
            if(result.find(temp)==-1):
                result=result+"%d  "%(i+1)+temp
            else:
                temp=""      
        result=result+'\n'
    return result
def file_write():
    fp=open("result.txt",'w')
    fp.writelines(generate_key())
    fp.close()
if __name__ == '__main__':
	file_write()
