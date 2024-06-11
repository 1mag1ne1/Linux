#coding = utf-8



import os


# 读取
def read_file(file_name):
    # 获取key文件的绝对路径
    file_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), file_name)
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
        f.close()
    return content