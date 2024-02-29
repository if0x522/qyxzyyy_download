from bs4 import BeautifulSoup


# 获取目录分页
def getindexpage(html: str) -> list[str]:
    soup = BeautifulSoup(html, 'lxml')
    indexpage = []
    middle = soup.select('.middle')[0]
    for a in middle.select('option'):
        # print(a)
        indexpage.append(a['value'])
    # print(indexpage)
    return indexpage

def getindex(html:str) -> list[str]:
    soup = BeautifulSoup(html, 'lxml')
    index = []
    bxxqyx = soup.select('#bxxqyx')[1]
    a_list = bxxqyx.select('a')
    for a in a_list:
        index.append({
            'title': a.text,
            'url': a['href']
        
        })
    # print(index)
    return index

def getcontent(html:str) -> str:
    soup = BeautifulSoup(html, 'lxml')
    content = soup.select('#content')[0]
    text = str(content).replace('<br/>', '\n')
    soup = BeautifulSoup(text,'lxml')
    content = soup.text
    # print(content)
    return content

def theNextPage(html:str) -> str:
    soup = BeautifulSoup(html, 'lxml')
    bottem2 = soup.select('.bottem2')[0]
    nextpage = bottem2.select('a')[-1]['href']
    # print(nextpage)
    # 判断href属性中是否有_
    if nextpage.find('_') != -1:
        return nextpage
    else:
        return False

if __name__ == '__main__':
    with open('./tmp/test.html', 'r', encoding='utf-8') as f:
        html = f.read()
    getcontent(html)