
def sevaFile(name: str, content: str):
    try:
        with open(name, 'w', encoding='utf-8') as f:
            f.write(content)
            print(f'{name} 保存成功')
    except Exception as e:
        print(f'{name} 保存失败')
        print(e)
    