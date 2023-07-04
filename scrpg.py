import requests
from bs4 import BeautifulSoup
import time
import win32com.client
import datetime

def html_perse(url):
    time.sleep(1)   
    proxies_dic = {
        "http":"//XXX.co.jp:0000",       # proxyサーバ
        "https":"//XXX.co.jp:0000"
    }
    html = requests.get(url,proxies=proxies_dic)    #Webから取得
    return BeautifulSoup(html.content, 'html.parser')   #html.perser要素を抽出

def weather(url):
    soup = html_perse(url)
    current_weather = soup.select_one("[class='weather-now__ul']")  #class weather-now__ulを抽出
    current_li = current_weather.find_all('li') #18行目で抽出した文字列から'li'を抽出
    text_list = []
    for value in current_li:
        text = value.text.strip()   #空白文字を削除し、textに代入
        text_list.append(text)  #text_list[]に代入
    return text_list

def send_mail(list):
    outlook = win32com.client.Dispatch("Outlook.Application")   #pythonからOutlookを起動
    mail = outlook.CreateItem(0)     #MailItemオブジェクトのID
    mail.to = 'XXX@xxx.co.jp'   #宛先アドレス
    mail.subject = '件名'    #件名
    mail.bodyFormat = 1     #3種の本文テキスト形式 (テキスト形式, リッチテキスト形式, HTML形式)
    now = datetime.datetime.now()   #今日の日付を取得
    dt_now = now.strftime('%Y/%m/%d %H:%M:%S')  #取得した日付の形式設定
    #メールの本文
    mail.body = """天気予報：TEST""" + "¥n" + dt_now + "¥n" + list[0] + "¥n" + list[1] + "¥n" + list[2] + "¥n" + list[3] + "¥n" + list[4] + "¥n" + list[5] + "¥n"
    mail.Display(True)  #Displayで開くか True or False
    mail.Send()     #メールを送信

if __name__ == '__main__':
    url = 'https://weathernews.jp/onebox/tenki/tokyo/13113/'
    time.sleep(1)   #１秒待機
    send_mail(weather(url))