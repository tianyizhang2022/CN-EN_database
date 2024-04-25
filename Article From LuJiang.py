import requests
from bs4 import BeautifulSoup
import re
def DownLoad(url,file_name):
    r = requests.get(url)
    r.encoding = 'utf-8'
    html_list = []
    soup = BeautifulSoup(r.text, 'lxml')
    t_list1 = soup.find_all("div",attrs={'class':'langs_en'})
    t_list2 = soup.find_all("div",attrs={'class':'langs_cn'})
    html_list_source = soup.find_all("a")
    for item in html_list_source:
        if re.search('/new/p42',item["href"]): #and re.search('日语美文阅读',item["title"]):
            html_list.append("https://jp.hjenglish.com"+item["href"])


    for item in t_list1:
        ne1 = item.get_text()
        print(ne1)
        with open(file_name,'a',encoding='utf-8') as file_obj:
            file_obj.write(item.get_text()+"\n")
            file_obj.close()
    for item in t_list2:
        ne2 = item.get_text()
        print(ne2)
        with open(file_name,'a',encoding='utf-8') as file_obj:
            file_obj.write(item.get_text()+"\n")
            file_obj.close()
    return html_list
        #for html in html_list:
          #  DownLoad(html, file_name)



if __name__ =="__main__":
    html_list = []
    html_list2 = [[]]
    url = "https://jp.hjenglish.com/new/p423987/"
    file_name = 'D:/pycharmfile/University-Design/Article2'
    html_list.extend(DownLoad(url,file_name))
    #for index in range(1,4):
    for html in html_list:
            html_list2.append(DownLoad(html,file_name))
    for index in html_list2:
        for html in index:
            DownLoad(html,file_name)