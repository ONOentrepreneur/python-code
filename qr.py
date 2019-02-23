import qrcode
#QRコードを生成
img=qrcode.make("http://kujirahand.com/wiki/")
#ファイルに保存
img.save("http://kujirahand.com/wiki/")
