import os
from bs4 import BeautifulSoup

root_dir = r"D:\\wen\\80days"

for file in os.listdir(root_dir):
    file_name = root_dir + "\\" + file
    filein = open(file_name, "rb")
    bb = BeautifulSoup(filein).get_text()
    with open("D:\\wen2\\1\\{0}.txt".format(file), "a",encoding="utf-8") as file_handle:
        file_handle.write(bb)  # 将txt文本依次写入文件夹中
        file_handle.write('\n')

