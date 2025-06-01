import requests
import os
import xml.etree.ElementTree as ET
from datetime import datetime

# 要下载的文件链接
urls = [
    "https://epg.112114.xyz/pp.xml",
    "https://epg.pw/xmltv/epg_HK.xml",
    "https://epg.pw/xmltv/epg_TW.xml",
    "https://epg.pw/xmltv/epg_CN.xml"
]

# 存储下载的文件路径
downloaded_files = []

for url in urls:
    try:
        # 下载文件
        response = requests.get(url, timeout=30)
        response.raise_for_status()  # 检查请求是否成功
        
        # 保存文件名
        file_name = os.path.basename(url)
        with open(file_name, 'wb') as file:
            file.write(response.content)
        print(f"{file_name} 下载成功。")
        downloaded_files.append(file_name)
        
    except requests.exceptions.RequestException as e:
        print(f"下载失败: {e}")
    except Exception as e:
        print(f"发生错误: {e}")

# 批量提交所有下载文件到Git
if downloaded_files:
    try:
        # 添加所有下载的文件
        for file in downloaded_files:
            os.system(f"git add {file}")
        
        # 提交并推送到远程仓库
        commit_msg = f"Download EPG files on {datetime.now().strftime('%Y-%m-%d')}"
        os.system(f'git commit -m "{commit_msg}"')
        os.system("git push")
        print(f"已将 {len(downloaded_files)} 个文件提交到Git仓库")
        
    except Exception as e:
        print(f"Git操作出错: {e}")
else:
    print("没有文件被下载，无法执行Git操作")
