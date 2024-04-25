import re
import math
class Solve_Pattern:
    def __init__(self):
        self.path = ""
        self.Passage_Couple = {}
        self.Sentence_Couple = {}
        self.Num_English_Vocubulary = 0
        self.Num_Chinese_Vocubulary = 0
        self.Num_English_bit = 0
        self.Num_Chinese_bit = 0
        self.R_Average = 0

    def Deal(self,path):
        self.path = path
        self.Split_Article_Into_List(self.path)
        self.Passage_Layout()
        self.Split_Passage()
        #self.Split_Sentence()

    def Split_Article_Into_List(self,path):
        Chinese = re.compile(u'[\u4e00-\u9fa5]')
        #English = re.compile(u'[a-zA-Z]{1} [a-zA-Z]{2}')
        English = re.compile(u'[a-zA-Z]')
        Passage1 = []
        Passage2 = []
        Passage3 = []
        str1 = ""

        Re_Space_Line = re.compile("\s*\n")
        with open(path,'r',encoding='utf-8') as f1:
             #f.encoding = 'utf-8'
             iter_f = iter(f1)
             #for line in iter_f:
                 # Passage1.append(line)
                 # print(line)
        # print(Passage1)
             for line in iter_f:
                  if not Re_Space_Line.match(line):                    #line未匹配到0个或多个空格符和\n
                       Passage1.append(line)
             for item in range(0,len(Passage1)-1):                                    #将同为英文或中文的列表元素合并为一个元素
                 str1 = str1 + str(Passage1[item])
                 if English.search(Passage1[item]) and Chinese.search(Passage1[item+1]) and not Chinese.search(Passage1[item]):
                      Passage2.append(str1)
                      str1 = ""
                 if Chinese.search(Passage1[item]) and English.search(Passage1[item+1]) and not Chinese.search(Passage1[item+1]):
                      Passage3.append(str1)
                      str1 = ""

             self.Passage_Couple = dict(zip(Passage2,Passage3))
             self.R_Average = self.Get_R_Average()
    def Get_R_Average(self):
        r = 0
        for item in self.Passage_Couple.keys():
            r = self.Calculation(item, self.Passage_Couple[item]) + r
        if len(self.Passage_Couple) != 0:
            R_Average = r / len(self.Passage_Couple)

        return R_Average

    def Calculation(self,Current_English_Sentence,Current_Chinese_Sentence):
        i = ['E_V','E_B','C_Z','C_B']
        D_i = dict.fromkeys(i,0)
        for item in Current_English_Sentence:
            if item.isalpha():
                D_i['E_B'] += 1
            elif item.isspace():
                D_i['E_V'] += 1
        for item in Current_Chinese_Sentence:
            if u'\u4e00'<=item<=u'\u9fff':
                D_i['C_Z'] += 1
        D_i['C_B'] = D_i['C_Z']*2
        self.Num_English_Vocubulary = D_i['E_V']          #等于句子中的空格数
        self.Num_Chinese_Vocubulary = D_i['C_Z']
        self.Num_English_bit = D_i['E_B']                 #等于字母数
        self.Num_Chinese_bit = D_i['C_B']

        if self.Num_Chinese_Vocubulary == 0 or self.Num_Chinese_bit == 0:
            r = 10000
        elif self.Num_English_Vocubulary == 0 or self.Num_English_bit == 0:
            r = 0
        elif self.Num_Chinese_Vocubulary!=0 and self.Num_Chinese_bit!=0 and self.Num_English_Vocubulary!=0 and self.Num_English_bit!=0:
            r = (self.Num_English_Vocubulary / self.Num_Chinese_Vocubulary) + (self.Num_English_bit / self.Num_Chinese_bit)
        return r

    def Get_P(self,r):

        p = (r - self.R_Average) / self.R_Average
        return p

    def Passage_Layout(self):
        English_Passage_List_U = []
        Chinese_Passage_List_U = []

        English_Passage_List_O = list(self.Passage_Couple.keys())
        for passage in English_Passage_List_O:
            re.sub(r'\?', '\.', passage)
            re.sub(r'!', '\.', passage)
            re.sub(r'!', '\.', passage)
            #re.sub(r',', '\.', passage)
            re.sub(r'(\.)+', '\.', passage)
            re.sub(r'”', '\"', passage)
            re.sub(r'“', '\"', passage)
            re.sub(r'’', '\'', passage)
            re.sub(r'‘', '\'', passage)
            re.sub(r'，', ',', passage)
            re.sub(r'．', '\.', passage)
            re.sub(r';', '\.', passage)
            English_Passage_List_U.append(passage)
        Chinese_Passage_List_O = list(self.Passage_Couple.values())
        for passage in Chinese_Passage_List_O:
            re.sub(r'？', '。', passage)
            re.sub(r'！', '。', passage)
            #re.sub(r'，', '。', passage)
            re.sub(r'(…)+', '。', passage)
            Chinese_Passage_List_U.append(passage)
        self.Passage_Couple = dict(zip(English_Passage_List_U, Chinese_Passage_List_U))



    def Split_Passage(self):

        for Article in self.Passage_Couple.keys():
            EL = []
            CL = []
            Current_English_Passage_list = re.split(r'\n',str(Article))
            Current_Chinese_Passage_list = re.split(r'\n', str(self.Passage_Couple[Article]))
            Current_Passage_Couple = dict(zip(Current_English_Passage_list,Current_Chinese_Passage_list))
            self.Split_Sentence(Current_Passage_Couple)

    def Split_Sentence(self,Current_Passage_Couple):
        English_Sentence_List = []
        Chinese_Sentence_List = []
        for Sentence in Current_Passage_Couple.keys():

            Sentence1 = re.sub(r'Mr.','',Sentence)
            Sentence2 = re.sub(r'Miss.','',Sentence1)
            English_Current_Sentence_List = re.split(r'\.\n|\. |\.\"\n|\.\"|\n|\.\"|\.\'|\. \' ', str(Sentence2))
            Chinese_Current_Sentence_List = re.split(r'。\n|。|。”\n|。”|\n|。”|， “ ', str(Current_Passage_Couple[Sentence]))
            if len(English_Current_Sentence_List) == len(Chinese_Current_Sentence_List) and English_Current_Sentence_List[0] !='' and Chinese_Current_Sentence_List[0] !='':
                self.Sentence_Couple.update(dict(zip(English_Current_Sentence_List, Chinese_Current_Sentence_List)))
            else:
                self.Grammer(English_Current_Sentence_List,Chinese_Current_Sentence_List)

    def Grammer(self,English_Current_Sentence_List,Chinese_Current_Sentence_List):
        Long_E = len(English_Current_Sentence_List)
        Long_C = len(Chinese_Current_Sentence_List)
        English_item = 0
        Chinese_item = 0

        if len(English_Current_Sentence_List)>=2 and len(Chinese_Current_Sentence_List)>=2:
          while(English_item<=len(English_Current_Sentence_List)-2 and Chinese_item<=len(Chinese_Current_Sentence_List)-2):

            Current_English_Sentence = str(English_Current_Sentence_List[English_item])
            Current_Chinese_Sentence = str(Chinese_Current_Sentence_List[Chinese_item])
            if Long_E != Long_C:
               while(True):
                  r0 = self.Calculation(str(Current_English_Sentence), str(Current_Chinese_Sentence))
                  p0 = self.Get_P(r0)
                  if p0<=0:
                      if English_item <=len(English_Current_Sentence_List)-2:
                         Current_English_Sentence = Current_English_Sentence + ' '+str(English_Current_Sentence_List[English_item+1])
                  else:
                      if Chinese_item <=len(Chinese_Current_Sentence_List)-2:
                         Current_Chinese_Sentence = Current_Chinese_Sentence + ' '+str(Chinese_Current_Sentence_List[Chinese_item+1])
                  r1 = self.Calculation(str(Current_English_Sentence), str(Current_Chinese_Sentence))
                  p1 = self.Get_P(r1)
                  if math.fabs(p0)<=math.fabs(p1):
                       if p0<=0:
                           if English_item <= len(English_Current_Sentence_List) - 2:
                              Current_English_Sentence = str(Current_English_Sentence).rstrip(str(English_Current_Sentence_List[English_item+1]))

                       else:
                           if Chinese_item <= len(Chinese_Current_Sentence_List) - 2:
                              Current_Chinese_Sentence = str(Current_Chinese_Sentence).rstrip(str(Chinese_Current_Sentence_List[Chinese_item+1])) #
                       self.Sentence_Couple.update({str(Current_English_Sentence):str(Current_Chinese_Sentence)})

                  #self.Sentence_Couple[str(Current_English_Sentence)] = str(Current_Chinese_Sentence)
                       English_item = English_item+1
                       Chinese_item = Chinese_item+1
                       break
                  else:
                       if p0<=0:
                            English_item = English_item+1
                            Long_E = Long_E - 1
                       else:
                            Chinese_item = Chinese_item+1
                            Long_C = Long_C - 1
                  #思考English_item和Chinese_item的值应该加多少
                       continue
            else:
                Q = []
                W = []
                for i in English_Current_Sentence_List:
                    if English_Current_Sentence_List.index(i)>=English_item:
                        Q.append(i)
                for j in Chinese_Current_Sentence_List:
                    if Chinese_Current_Sentence_List.index(j)>=Chinese_item:
                        W.append(j)
                self.Sentence_Couple.update(dict(zip(Q,W)))
                English_item = len(English_Current_Sentence_List)-1
                Chinese_item = len(Chinese_Current_Sentence_List)-1
                break




        #用标点符号更精确的划分句子为最小的单位，得到Sentence_Couple之后采用算法对句子进行适当的合并

if __name__ == '__main__':
    S = Solve_Pattern()
    path = 'D:\\pycharmfile\\University-Design\\English-Chinese Resource2\\Article9+.txt'
    S.Deal(path)
    # EL = []
    # CL = []
    # for item in S.Sentence_Couple.keys():
    #
    #     EL.append(str(item).replace(u'\u3000\u3000',u''))
    #     CL.append(S.Sentence_Couple[item])
    #     #print(item)
    # SC = dict(zip(EL,CL))


    for i in S.Sentence_Couple.keys():
        print(i)
        print(S.Sentence_Couple[i])