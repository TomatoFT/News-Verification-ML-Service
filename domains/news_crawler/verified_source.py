from base_get_link import BaseNewsLinks

class VTVNewsLinks(BaseNewsLinks):
    source = 'https://vtv.vn/' 
    format_category_urls = [
                    'chinh-tri.htm',
                    'xa-hoi.htm',
                    'phap-luat.htm',
                    'the-gioi.htm',
                    'kinh-te.htm',
                    'the-thao.htm',
                    'van-hoa-giai-tri.htm',
                    'doi-song.htm',
                    'cong-nghe.htm',
                    'giao-duc.htm',
                    'suc-khoe.htm'
                    ]
    unformat_category_urls = ['https://suckhoe.vtv.vn/']
    news_pos = 4

class ThanhNienNewsLinks(BaseNewsLinks):
    source = 'https://thanhnien.vn/' 
    format_category_urls = [
                    'thoi-su.htm',
                    'the-gioi.htm',
                    'kinh-te.htm',
                    'doi-song.htm',
                    'suc-khoe.htm',
                    'gioi-tre.htm',
                    'giao-duc.htm',
                    'du-lich.htm',
                    'van-hoa.htm',
                    'giai-tri.htm',
                    'the-thao.htm',
                    'cong-nghe-game.htm',
                    'xe.htm',
                    'tieu-dung-thong-minh.htm',
                    'thoi-trang-tre.htm'
                    ]
    unformat_category_urls = ['']
    news_pos = 3

class VnExpressNewsLink(BaseNewsLinks):
    source = 'https://vnexpress.net/'
    format_category_urls = ['thoi-su', 'goc-nhin', 'the-gioi', 'kinh-doanh', 
                            'bat-dong-san', 'khoa-hoc', 'giai-tri', 'the-thao', 'phap-luat'
                            'giao-duc', 'suc-khoe', 'doi-song', 'du-lich', 
                            'so-hoa', 'xe', 'y-kien', 'tam-su', 'thu-gian']
    unformat_category_urls = ['']
    news_pos = 3