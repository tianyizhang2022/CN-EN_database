from tkinter import *
from tkinter.ttk import Separator
import tkinter.filedialog
import tkinter.messagebox
import Pattern_Convert
import Input_to_Mysql
import pymysql
import Connect_Pyspider
class A:
    def __init__(self,var):
        self.var = var
        self.TestDatabase = Input_to_Mysql.Database(self.var)
        self.Down_Article = Connect_Pyspider.Connected_Pyspider()
        self.__root = Tk()
        self.path0 = StringVar()  # 爬虫网址
        self.path1 = StringVar()  # 从数据库导出文件的路径
        self.path2 = StringVar()  # 做对齐处理时输入的TXT路径
        self.var1 = IntVar()
        self.var1.set(1)
        self.__root.title('Demo2')
        self.__root.geometry('1200x600+50+50')
        self.__root.configure(bg = 'AliceBlue')
        self.__root.resizable(width = False,height = False)
        self.__frameUpper1 = Frame(self.__root, bg='AliceBlue')
        self.__frameUpper2 = Frame(self.__root, bg='AliceBlue')
        self.__frameUpper1_1 = Frame(self.__frameUpper1, bg='AliceBlue')
        self.__frameUpper1_2 = Frame(self.__frameUpper1, bg='AliceBlue')
        self.__frameUpper2_1 = Frame(self.__frameUpper2, bg='AliceBlue')
        self.__frameUpper2_2 = Frame(self.__frameUpper2, bg='AliceBlue')
        self.__frameUpper2_3 = Frame(self.__frameUpper2, bg='AliceBlue')
        self.__frameUpper2_4 = Frame(self.__frameUpper2, bg='AliceBlue')
        self.__frameUpper2_5 = Frame(self.__frameUpper2, bg='AliceBlue')
        self.__label1 = Label(self.__frameUpper1, text="输入网站地址")
        self.__entry1 = Entry(self.__frameUpper1, bd=10, textvariable=self.path0, width=60)
        self.__label2 = Label(self.__frameUpper1, text="工程名称")
        self.__entry2 = Entry(self.__frameUpper1, bd=10, width=60)
        self.__button1 = Button(self.__frameUpper1, text="下载文档", width=10,command = self.DownLoad)
        self.__label3 = Label(self.__frameUpper1, text="文件路径")
        self.__entry3 = Entry(self.__frameUpper1, bd=10, textvariable=self.path2, width=60)
        self.__button2 = Button(self.__frameUpper1, text="浏览", command=self.Scan_Path2, width=10)

        self.__button3 = Button(self.__frameUpper1_1, text="对齐处理", width=10,command = self.Match_Process)
        self.__button4 = Button(self.__frameUpper1_1, text="保存", width=10,pady = 10,command = self.Save_to_Mysql)
        self.__button9 = Button(self.__frameUpper1_1, text="清除", width=10, pady=10, command=self.Delete_Listbox1)
        self.__scrollbar1 = Scrollbar(self.__frameUpper1_2,orient = VERTICAL)
        self.__scrollbar2 = Scrollbar(self.__frameUpper1_2,orient = HORIZONTAL)
        self.__scrollbar3 = Scrollbar(self.__frameUpper2_3,orient = VERTICAL)
        self.__scrollbar4 = Scrollbar(self.__frameUpper2_3,orient = HORIZONTAL)
        self.__listbox1 = Listbox(self.__frameUpper1_2, width=60, heigh=20,exportselection = False)
        self.__button6 = Button(self.__frameUpper2_1, text="查询", width=10,command =self.Find_Data_by_Index)
        self.__label4 = Label(self.__frameUpper2_1, text="从",padx = 20)
        self.__label5 = Label(self.__frameUpper2_1, text="条 到")
        self.__label6 = Label(self.__frameUpper2_1, text="条")
        self.__entry4 = Entry(self.__frameUpper2_1, bd=10, width=10)
        self.__entry5 = Entry(self.__frameUpper2_1, bd=10, width=10)
        self.__listbox2 = Listbox(self.__frameUpper2_3, width=60, heigh=20, exportselection=False,selectmode = MULTIPLE)
        self.__entry6 = Entry(self.__frameUpper2_2, bd=10, textvariable=self.path1, width=40)
        self.__label7 = Label(self.__frameUpper2_2, text="导出文件路径")
        self.__button5 = Button(self.__frameUpper2_2, text="浏览", width=10,command=self.Scan_Path1)
        self.__button7 = Button(self.__frameUpper2_4, text="导出", width=10,command =self.Mysql_to_File)
        self.__button8 = Button(self.__frameUpper2_1, text="删除选中记录", width=10,command =self.Delete_Index)
        self.__label8 = Label(self.__frameUpper2_4, text="导出文件格式")
        self.__rbTXT = Radiobutton(self.__frameUpper2_4, text = "TXT",variable = self.var1,value=1)
        self.__rbCSV = Radiobutton(self.__frameUpper2_4, text="CSV", variable=self.var1, value=2)
        self.__entry7 = Entry(self.__frameUpper2_5, bd=10, width=40)
        self.__button10 = Button(self.__frameUpper2_5, text="查询", width=10, command=self.Find_Data_by_Vocabulary)
        self.__button11 = Button(self.__frameUpper2_5, text="浏览语料库", width=15,command=self.Revive_Database)
        self.Canvas_And_Button()

    def Get_var(self):
        return self.var
    def Scan_Path2(self):
        path1 = tkinter.filedialog.askopenfilename()
        self.path2.set(path1)

    def Scan_Path1(self):
        path1 = tkinter.filedialog.askdirectory()
        self.path1.set(path1)

    def Match_Process(self):
        global File1
        File1 = Pattern_Convert.Solve_Pattern()
        Path_to_Pattern_Convert = ''
        try:
          if self.__entry3.get() != "":
            Path_to_Pattern_Convert = self.__entry3.get()#装换为字符串类型
            File1.Deal(Path_to_Pattern_Convert)
            for item in File1.Sentence_Couple.keys():
                self.__listbox1.insert(END,item)
                self.__listbox1.insert(END,File1.Sentence_Couple[item])
        except :
            print("mistake")#报错
    def Delete_Listbox1(self):
        num = self.__listbox1.size()
        if num > 0:
            self.__listbox1.delete(0, END)

    def Save_to_Mysql(self):
        try:

            self.TestDatabase.Insert_Data(File1.Sentence_Couple)
        except:
            print("mistake")  # 报错

    def Find_Data_by_Index(self):
        num = self.__listbox2.size()
        print(num)
        if num>0:
           self.__listbox2.delete(0,END)
        Start_Index = self.__entry4.get()
        End_Index = self.__entry5.get()
        list = self.TestDatabase.Find_Data_by_Index(int(Start_Index),int(End_Index))
        for item in list:
            self.__listbox2.insert(END,item)

    def Find_Data_by_Vocabulary(self):
        Chinese = re.compile(u'[\u4e00-\u9fa5]')
        English = re.compile(u'[a-zA-Z]')
        Connect_Setence_list = []
        num = self.__listbox2.size()
        print(num)
        if num > 0:
            self.__listbox2.delete(0, END)
        Str_Vocabulary = self.__entry7.get()
        if English.search(Str_Vocabulary) and not Chinese.search(Str_Vocabulary):
            Connect_Setence_list = self.TestDatabase.Find_Data_by_English_Vocabulary(Str_Vocabulary)
        if Chinese.search(Str_Vocabulary) and not English.search(Str_Vocabulary):
            Connect_Setence_list = self.TestDatabase.Find_Data_by_Chinese_Vocabulary(Str_Vocabulary)
        if Chinese.search(Str_Vocabulary) and English.search(Str_Vocabulary):
            tkinter.messagebox.showinfo('提示','请输入同一种语言')
        if len(Connect_Setence_list)>=1:
           for item in Connect_Setence_list:
               self.__listbox2.insert(END, item)

    def Delete_Index(self):
        num = self.__listbox2.size()
        if num>0:
           for item in range(0,num):
               if self.__listbox2.select_includes(item) == True:
                   self.__listbox2.delete(item)


    def Revive_Database(self):
        Q = ReviveUI(self.Get_var())
    def DownLoad(self):
        self.Down_Article.Get_Web()
        self.Down_Article.Web_Path = self.__entry1.get()
        self.Down_Article.project_name = self.__entry2.get()
        self.Down_Article.Operate_Chrome()

    def Mysql_to_File(self):
        self.TestDatabase.Export(self.var1.get(),self.__entry6.get())

    def Canvas_And_Button(self):
        self.__label1.grid(row = 0,column = 0)
        self.__entry1.grid(row = 0,column = 1)
        self.__label2.grid(row = 1,column = 0)
        self.__entry2.grid(row = 1,column = 1)
        self.__button1.grid(row = 0,column = 2)

        self.__label3.grid(row = 2,column = 0,pady = 40)
        self.__entry3.grid(row = 2,column = 1)
        self.__button2.grid(row = 2,column = 2)
        self.__listbox1.grid(row = 0,column = 0)
        self.__listbox1.configure(yscrollcommand = self.__scrollbar1.set,xscrollcommand = self.__scrollbar2.set)
        self.__scrollbar1['command'] = self.__listbox1.yview()
        self.__scrollbar2['command'] = self.__listbox1.xview()

        self.__scrollbar1.grid(row = 0,column = 1,rowspan = 20,sticky = W+N+S, padx = 1,pady =1)
        self.__scrollbar2.grid(row=1, column=0, rowspan=10, sticky=W + E + N, padx=1, pady=1)
        self.__button3.grid(row = 0,column = 0,sticky = N)
        self.__button4.grid(row = 1,column = 0)
        self.__button9.grid(row = 2,column = 0)
        self.__frameUpper1_1.grid(row = 3,column = 0,sticky = N)
        self.__frameUpper1_2.grid(row=3, column=1, sticky=N)
        #左侧页面布局
        self.__label4.grid(row=0, column=0)
        self.__entry4.grid(row=0, column=1)
        self.__label5.grid(row=0, column=2)
        self.__entry5.grid(row=0, column=3)
        self.__label6.grid(row=0, column=4)
        self.__button6.grid(row=0, column=5)
        self.__button8.grid(row=0, column=6,padx =5)
        self.__entry7.grid(row=0, column=0)
        self.__button10.grid(row=0, column=1)
        self.__button11.grid(row=0, column=2)
        self.__frameUpper2_1.grid(row=0, column=0,sticky = W+E)
        #右上页面布局
        self.__listbox2.configure(yscrollcommand=self.__scrollbar3.set, xscrollcommand=self.__scrollbar4.set)
        self.__scrollbar3['command'] = self.__listbox2.yview()
        self.__scrollbar4['command'] = self.__listbox2.xview()
        self.__listbox2.grid(row=0, column=0,pady=15,sticky = N+S+W)
        self.__scrollbar3.grid(row=0, column=1, rowspan=20, sticky=W + N + S, padx=1, pady=1)
        self.__scrollbar4.grid(row=1, column=0, rowspan=20, sticky=W + N + E, padx=1, pady=1)
        self.__label7.grid(row=0, column=0)
        self.__entry6.grid(row=0, column=1)
        self.__button5.grid(row=0, column=2)
        self.__label8.grid(row=0, column=0)
        self.__rbTXT.grid(row=0, column=1)
        self.__rbCSV.grid(row=0, column=2)
        self.__button7.grid(row=0, column=4)
        self.__frameUpper2_5.grid(row=1, column=0, sticky=N + S + W)
        self.__frameUpper2_3.grid(row=2, column=0, sticky=N + S + W)
        self.__frameUpper2_2.grid(row=3, column=0,sticky = N+S+W)
        self.__frameUpper2_4.grid(row=4, column=0, sticky=N + S + W)


        #右下页面布局
        self.__frameUpper1.grid(row=0, column=0)
        self.__frameUpper2.grid(row=0, column=1,sticky = N,padx =10)
        self.__root.mainloop()


