import re
import os

def FileDeal_Del(path):
    file = 'D:/pycharmfile/University-Design/English-Chinese Resource1/Article'
    DelWord1 = re.compile("可可英语")
    DelWord2 = re.compile("=")
    DelWord3 = re.compile("{")
    DelWord4 = re.compile("}")
    with open(path,'r',encoding='utf-8') as f1:
        #f.encoding = 'utf-8'
        iter_f = iter(f1)
        with open(file, 'a', encoding='utf-8') as file_obj:
            for line in iter_f:
                if (DelWord1.search(line) or DelWord2.search(line) or DelWord3.search(line) or DelWord4.search(line)):
                    print(DelWord3.search(line))
                else:
                    file_obj.write(line)

    #有“可可英语”的删除，有“=”的删除，有“{”或“}”的删除

def Del_Space(path):
    file = 'D:/pycharmfile/University-Design/English-Chinese Resource1/Article9'
    Space = re.compile("可可原创")
    with open(path,'r',encoding='utf-8') as f1:
        #f.encoding = 'utf-8'
        iter_f = iter(f1)
        with open(file, 'a', encoding='utf-8') as file_obj:
            for line in iter_f:
                if Space.search(line):
                    print(1)
                else:
                    file_obj.write(line)

def Split_Passage(path):
    Passage = []
    Chinese = re.compile(u'[\u4e00-\u9fa5]')
    English = re.compile(u'[a-zA-Z]{4}')
    file = 'D:/pycharmfile/University-Design/English-Chinese Resource2/Article14+'
    with open(path, 'r', encoding='utf-8') as f1:
        # f.encoding = 'utf-8'
        iter_f = iter(f1)
        for line in iter_f:
            Passage.append(line)
        with open(file, 'a', encoding='utf-8') as file_obj:
            for line in range(0,len(Passage)):
                if English.search(Passage[line]) and Chinese.search(Passage[line+1]):
                    file_obj.write(Passage[line])
                    file_obj.write('----------||||||||'+'\n')

                else:
                    file_obj.write(Passage[line])



if __name__ == '__main__':
    #整理格式
    #path = "D:/pycharmfile/university-Design/English-Chinese Resource1"
    #files = os.listdir(path)
    #for item in files:
     #   FileDeal_Del("D:/pycharmfile/university-Design/English-Chinese Resource1/"+item)
     #删除换行
     #path = "D:/pycharmfile/university-Design/English-Chinese Resource1/Article8.txt"
     #Del_Space(path)
     #中英文分行
     path = "D:/pycharmfile/university-Design/English-Chinese Resource2/Article14.txt"
     Split_Passage(path)

