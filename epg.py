import requests
import os
import xml.etree.ElementTree as ET
from datetime import datetime

# 要下载的文件链接
urls = [
    "https://epg.112114.xyz/pp.xml",
    "https://epg.pw/xmltv/epg_HK.xml",
    "https://epg.pw/xmltv/epg_TW.xml"
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
        
        # 执行Git操作
        os.system(f"git add {file_name}")
        os.system(f'git commit -m "Add {file_name}"')
        
    except requests.exceptions.RequestException as e:
        print(f"下载失败: {e}")
    except Exception as e:
        print(f"发生错误: {e}")

# 合并XML文件（如果有多个下载文件）
if len(downloaded_files) > 1:
    try:
        # 创建新的根节点
        new_root = ET.Element("tv")
        
        # 添加生成信息
        info = ET.SubElement(new_root, "info")
        info.set("generator", "EPG_Merger")
        info.set("created", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        
        # 合并所有文件的内容
        for file in downloaded_files:
            tree = ET.parse(file)
            root = tree.getroot()
            
            # 将每个文件中的channel和programme节点添加到新的根节点
            for channel in root.findall("channel"):
                new_root.append(channel)
            for programme in root.findall("programme"):
                new_root.append(programme)
        
        # 保存合并后的文件
        merged_file = "pp.xml"
        new_tree = ET.ElementTree(new_root)
        new_tree.write(merged_file, encoding="utf-8", xml_declaration=True)
        print(f"合并文件 {merged_file} 已生成。")
        
        # 提交合并文件到Git
        os.system(f"git add {merged_file}")
        os.system(f'git commit -m "Merge EPG files into 123.xml"')
        os.system("git push")
        
    except Exception as e:
        print(f"合并文件时出错: {e}")
else:
    print("没有足够的文件进行合并。")
