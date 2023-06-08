from urllib.request import urlopen

f = urlopen("https://youtube.com/") # urlopen URLを開く（HTTPResponseHTTPResponse型のオブジェクトで返す）
read = f.read()

print(type(f))

# HTTPヘッダーの`Content-Type`の値を取得します Content-Type=メディア種別
read2 = f.getheader("Content-Type")
print(read2)

# info()で`HTTPMessage型`オブジェクトを取得 infoメソッドはHTTPMessage型のオブジェクトを返します。
# get_content_charset()で`charset`を取得 オブジェクトからget_content_charsetメソッドでcharsetを取得します。
# 引数の`failobj=`はcharsetが指定されていない場合のエンコーディングを指定
encoding = f.info().get_content_charset(failobj="utf-8")
print(encoding)
