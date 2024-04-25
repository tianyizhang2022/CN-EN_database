from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import IU

class Connected_Pyspider:
    def __init__(self):
        self.Pyspider_Path = ''  #pyspider运行端口
        self.Web_Path = '' #要爬取的目标网站
        self.Index_page = "'.clearfix a'"
        self.text_in_Detail_page = "'text'"
        self.text_Code ="'.text'"
        self.project_name = ''
        self.Detail_page = ''' "url": response.url, "title": response.doc('title').text(), "text" : (response.doc('.text').text() or response.doc('.text > p').text()) '''
        #chrome_driver = 'C:\Program Files (x86)\DcBrowser\chromedriver.exe'

    def Get_Web(self):
        self.Pyspider_Path ="http://localhost:5000"
          # 要爬取的目标网站

    def Operate_Chrome(self):
        brower = webdriver.Chrome()
        brower.get(self.Pyspider_Path)
        Button_Create1 = brower.find_element_by_class_name('btn')
        Button_Create1.click()
        time.sleep(2)
        Input_Project_Name = brower.find_element_by_name('project-name')
        Input_Project_Name.send_keys(self.project_name)
        time.sleep(2)
        Input_URL_Name = brower.find_element_by_name('start-urls')
        Input_URL_Name.send_keys(self.Web_Path)
        time.sleep(2)
        # Button_DownLoad1 = brower.find_element_by_css_selector("a[href='/debug/DownLoad1']")
        # time.sleep(2)
        # Button_DownLoad1.click()
        Button_Create2 = brower.find_element_by_css_selector("button[class='btn btn-primary']")
        time.sleep(2)
        Button_Create2.click()
        #Code_Find_Html1 = brower.find_element_by_xpath("//*[contains(text(),'http://novel')]")
        time.sleep(2)
        js_Index_page = 'x=document.getElementsByClassName("cm-string")[10]; x.innerHTML="{name}";'.format(name = self.Index_page)#找[9]
        js_text_in_Detail_page = 'x=document.getElementsByClassName("cm-string")[12]; x.innerHTML="{name}";'.format(name = self.text_in_Detail_page)
        js_code_in_Detail_page = 'x=document.getElementsByClassName("cm-string")[13]; x.innerHTML="{name}";'.format(name = self.text_Code)
        #修改index_page和detail_page,在class值为cm-string的元素列表中寻找上述三个元素 [10] [12] [13]
        time.sleep(2)
        brower.execute_script(js_text_in_Detail_page)
        time.sleep(2)
        brower.execute_script(js_Index_page)
        time.sleep(2)
        brower.execute_script(js_code_in_Detail_page)
        Button_Save = brower.find_element_by_css_selector("div[id='save-task-btn']")
        time.sleep(2)
        Button_Save.click()
        Button_Back = brower.find_element_by_xpath("//*[text()='pyspider']")
        time.sleep(2)
        Button_Back.click()
        st = "tr[data-name='{file_name}']".format(file_name = self.project_name)
          #输入代码，修改index_page和detail_page，定位文章的html连接，和下载的文档，然后点击save
        First_Tab = brower.find_element_by_css_selector(st)
        Sencond_Tab = First_Tab.find_element_by_css_selector("span[data-value='TODO']")
        Sencond_Tab.click()
        time.sleep(2)
        Option_Debug = First_Tab.find_element_by_css_selector("option[value='DEBUG']")
        Option_Debug.click()
        time.sleep(2)
        Ready = First_Tab.find_element_by_css_selector("button[class='btn btn-primary btn-sm editable-submit']")
        Ready.click()
        time.sleep(2)
        Run = First_Tab.find_element_by_css_selector("button[class='project-run btn btn-default btn-xs']")
        Run.click()
        time.sleep(2)
        Result = First_Tab.find_element_by_css_selector("a[class='btn btn-default btn-xs']")
        Result.click()


        # time.sleep(2)
        #
        #返回上一页













