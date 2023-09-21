import requests
from bs4 import BeautifulSoup
def crawler():
    url="https://s.weibo.com/top/summary?cate=realtimehot"
    user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 SLBrowser/8.0.1.4031 SLBChan/105"
    #注意时常更换cookie
    cookie="SUBP=0033WrSXqPxfM72-Ws9jqgMF55529P9D9WWxh0XssYqimCLQEQmDh0vI; SUB=_2AkMUyli0f8NxqwJRmfERzmvrbIlxzwvEieKilqlvJRMxHRl-yT9jqkImtRB6P0p2W2TWM74w_JIg00paHGpBu28DcOq-; XSRF-TOKEN=rABtdk5ONAQrDwvdlW40uwIZ; WBPSESS=5Gh1MjbHbWED7wnbzL0HeoLgnFOwlWBlIFhrLNLOwXhyylSyha2uZuN4daHtU72XyzqHTJ7JoS5HZ0g1vtNK2KpuN4uIxg7SqYcD5nyvzAM4YsGVt3I_UF5p3KMzeNsrYp8bpUd13dKaaYp6SW1KyqlCZ6w6fA8CjYlirLmV-Qw="

    headers={"User-Agent": user_agent, "Cookie": cookie}

    response = requests.get(url=url, headers=headers)


    soup = BeautifulSoup(response.text,"html.parser")
    html=soup.findAll("a",attrs={"target":"_blank"})
    return html


# for i in crawler():
#     b=i.string
#     print(b)

# --------------------------------------------------------------------------------

#清除内容
def clear_content(file_path):
    try:
        with open(file_path, 'r',encoding='utf-8') as f:
            lines = f.readlines()

        start_index = -1
        end_index = -1

        for i, line in enumerate(lines):
            if '<body>' in line:
                start_index = i
            elif '</body>' in line:
                end_index = i


        if start_index != -1 and end_index != -1:
            lines = lines[:start_index+1] + lines[end_index:]


        with open(file_path, 'w',encoding='utf-8') as f:
            f.writelines(lines)

        print("清除内容成功")
    except IOError as e:
        print(f"文件处理错误：{e}")

# test


# --------------------------------
#写入

def insert_content(file_path, content):
    with open(file_path, 'r+',encoding='utf-8') as file:
        text = file.read()
        start_index = text.find("<body>")
        end_index = text.find("</body>") + len("</body>")

        new_text = text[:start_index] + "<body>" + content + "</body>" + text[end_index:]
        file.seek(0)
        file.write(new_text)
        file.truncate()

file_path = r"C:\Users\Mr.chen\Desktop\crawler.html"
contents="<ol><li>"
count=0
for i in crawler():
    count+=1
    if(count>=51):
        break
    contents+=i.string
    contents+="<li>"
new_contents=contents[:-4]
new_contents+="<ol>"
content=new_contents
#先清除原有的
clear_content(r'C:\Users\Mr.chen\Desktop\crawler.html')
#导入top50
insert_content(file_path, content)
