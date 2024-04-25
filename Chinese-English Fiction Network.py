import requests
from bs4 import BeautifulSoup
import re
from bs4.element import NavigableString

def DownLoad(url,file_name):
    user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
    headers = {'User-Agent': user_agent}
    r = requests.get(url, headers=headers)
    r.encoding = 'utf-8'
    soup = BeautifulSoup(r.text, 'lxml')
    Passage = soup.find_all("p")
    for item in Passage:
        with open(file_name, 'a', encoding='utf-8') as file_obj:
            file_obj.write(item.get_text())
            file_obj.write("\n")
            file_obj.close()

def FindHtml(url):
    Html_list = []
    user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
    headers = {'User-Agent': user_agent}
    r = requests.get(url, headers=headers)
    r.encoding = 'utf-8'
    soup = BeautifulSoup(r.text, 'lxml')
    Html_Source = soup.find_all("a")
    for Html in Html_Source:
        if 'href' in Html.attrs:
           if re.search('38', Html["href"]):
               Html_list.append("http://novel.tingroom.com/shuangyu/696/"+Html["href"])
    return Html_list




if __name__ =="__main__":
    url = "http://novel.tingroom.com/shuangyu/696/list.html"
    file_name = 'D:/pycharmfile/University-Design/English-Chinese Resource2/Article13'
    Html_List = FindHtml(url)
    for html in Html_List:
        DownLoad(html,file_name)