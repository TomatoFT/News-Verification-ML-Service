from bs4 import BeautifulSoup

html = """
<a href="/chinh-tri/tuyen-bo-chung-viet-nam-trung-quoc-20231213162124309.htm" title="Tuyên bố chung Việt Nam - Trung Quốc">
    <img alt="Tuyên bố chung Việt Nam - Trung Quốc" src="https://vtv1.mediacdn.vn/zoom/527_330/562122370168008704/2023/12/13/photo1702459171315-1702459171562626103418.jpg"/>
    <span class="sprite image_icon_video"></span>
</a>
<a data-nocheck="1" href="/chinh-tri/infographic-36-van-ban-thoa-thuan-hop-tac-giua-viet-nam-trung-quoc-20231213153828674.htm" title="[Infographic] 36 văn bản thỏa thuận hợp tác giữa Việt Nam - Trung Quốc">[Infographic] 36 văn bản thỏa thuận hợp tác giữa Việt Nam - Trung Quốc</a>
<a href="/chinh-tri/tong-bi-thu-nguyen-phu-trong-chia-tay-tong-bi-thu-chu-tich-nuoc-trung-quoc-tap-can-binh-20231213181421942.htm" title="Tổng Bí thư Nguyễn Phú Trọng chia tay Tổng Bí thư, Chủ tịch nước Trung Quốc Tập Cận Bình">
    <img alt="Tổng Bí thư Nguyễn Phú Trọng chia tay Tổng Bí thư, Chủ tịch nước Trung Quốc Tập Cận Bình" src="https://vtv1.mediacdn.vn/zoom/227_142/562122370168008704/2023/12/13/photo1702465938361-1702465938712227861446.jpg"/>
</a>
"""

# Parse the HTML content with BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')

# Find all <a> tags and get the href attributes
href_list = [a.get('href') for a in soup.find_all('a')]

# Print the extracted href attributes
for href in href_list:
    if href.startswith('/'):
        print(href)
