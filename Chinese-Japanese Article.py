import requests
from bs4 import BeautifulSoup

def DownLoad(url,file_name):

    r = requests.get(url)
    r.encoding = 'utf-8'
    soup = BeautifulSoup(r.text, 'lxml')

    t_list = soup.find_all("p")
    nex = soup.find_all("strong")
    for item in nex:
        ne = item.get_text()
        if ne == "下一篇：":
            hel = item.next_sibling["href"]
            break
    print(hel)
    for item in t_list:
        print(item.get_text())
        with open(file_name,'a',encoding='utf-8') as file_obj:
            file_obj.write(item.get_text())
            file_obj.close()
    return hel


if __name__ =="__main__":
    url = "http://jp.tingroom.com/yuedu/wenzhang/3836.html"
    file_name = 'D:/pycharmfile/University-Design/Article'

    for index in range(1,290):
        next_html = DownLoad(url,file_name)
        url = next_html
