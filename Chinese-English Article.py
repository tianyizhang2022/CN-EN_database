import requests
from bs4 import BeautifulSoup
import re
from bs4.element import NavigableString
def DownLoad(url,file_name,j):

    user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
    headers = {'User-Agent': user_agent}
    r = requests.get(url,headers = headers)
    r.encoding = 'utf-8'
    soup = BeautifulSoup(r.text, 'lxml')
    #ENWord_list = soup.find_all("span",attrs={'class':'hcdict'})
    #ENWord_list = soup.find_all("span")
    Word_list = soup.find_all("td", attrs={'class': 'zuoyou'})
    print(j)
    CNPassege_list = soup.find_all("p")
   # Next_Html_List = soup.find_all("strong")
   # for Next_Html_Offspring in Next_Html_List:
       # if Next_Html_Offspring.get_text() == "下一页":
            #  Next_Html = Next_Html_Offspring.parent["href"]
              ##break

    #for word in ENWord_list:
       # if 'class' in word.attrs:
        #   #if word["class"] == "hcdict":
           #    with open(file_name, 'a', encoding='utf-8') as file_obj:
             #      file_obj.write(word.get_text())
              #     file_obj.close()
              # if word.next_sibling is None:
               #    with open(file_name, 'a', encoding='utf-8') as file_obj:
                #        file_obj.write("\n")
                 #       file_obj.close()
    #for CNPassege in CNPassege_list:
        #if CNPassege.children is None:
    for item in Word_list:

         with open(file_name, 'a', encoding='utf-8') as file_obj:

                file_obj.write(item.get_text())
                file_obj.write("\n")
                file_obj.close()


def FindHtml(url):
    html_list = []
    Cookie = "id=2232f29537c10007||t=1581432125|et=730|cs=002213fd482bb4a7c37f4a1380"
    Use_Agent = "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"
    headers = {'User-Agent':Use_Agent,'Cookie':Cookie,}
    r = requests.get(url,headers = headers)
    r.encoding = 'utf-8'
    soup = BeautifulSoup(r.text, 'lxml')
    html_list_source = soup.find_all("a")
    for item in html_list_source:
        if 'href' in item.attrs:
           if re.search('http://www.kekenet.com/read/20', item["href"]):
               html_list.append(item["href"])

    return html_list

def FindNextHtml(url,i):
    Cookie = "id=2232f29537c10007||t=1581432125|et=730|cs=002213fd482bb4a7c37f4a1380"
    Use_Agent = "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"
    headers = {'User-Agent': Use_Agent, 'Cookie': Cookie, }
    r = requests.get(url, headers=headers)
    Next_Html = ""
    r.encoding = 'utf-8'
    soup = BeautifulSoup(r.text, 'lxml')
    html_list_source = soup.find_all("a")
    Current_html = soup.find("div",attrs={"class","page th"})
    for item in Current_html.contents:
        if isinstance(item, NavigableString) is False :
            if 'href' in item.attrs:
                if item.get_text() == str(i+1):
                    Next_Html = "http://www.kekenet.com"+item["href"]
                    break
            else:
                if item.get_text() == str(i+1):
                    Next_Html = "http://www.kekenet.com" + item.next_sibling.next_sibling["href"]
    #for item in html_list_source:
      #if 'href' in item.attrs:
           # if re.search('http://www.kekenet.com/read/story/pride/',item["href"]):
             #   str1 = item["href"]+"1111"
               # print(str1)
        #print(item.get_text())
        #if item.get_text() == "下一页":#.isdigit():#
           # print(111111111)
            #print(item.next_sibling["href"])
           # Next_Html = item["href"]
            #print(Next_Html+"111")
            #break
    if i == 3:
        print("3")
    return Next_Html

if __name__ =="__main__":
    i = 1
    j = 1
    n = 2
    Html_List = []
    url = "http://www.kekenet.com/menu/13348/"
    file_name = 'D:/pycharmfile/University-Design/Article13'
    Html_List = FindHtml(url)
    for index in range(1,2):
        for html in Html_List:
            DownLoad(html,file_name,j)
            with open(file_name, 'a', encoding='utf-8') as file_obj:
                file_obj.write("\n\n")
            j = j+1
        #url = FindNextHtml(url,i)
        #url = "http://www.kekenet.com/read/story/dongbei/List_"+str(n-1)+".shtml"
        url = "http://www.kekenet.com/menu/13347/"
        i = i + 1
        Html_List = FindHtml(url)

