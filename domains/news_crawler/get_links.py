import csv

from base_get_link import BaseBS4NewsLinks, BaseSeleniumNewsLinks


class VTVNewsLinks(BaseSeleniumNewsLinks):
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
    name = 'VTV'

class ThanhNienNewsLinks(BaseSeleniumNewsLinks):
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
    name = 'Thanh_Nien'

class VnExpressNewsLink(BaseBS4NewsLinks):
    source = 'https://vnexpress.net/'
    format_category_urls = ['thoi-su', 'goc-nhin', 'the-gioi', 'kinh-doanh', 
                            'bat-dong-san', 'khoa-hoc', 'giai-tri', 'the-thao', 'phap-luat'
                            'giao-duc', 'suc-khoe', 'doi-song', 'du-lich', 
                            'so-hoa', 'xe', 'y-kien', 'tam-su', 'thu-gian']
    unformat_category_urls = ['']
    news_pos = 3
    name = 'VnExpress'

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

class LinkCrawler:
    def __init__(self, sources) -> None:
        self.sources = sources

    def __call__(self) -> Any:
        for source in self.sources:
            crawler = source()
            crawler.get_articles_link().to_csv()
    

class CombineCSV:
    def __init__(self, directory_path, output_file) -> None:
        self.directory_path = directory_path
        self.output_file = output_file

    def __call__(self):
        # Get a list of all CSV files in the directory
        csv_files = [file for file in os.listdir(self.directory_path) if file.endswith('.csv')]

        # Check if there are any CSV files in the directory
        if not csv_files:
            print("No CSV files found in the specified directory.")
            return

        # Open the output file in write mode
        with open(self.output_file, 'w', newline='') as combined_csv:
            # Create a CSV writer object
            csv_writer = csv.writer(combined_csv)

            # Write the header (assuming the first file has the header)
            with open(os.path.join(self.directory_path, csv_files[0]), 'r') as first_file:
                header = next(csv.reader(first_file))
                csv_writer.writerow(header)

            # Loop through each CSV file and append its data to the combined CSV file
            for csv_file in csv_files:
                file_path = os.path.join(self.directory_path, csv_file)
                with open(file_path, 'r') as current_file:
                    # Skip the header in the current file
                    next(current_file)
                    # Write the remaining rows to the combined CSV file
                    for row in csv.reader(current_file):
                        csv_writer.writerow(row)

        print(f"Combined data saved to {self.output_file}")
