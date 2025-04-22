import requests
import os

urls = [
    "https://epg.112114.xyz/pp.xml",
    "https://epg.112114.xyz/pp.xml.gz"
]

for url in urls:
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            file_name = os.path.basename(url)
            with open(file_name, 'wb') as file:
                file.write(response.content)
            file_size = os.path.getsize(file_name)
            if file_size > 0:
                print(f"{file_name} 下载成功，文件大小: {file_size} 字节。")
            else:
                print(f"{file_name} 下载可能失败，文件大小为 0 字节。")
        else:
            print(f"下载失败，状态码: {response.status_code}")
    except requests.RequestException as e:
        print(f"下载 {url} 时发生网络错误: {e}")
        
