from urllib.request import Request, urlopen

urls = [
    "https://epg.112114.xyz/pp.xml.gz",
    "https://diyp.112114.xyz/"  # 新增的链接，你可以替换为实际需要的链接
]

# 遍历URL列表，下载文件
for url in urls:
    try:
        req = Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'})
        with urlopen(req, timeout=10) as response:  # 设置超时时间为10秒
            data = response.read()
            file_name = url.split('/')[-1]  # 从URL中获取文件名
            with open(file_name, 'wb') as file:
                file.write(data)
            print(f"成功下载文件: {file_name} 来自 {url}")
    except Exception as e:
        print(f"下载文件时出错: {e} 对于URL: {url}")
