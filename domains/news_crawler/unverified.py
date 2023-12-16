from base_get_link import BaseBS4NewsLinks


class DKNNewsLink(BaseBS4NewsLinks):
    source = 'https://www.dkn.tv/'
    format_category_urls = ['cat/thoi-su', 'cat/the-gioi', 'cat/van-hoa', 
                            'cat/doi-song', 'cat/ve-dep-chan-thien-nhan', 'e-magazine', 'khoa-hoc-cong-nghe']
    
    unformat_category_urls = ['']
    news_pos = -1
    name = 'DKN'


class NgoisaoLink(BaseBS4NewsLinks):
    source = 'https://ngoisao.vnexpress.net/'
    format_category_urls = ['showbiz', 'thoi-trang', 'lam-dep', 'an-choi', 
                            'loi-song', 'the-thao', 'thoi-cuoc', 'thuong-truong']
    unformat_category_urls = ['']
    news_pos = 3
    name = 'Ngoi Sao VNExpress'





class LuatKhoaLink(BaseBS4NewsLinks):
    source = 'https://www.luatkhoa.com/'
    format_category_urls = ['tag/chinh-tri', 'tag/the-che', 'tag/hinh-su', 'tag/viet-nam-cong-hoatag/luat-my', 
                            'tag/luat-quoc-te', 'tag/diem-sach', 'tag/quan-diem', 
                            'tag/chinh-tri/page/2/', 'tag/chinh-tri/page/3/', 'tag/chinh-tri/page/4/', 
                            'tag/chinh-tri/page/5/', 'tag/chinh-tri/page/6/', 'tag/the-che/page/2/', 
                            'tag/the-che/page/3/', 'tag/the-che/page/4/', 'tag/the-che/page/5/', 
                            'tag/the-che/page/6/', 'tag/hinh-su/page/2/', 'tag/hinh-su/page/3/', 
                            'tag/hinh-su/page/4/', 'tag/hinh-su/page/5/', 'tag/hinh-su/page/6/', 
                            'tag/viet-nam-cong-hoatag/luat-my/page/2/', 'tag/viet-nam-cong-hoatag/luat-my/page/3/', 
                            'tag/viet-nam-cong-hoatag/luat-my/page/4/', 'tag/viet-nam-cong-hoatag/luat-my/page/5/', 
                            'tag/viet-nam-cong-hoatag/luat-my/page/6/', 'tag/luat-quoc-te/page/2/', 'tag/luat-quoc-te/page/3/', 
                            'tag/luat-quoc-te/page/4/', 'tag/luat-quoc-te/page/5/', 'tag/luat-quoc-te/page/6/', 
                            'tag/diem-sach/page/2/', 'tag/diem-sach/page/3/', 'tag/diem-sach/page/4/', 'tag/diem-sach/page/5/', 
                            'tag/diem-sach/page/6/', 'tag/quan-diem/page/2/', 
                            'tag/quan-diem/page/3/', 'tag/quan-diem/page/4/', 'tag/quan-diem/page/5/', 'tag/quan-diem/page/6/'
]
    unformat_category_urls = ['']
    news_pos = -2
    name = 'Luat Khoa'

