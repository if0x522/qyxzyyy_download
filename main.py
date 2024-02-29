# 从起源小说 https://www.qyxzyyy.com/ 下载小说

from httpGet import getHtml
from fileIO import sevaFile
from readFile import getindexpage,getindex,getcontent,theNextPage
import config
from tqdm import tqdm


def startpage(host:str,index:dict)->str:
    # print(index['title'] + '开始下载')
    url = host + index['url']
    # 获取本章第一页
    html = getHtml(url)
    t_data = index['title'] + '\n\n' + getcontent(html)
    # print('第1页下载完成')
    a = []
    index = url.find('/')
    while index != -1:
        a.append(index)
        index = url.find('/', index+1)
    url = url[:a[-1]] + '/'
    count = 2
    while True:
        # 判断是否有下一页
        n_flg = theNextPage(html)
        if n_flg:
            html = getHtml(url + n_flg)
            t_data += getcontent(html)
            # print(f'第{count}页下载完成')
            count += 1
        else:
            break
    return t_data + '\n\n'
    

def startDownload(url, title):
    # 解析主机
    host = 'https://' + url.split('/')[2]
    # 获取网页源码
    html = getHtml(url)
    # 保存网页源码
    sevaFile('./tmp/root.html', html)
    # 获取目录分页
    indexpage = getindexpage(html)
    index = []
    for page in indexpage:
        html = getHtml(host + page)
        sevaFile('./tmp/' + page[-1] + '.html', html)
        index += getindex(html)
    sevaFile('./tmp/index.json', str(index))
    # 获取小说内容
    for i in tqdm(index):
        content = startpage(host,i)
        # 保存小说,追加模式
        with open(f'./out/{title}.txt', 'a', encoding='utf-8') as f:
            f.write(content)
    # # 保存小说
    # sevaFile(f'./out/{title}.txt', content)
        






if __name__ == '__main__':
    startDownload(config.url, config.title)