class LoginUI:
    def __init__(self):
        self.root = Tk()
        self.root.title('Demo1')
        self.root.geometry('500x250+200+200')
        self.root.configure(bg='AliceBlue')
        self.root.resizable(width=False, height=False)
        self.var1 = IntVar()
        self.frameUpper1 = Frame(self.root, bg='AliceBlue')
        self.frameUpper2 = Frame(self.root, bg='AliceBlue')
        self.frameUpper3 = Frame(self.root, bg='AliceBlue')
        self.frameUpper4 = Frame(self.root, bg='AliceBlue')
        self.label1 = Label(self.root, text="英汉双语语料库系统", bg='AliceBlue',font=("helvetic",18,"bold") )
        self.label2 = Label(self.frameUpper1, text="账号",width = 12, bg='AliceBlue',font=("helvetic",12))
        self.entry2 = Entry(self.frameUpper1, bd=10, width=40)
        self.label3 = Label(self.frameUpper2, text="密码", width=12, bg='AliceBlue',font=("helvetic",12))
        self.entry3 = Entry(self.frameUpper2, bd=10, width=40)
        self.Administrator = Radiobutton(self.frameUpper3, text="管理员", variable=self.var1, value=1)
        self.Guest = Radiobutton(self.frameUpper3, text="用户", variable=self.var1, value=2)
        self.button1 = Button(self.frameUpper4, text="登录", width=20,height=2, command=self.Login)
        self.button2 = Button(self.frameUpper4, text="退出", width=20, height=2, command=self.root.quit)
        self.Canvas_And_Button()
    def Canvas_And_Button(self):
        self.label1.grid(row=0, column=0,pady=10)
        self.frameUpper1.grid(row=1, column=0)
        self.frameUpper2.grid(row=2, column=0)
        self.frameUpper3.grid(row=3, column=0,pady=15)
        self.frameUpper4.grid(row=4, column=0)
        self.button1.grid(row=0, column=0)
        self.button2.grid(row=0, column=1)
        self.label2.grid(row=0, column=0,padx=3)
        self.entry2.grid(row=0, column=1)
        self.label3.grid(row=0, column=0,padx=3)
        self.entry3.grid(row=0, column=1)
        self.Administrator.grid(row=0, column=0)
        self.Guest.grid(row=0, column=1)

        self.root.mainloop()

    def Get_Character(self, num):
        account = ''
        password = ''
        if num == 1:  # 管理员身份登录
            account = 'Administrator'
            password = 'Abc_123456'
        if num == 2:  # 用户身份登录
            account = 'USER'
            password = 'Abc_123456'
        Login_Keyword = [account, password]
        return Login_Keyword
    def Login(self):

        account_input = self.entry2.get()
        password_input = self.entry3.get()
        Login_Keyword = self.Get_Character(self.var1.get())
        if account_input == Login_Keyword[0] and password_input == Login_Keyword[1]:
                 self.root.destroy()
                 a = A(self.var1.get())

        else:
                 tkinter.messagebox.showinfo('警告', '用户信息有误，请重新输入')

