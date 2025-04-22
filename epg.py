import requests
import subprocess
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
                try:
                    subprocess.run(['git', 'add', file_name], check=True)
                    print(f"Git 添加 {file_name} 成功。")
                except subprocess.CalledProcessError as e:
                    print(f"Git 添加 {file_name} 失败: {e}")
                    continue
                try:
                    subprocess.run(['git', 'commit', '-m', f'Add {file_name}'], check=True)
                    print(f"Git 提交 {file_name} 成功。")
                except subprocess.CalledProcessError as e:
                    print(f"Git 提交 {file_name} 失败: {e}")
                    continue
                try:
                    subprocess.run(['git', 'push'], check=True)
                    print(f"Git 推送 {file_name} 成功。")
                except subprocess.CalledProcessError as e:
                    print(f"Git 推送 {file_name} 失败: {e}")
            else:
                print(f"{file_name} 下载可能失败，文件大小为 0 字节。")
        else:
            print(f"下载失败，状态码: {response.status_code}")
    except requests.RequestException as e:
        print(f"下载 {url} 时发生网络错误: {e}")
