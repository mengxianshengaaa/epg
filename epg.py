import requests
import os

# 要下载的文件链接
urls = [
    "https://epg.112114.xyz/pp.xml"
]

for url in urls:
    # 下载文件
    response = requests.get(url)
    if response.status_code == 200:
        # 保存文件名
        file_name = os.path.basename(url)
        with open(file_name, 'wb') as file:
            file.write(response.content)
        print(f"{file_name} 下载成功。")

        # 假设你已经在本地初始化了一个 Git 仓库，并且当前目录是仓库目录
        # 执行 Git 命令添加文件
        os.system(f"git add {file_name}")
        # 执行 Git 命令提交文件
        os.system(f'git commit -m "Add {file_name}"')
        # 执行 Git 命令推送文件到远程仓库（请确保已经配置好远程仓库地址）
        os.system("git push")
    else:
        print(f"下载失败，状态码: {response.status_code}")