class ReviveUI:
    def __init__(self,var):

        self.Database = Input_to_Mysql.Database(var)
        self.root = Tk()
        self.root.title('Demo3')
        self.root.geometry('900x600+50+50')
        self.root.configure(bg='AliceBlue')
        self.root.resizable(width=False, height=False)
        self.frameUpper1 = Frame(self.root, bg='AliceBlue')
        self.frameUpper1_1 = Frame(self.frameUpper1, bg='AliceBlue')
        self.frameUpper1_2 = Frame(self.frameUpper1, bg='AliceBlue')
        self.frameUpper1_3 = Frame(self.frameUpper1_2, bg='AliceBlue')
        self.frameUpper1_4 = Frame(self.frameUpper1_2, bg='AliceBlue')
        self.frameUpper2 = Frame(self.root, bg='AliceBlue')
        self.frameUpper3 = Frame(self.root, bg='AliceBlue')
        self.frameUpper4 = Frame(self.root, bg='AliceBlue')
        # frameUpper1布局
        self.label1_1 = Label(self.frameUpper1_3, text="从", padx=20)
        self.label1_2 = Label(self.frameUpper1_3, text="条 到")
        self.label1_3 = Label(self.frameUpper1_3, text="条")
        self.entry1_1 = Entry(self.frameUpper1_3, bd=10, width=10)
        self.entry1_2 = Entry(self.frameUpper1_3, bd=10, width=10)
        self.button1_1 = Button(self.frameUpper1_3, text="查询", width=10, command=self.Find_Data_by_Index)
        self.label2_1 = Label(self.frameUpper1_4, text="查询内容")
        self.entry2_1 = Entry(self.frameUpper1_4, bd=10, width=20)
        self.button2_1 = Button(self.frameUpper1_4, text="查询", width=10, command=self.Find_Data_by_Vocabulary)
        self.label1_1_1 = Label(self.frameUpper1_1, text="序号查询", padx=20,font=("宋体",10))
        self.label1_1_2 = Label(self.frameUpper1_1, text="词汇查询", padx=20,font=("宋体",10))
        # frameUpper2布局
        self.listbox2_1 = Listbox(self.frameUpper2, width=120, heigh=20, exportselection=False)
        # frameUpper3布局
        self.label3_1 = Label(self.frameUpper3, text="句对序号", padx=20)
        self.entry3_2 = Entry(self.frameUpper3, bd=10, width=10)
        self.label3_3 = Label(self.frameUpper3, text="英文", padx=20)
        self.entry3_4 = Entry(self.frameUpper3, bd=10, width=80)
        # frameUpper4布局
        self.button4_1 = Button(self.frameUpper4, text="修改", width=10, command=self.Alter)
        self.label4_1 = Label(self.frameUpper4, text="中文", padx=20)
        self.entry4_1 = Entry(self.frameUpper4, bd=10, width=80)
        self.Canvas_And_Button()
    def Find_Data_by_Index(self):
        num = self.listbox2_1.size()
        print(num)
        if num > 0:
            self.listbox2_1.delete(0, END)
        Start_Index = self.entry1_1.get()
        End_Index = self.entry1_2.get()
        list = self.Database.Find_Data_by_Index(int(Start_Index), int(End_Index))
        for item in list:
            self.listbox2_1.insert(END, item)
    def Find_Data_by_Vocabulary(self):
        Chinese = re.compile(u'[\u4e00-\u9fa5]')
        English = re.compile(u'[a-zA-Z]')
        Connect_Setence_list = []
        num = self.listbox2_1.size()
        print(num)
        if num > 0:
            self.listbox2_1.delete(0, END)
        Str_Vocabulary = self.entry2_1.get()
        if English.search(Str_Vocabulary) and not Chinese.search(Str_Vocabulary):
            Connect_Setence_list = self.Database.Find_Data_by_English_Vocabulary(Str_Vocabulary)
        if Chinese.search(Str_Vocabulary) and not English.search(Str_Vocabulary):
            Connect_Setence_list = self.Database.Find_Data_by_Chinese_Vocabulary(Str_Vocabulary)
        if Chinese.search(Str_Vocabulary) and English.search(Str_Vocabulary):
            tkinter.messagebox.showinfo('提示', '请输入同一种语言')
        if len(Connect_Setence_list) >= 1:
            for item in Connect_Setence_list:
                self.listbox2_1.insert(END, item)
    def Alter(self):
        id = self.entry3_2.get()
        English = self.entry3_4.get()
        Chinese = self.entry4_1.get()
        self.Database.Alter_Sentence(id,English,Chinese)

    def Canvas_And_Button(self):
        self.frameUpper1.grid(row=0, column=0)
        self.frameUpper2.grid(row=1, column=0,sticky=E)
        self.frameUpper3.grid(row=2, column=0,sticky=E)
        self.frameUpper4.grid(row=3, column=0,sticky=E)
        self.frameUpper1_1.grid(row=0, column=0,sticky=W+N+S)
        self.frameUpper1_2.grid(row=0, column=1,sticky=E+S+N)
        self.frameUpper1_3.grid(row=0, column=0,sticky=E)
        self.frameUpper1_4.grid(row=1, column=0,sticky=E)
        # frameUpper1布局
        self.label1_1_1.grid(row=0, column=0,pady=12,sticky=N)
        self.label1_1_2.grid(row=1, column=0,sticky=S)
        self.label1_1.grid(row=0, column=0)
        self.label1_2.grid(row=0, column=2)
        self.label1_3.grid(row=0, column=4)
        self.entry1_1.grid(row=0, column=1)
        self.entry1_2.grid(row=0, column=3)
        self.button1_1.grid(row=0, column=5)
        self.label2_1.grid(row=0, column=0)
        self.entry2_1.grid(row=0, column=1)
        self.button2_1.grid(row=0, column=2)
        # frameUpper2布局
        self.listbox2_1.grid(row=0, column=0)
        # frameUpper3布局
        self.label3_1.grid(row=0, column=0)
        self.entry3_2.grid(row=0, column=1)
        self.label3_3.grid(row=0, column=2)
        self.entry3_4.grid(row=0, column=3)
        # frameUpper4布局
        self.button4_1.grid(row=0, column=0)
        self.label4_1.grid(row=0, column=1)
        self.entry4_1.grid(row=0, column=2)
        self.root.mainloop()
