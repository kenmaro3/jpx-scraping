import time
import requests
from bs4 import BeautifulSoup
import pandas as pd


if __name__ == "__main__":
    print("hello, world!")
    # scrape following url
    url = "https://www.jpx.co.jp/listing/stocks/new/00-archives-04.html"
    res = requests.get(url)
    soup = BeautifulSoup(res.content, "html.parser")
    tbody = soup.select("#readArea > div:nth-child(4) > div > table:nth-child(1) > tbody")
    trs = tbody[0].find_all("tr")

    res_list = []
    for i, tr in enumerate(trs):
        print(f"{i} / {len(trs)}")
        try:
            tds = tr.find_all("td")
            flag = i%2
            if i%2 == 0:
                data_dict = {}

                date = tds[0].text
                date = date.split(" ")[0]
                date = date.split("\n")[0]
                date = date.split("\r")[0]
                #print("date", date)

                name = tds[1]
                name = name.find("a").text
                name = name.split("\x89")[-1]

                code = tds[2].text
                code = code.split("\n")[2]


                detail_url = f"https://finance.yahoo.co.jp/quote/{code}.T"
                res = requests.get(detail_url)
                soup = BeautifulSoup(res.text, "html.parser")
                current_price = soup.select("#detail > section._2FGOdR4R._1cK2V1oI > div > ul > li:nth-child(1) > dl > dd > span._1fofaCjs._2aohzPlv._1DMRub9m > span > span")[0].text
                current_price = current_price.replace(",", "")
                current_price = int(current_price)
                #print("current_price", current_price)

                data_dict["date"] = date
                data_dict["name"] = name
                data_dict["current_price"] = current_price
            
            else:
                place = tds[0].text
                initial_price = tds[3].text
                initial_price = initial_price.replace(",", "")
                initial_price = int(initial_price)
                #print("initial_price", initial_price)
                data_dict["place"] = place
                data_dict["initial_price"] = initial_price
                print("data_dict", data_dict)
                res_list.append(data_dict)


        except:
            print("except")
            pass


    df = pd.json_normalize(res_list)
    df.to_csv('data.csv', index=False, encoding='utf-8')




    # detail_url = f"https://quote.jpx.co.jp/jpx/template/quote.cgi?F=tmp/stock_detail&MKTN=T&QCODE={code}"
    # print(detail_url)

    # flag = True
    # count = 0
    # while flag: 
    #     res = requests.get(detail_url)

    #     time.sleep(2)
    #     print("res.status_code", res.status_code)
    #     status_code = res.status_code
    #     if status_code != 500:
    #         flag  = False
    #     count += 1
    #     if count > 5:
    #         break
    # quit()