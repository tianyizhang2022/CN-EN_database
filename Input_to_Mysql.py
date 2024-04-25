import pymysql
import Pattern_Convert


class Database:
   def __init__(self,num):
        self.var = ''
        self.sql = ''
        self.num = num
        self.db = self.Login(self.num)
        self.cursor = self.Get_cursor()

   def Login(self,num):
       if num == 1:  # 管理员身份登录
          db = pymysql.Connect(host="localhost", user="Administrator", password="Abc_123456", database="english-chinese")
       if num == 2:
          db = pymysql.Connect(host="localhost", user="USER", password="Abc_123456", database="english-chinese")
       return db
   def Get_cursor(self):
       cursor = self.db.cursor()
       return cursor

   def Insert_Data(self,Language_Couple):
         for key in Language_Couple.keys():
            sql = "insert into testtable (english,chinese) values(%s,%s);"
            english = str(key)
            chinese = str(Language_Couple[key])
            self.var = (english,chinese)
            self.cursor.execute(sql,self.var)
            self.db.commit()


   def Find_Data_by_Index(self,a,b):
       list = []
       for index in range(a,b+1):
             sql = "select * from testtable where id={ID};".format(ID = index)
             self.cursor.execute(sql)
             list.append(self.cursor.fetchall())
             self.db.commit()
       return list

   def Find_Data_by_English_Vocabulary(self,Vocabulary):
       list = []
       sql = "select * from testtable where english like '%{word}%';".format(word = Vocabulary)
       self.cursor.execute(sql)
       list.extend(self.cursor.fetchall())
       self.db.commit()
       return list

   def Find_Data_by_Chinese_Vocabulary(self,Vocabulary):
       list = []
       sql = "select * from testtable where chinese like '%{word}%';".format(word=Vocabulary)
       self.cursor.execute(sql)
       list.extend(self.cursor.fetchall())
       self.db.commit()
       return list

   def Alter_Sentence(self,id,English,Chinese):
       sql = "update testtable set english='{E}',chinese='{C}' where id={ID};".format(ID=id,E=English,C=Chinese)
       self.cursor.execute(sql)
       self.db.commit()
   def Export(self,num,file_path):
       if num == 1:
           self.sql = "select * from testtable into outfile '{A}'".format(A = file_path+'/file0.txt')
       if num == 2:
           self.sql = "select * from testtable into outfile '{A}'".format(A = file_path+'/file_0.csv')
       if num == 3:
           self.sql = "mysqldump -u root -p english-chinese testtable>{A}".format(A = file_path+'/file_0.sql')
        # C:\ProgramData\MySQL\MySQL Server 8.0\Uploads
       self.cursor.execute(self.sql)
       self.db.commit()


   def CLose(self):
       self.db.close()
       self.cursor.close()
