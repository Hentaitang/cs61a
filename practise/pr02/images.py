import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

# 设置目标网站 URL
url = 'https://bgm.tv/user/569501'  # 替换为你要爬取的网站

# 设置下载图片保存的目录
output_dir = 'images'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# 添加请求头，模拟浏览器访问
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
}

# 发送请求，获取网页内容
response = requests.get(url, headers=headers)
if response.status_code == 200:
    # 解析网页
    soup = BeautifulSoup(response.text, 'html.parser')

    # 查找所有 <img> 标签
    img_tags = soup.find_all('img')

    # 提取并下载每个图片的 URL
    for img_tag in img_tags:
        img_url = img_tag.get('src')

        # 如果图片 URL 不是完整的，使用 urljoin 补全
        img_url = urljoin(url, img_url)

        # 下载图片
        img_data = requests.get(img_url, headers=headers).content
        img_name = os.path.join(output_dir, os.path.basename(img_url))

        # 保存图片到本地
        with open(img_name, 'wb') as f:
            f.write(img_data)
            print(f"Downloaded {img_name}")

else:
    print(f"Failed to retrieve website, status code: {response.status_code}")
