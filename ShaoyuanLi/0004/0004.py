# -*- coding: cp936 -*-
import re
fin=open("example.txt","r")
fout=open("result.txt","w")
str=fin.read()
#ƥ��������ʽ
reObj=re.compile("\b?([a-zA-Z]+)\b?")
words=reObj.findall(str)
#�������ֵ�
word_dict={}
#�Ե��ʵ�Сд��Ϊ��ֵ����ͳ�ƣ�ͬʱҪ
for word in words:
    if(word_dict.has_key(word)):
        word_dict[word.lower()]=max(word_dict[word.lower()],words.count(word.lower())+words.count(word.upper())+words.count(word))
    else:
        word_dict[word.lower()]=max(0,words.count(word.lower())+words.count(word.upper())+words.count(word))       
for(word,number) in word_dict.items():
    fout.write(word+":%d\n"%number)
    
