from verified_source import VTVNewsLinks, ThanhNienNewsLinks, VnExpressNewsLink

vtv = VTVNewsLinks()
vtv.get_articles_link().to_csv(file_name='VTV_link.csv')

thanhnien = ThanhNienNewsLinks()
thanhnien.get_articles_link().to_csv(file_name='ThanhNien_link.csv')

vnexpress = VnExpressNewsLink()
vnexpress.get_articles_link().to_csv(file_name='VNExpress_link.csv')

