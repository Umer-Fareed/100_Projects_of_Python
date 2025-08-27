import requests
from bs4 import BeautifulSoup
import lxml

url= ("https://www.amazon.com/BERIBES-Bluetooth-Headphones-Microphone-Lightweight/dp/B09LYF2ST7/ref=sr_1_1?_encoding=UTF8&content-id=amzn1.sym.f0670b1b-e1fd-4c67-a2b1-b8a347243628&dib=eyJ2IjoiMSJ9.Pfix3I77yjMkN8wajdeQJx6zpcL_ntk5tWSLbZ9poiwejcBbvBRPf_mxiZXHdpxu2-Nt4r_yZ5D1zB74x_VpaSF31oaJ1zAmAvfOp8-lb5C0N3COdbo3M5NP8rmB4aTTUj3AjcIOn2Q4gSrjCPBqChVz8GibMQIPx2S-nj_z7BKsYve-ZoW1YrpHPlRX-cXaPBPqhQM-8W2CcE2MVrZxCAtdpan_Pd6Fwb0_kEh_mZw.zg60PqGhpTGBEvRlsn14peLLS_FCA6QI5zLERrBqUOE&dib_tag=se&keywords=headphones&pd_rd_r=f2462602-0057-4d0b-a766-2731ed004091&pd_rd_w=tC7jA&pd_rd_wg=2YlL8&qid=1756293866&sr=8-1&th=1")
header= {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
}
response = requests.get(url, headers=header)
print(response.status_code)
"""
soup = BeautifulSoup(response.content, "lxml")
print(soup.prettify())

price = soup.find(class_="a-offscreen").get_text()
price_without_currency = price.split("$")[1]
price_as_float = float(price_without_currency)
print(price_as_float)

import smtplib

title = soup.find(id="productTitle").get_text().strip()
print(title)

BUY_PRICE = 200

if price_as_float < BUY_PRICE:
    message = f"{title} is now {price}"

    with smtplib.SMTP(YOUR_SMTP_ADDRESS, port=587) as connection:
        connection.starttls()
        result = connection.login(YOUR_EMAIL, YOUR_PASSWORD)
        connection.sendmail(
            from_addr=YOUR_EMAIL,
            to_addrs=YOUR_EMAIL,
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{url}".encode("utf-8")
        )
"""
