import json

import scrapy
from scrapy.crawler import CrawlerProcess


class LazadaSpider(scrapy.Spider):
    name = 'lazada'

    headers = {
        'authority': 'acs-m.lazada.co.id',
        'accept': 'application/json',
        'accept-language': 'mn,en;q=0.9',
        'cache-control': 'no-cache',
        'content-type': 'application/x-www-form-urlencoded',
        'cookie': 't_fv=1669041630363; t_uid=ZvRXmFdlA493NeHrMs4uovAibxdv7Njg; cna=l/HJGp0nK1ECAco3vCz3rBL1; hng=ID|id-ID|IDR|360; hng.sig=to18pG508Hzz7EPB_okhuQu8kDUP3TDmLlnu4IbIOY8; lzd_cid=9c3dd7ec-7e7c-4c48-c4f0-66e17b3c6f6b; xlly_s=1; t_sid=mFWIP23I50M5LLoGUCSdG6RHCD8vYBuA; utm_channel=NA; _m_h5_tk=e4b67e6226190de40d96c3e75a4d8180_1669354746694; _m_h5_tk_enc=93a1769c22118b768ed1075f14d4b452; lzd_sid=169b2301feee712dd6e6cca16f51ebb1; _tb_token_=e73e3ee78e3e6; isg=BBcXNZ8QOO6CAbyZ1KntdIs8poJhXOu-ikAahWlF7OZdmDbadSyqDm35-jCGcMM2; l=eBMqxti7TcC1QAFKBO5anurza77O4Idb8sPzaNbMiInca1k1MeGMXNCFMaxpydtj_t5f4FtruS5yBdneJJzLyFkDBeYClCmLHwJM8e1..; tfstk=cloCBPx9B-VwdgtlxW9wajBD8yq1ay6bFeNndBG9MqVWlNwL6sbR0Sglv4f848e1.',
        'entrance': '',
        'origin': 'https://www.lazada.co.id',
        'pragma': 'no-cache',
        'referer': 'https://www.lazada.co.id/',
        'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Linux"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
        'x-i18n-language': 'id',
        'x-i18n-regionid': 'ID',
    }
    data = 'data=%7B%22deviceType%22%3A%22pc%22%2C%22path%22%3A%22https%3A%2F%2Fwww.lazada.co.id%2Fproducts%2Fadera-darkspot-anti-aging-serum-penghilang-flek-hitam-serum-pencerah-wajah-pria-wanita-pengencang-kulit-mencegah-penuaan-dini-dark-spot-serum-100-original-bpom-i6562360210.html%3Fspm%3Da2o4j.searchlistcategory.list.1.75f3a620E9FptQ%22%2C%22uri%22%3A%22adera-darkspot-anti-aging-serum-penghilang-flek-hitam-serum-pencerah-wajah-pria-wanita-pengencang-kulit-mencegah-penuaan-dini-dark-spot-serum-100-original-bpom-i6562360210%22%2C%22headerParams%22%3A%22%7B%5C%22user-agent%5C%22%3A%5C%22Mozilla%2F5.0%20(X11%3B%20Linux%20x86_64)%20AppleWebKit%2F537.36%20(KHTML%2C%20like%20Gecko)%20Chrome%2F107.0.0.0%20Safari%2F537.36%5C%22%7D%22%2C%22cookieParams%22%3A%22%7B%5C%22_uab_collina%5C%22%3A%5C%22166904164092123795363815%5C%22%2C%5C%22__wpkreporterwid_%5C%22%3A%5C%222790869f-1f4d-4a48-a890-e8e6d7fad227%5C%22%2C%5C%22t_fv%5C%22%3A%5C%221669041630363%5C%22%2C%5C%22t_uid%5C%22%3A%5C%22ZvRXmFdlA493NeHrMs4uovAibxdv7Njg%5C%22%2C%5C%22cna%5C%22%3A%5C%22l%2FHJGp0nK1ECAco3vCz3rBL1%5C%22%2C%5C%22hng%5C%22%3A%5C%22ID%7Cid-ID%7CIDR%7C360%5C%22%2C%5C%22hng.sig%5C%22%3A%5C%22to18pG508Hzz7EPB_okhuQu8kDUP3TDmLlnu4IbIOY8%5C%22%2C%5C%22lzd_cid%5C%22%3A%5C%229c3dd7ec-7e7c-4c48-c4f0-66e17b3c6f6b%5C%22%2C%5C%22_bl_uid%5C%22%3A%5C%22s2lwgaC1qvwwO7a7ztqUf7n54XR5%5C%22%2C%5C%22xlly_s%5C%22%3A%5C%221%5C%22%2C%5C%22t_sid%5C%22%3A%5C%22mFWIP23I50M5LLoGUCSdG6RHCD8vYBuA%5C%22%2C%5C%22utm_channel%5C%22%3A%5C%22NA%5C%22%2C%5C%22_m_h5_tk%5C%22%3A%5C%22e4b67e6226190de40d96c3e75a4d8180_1669354746694%5C%22%2C%5C%22_m_h5_tk_enc%5C%22%3A%5C%2293a1769c22118b768ed1075f14d4b452%5C%22%2C%5C%22lzd_sid%5C%22%3A%5C%22169b2301feee712dd6e6cca16f51ebb1%5C%22%2C%5C%22_tb_token_%5C%22%3A%5C%22e73e3ee78e3e6%5C%22%2C%5C%22isg%5C%22%3A%5C%22BBcXNZ8QOO6CAbyZ1KntdIs8poJhXOu-ikAahWlF7OZdmDbadSyqDm35-jCGcMM2%5C%22%2C%5C%22l%5C%22%3A%5C%22eBMqxti7TcC1QAFKBO5anurza77O4Idb8sPzaNbMiInca1k1MeGMXNCFMaxpydtj_t5f4FtruS5yBdneJJzLyFkDBeYClCmLHwJM8e1..%5C%22%2C%5C%22tfstk%5C%22%3A%5C%22cloCBPx9B-VwdgtlxW9wajBD8yq1ay6bFeNndBG9MqVWlNwL6sbR0Sglv4f848e1.%5C%22%7D%22%2C%22requestParams%22%3A%22%7B%5C%22spm%5C%22%3A%5C%22a2o4j.searchlistcategory.list.1.75f3a620E9FptQ%5C%22%7D%22%7D'

    custom_settings = {
        'COOKIES_ENABLED': False
    }

    def start_requests(self):
        yield scrapy.Request(
            url='https://acs-m.lazada.co.id/h5/mtop.global.detail.web.getdetailinfo/1.0/?jsv=2.5.1&appKey=24677475&t=1669347171969&sign=0c585a826266d810b30474a62ffa7002&api=mtop.global.detail.web.getDetailInfo&v=1.0&type=originaljson&isSec=1&AntiCreep=true&timeout=20000&dataType=json&sessionOption=AutoLoginOnly&x-i18n-language=id&x-i18n-regionID=ID',
            method='POST',
            headers=self.headers,
            body=self.data,
            callback=self.parse
        )

    def parse(self, response):
        # print(response.json())
        resp = json.loads(response.json()["data"]["module"])
        comments = resp["review"]["reviews"]
        results = []
        for comment in comments:
            results.append(
                {"Title": comment["reviewer"], "description": comment["reviewContent"], "rating": comment["rating"],
                 "date": comment["reviewTime"]})

        print(json.dumps(results, indent=4))

if __name__ == '__main__':
    process = CrawlerProcess()
    process.crawl(LazadaSpider)
    process.start()
