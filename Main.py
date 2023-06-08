from Insan import Insan
from Issiz import Issiz
from Calisan import Calisan
from MaviYaka import MaviYaka
from BeyazYaka import BeyazYaka
import pandas as pd

insan1 = Insan("12345678900", "Nira", "Saat", 30, "Kadın", "Turk")
insan2 = Insan("98765432109", "Alexander", "Hamilton", 25, "Erkek", "Amerikali")
print(str(insan1))

issiz1 = Issiz("Johnny", "Deer", 30, "Erkek", "Amerikali", {"mavi yaka": 3, "beyaz yaka": 6, "yonetici": 2})
issiz2 = Issiz("Canute", "Forkbeard", 25, "Erkek", "Danimarkali", {"mavi yaka": 1, "beyaz yaka": 2, "yonetici": 8})
issiz3 = Issiz("Jolyne", "Smith", 29, "Kadin", "Amerikali", {"mavi yaka": 8, "beyaz yaka": 2, "yonetici": 0})
print(str(issiz1))
print(str(issiz2))
print(str(issiz3))

calisan1 = Calisan("", "Emma", "Stone", 30, "Kadin", "Amerikali", "teknoloji", 5, 15000)
calisan2 = Calisan("", "Thorfinn", "Karslefni", 26, "Erkek", "Izlandali", "insaat", 5, 2000)
calisan3 = Calisan("", "Bruno", "Ale", 36, "Erkek", "Italyan", "muhasebe", 26, 8000)
print(str(calisan1))
print(str(calisan2))
print(str(calisan3))

maviyaka1 = MaviYaka("14984893834", "Harry", "Brown", 25, "Erkek", "Amerikali", "teknoloji", 27, 5000, 0.2)
maviyaka2 = MaviYaka("29303978666", "Thors", "Knutson", 28, "Erkek", "Izlandali", "insaat", 5, 2000, 0.5)
maviyaka3 = MaviYaka("44585666657", "Meralda", "Guido", 37, "Kadin", "Italyan", "muhasebe", 56, 4000, 0.5)
print(str(maviyaka1))
print(str(maviyaka2))
print(str(maviyaka3))

beyazyaka1 = BeyazYaka("12345678909", "Melek", "Kaya", 30, "Kadin", "Turk", "teknoloji", 37, 25000, 2500)
beyazyaka2 = BeyazYaka("16665688882", "Aaron", "Diaz", 33, "Erkek", "Ispanyol", "muhasebe", 15, 14000, 500)
beyazyaka3 = BeyazYaka("15545667894", "Kiryu", "Yamazaki", 34, "Erkek", "Japon", "insaat", 25, 9000, 2500)
print(str(beyazyaka1))
print(str(beyazyaka2))
print(str(beyazyaka3))

pd.set_option('display.max_columns',13)
pd.set_option('display.max_rows',13)

# DataFrame icin data sozlugu olusturulması
data = {
    "Nesne": ["Calisan", "Mavi Yaka", "Beyaz Yaka", "Calisan", "Mavi Yaka", "Beyaz Yaka", "Calisan", "Mavi Yaka", "Beyaz Yaka"],
    "Tc No": [calisan1.get_tc_no(), maviyaka1.get_tc_no(), beyazyaka1.get_tc_no(), calisan2.get_tc_no(), maviyaka2.get_tc_no(), beyazyaka2.get_tc_no(), calisan3.get_tc_no(), maviyaka3.get_tc_no(), beyazyaka3.get_tc_no()],
    "Ad": [calisan1.get_ad(), maviyaka1.get_ad(), beyazyaka1.get_ad(), calisan2.get_ad(), maviyaka2.get_ad(), beyazyaka2.get_ad(), calisan3.get_ad(), maviyaka3.get_ad(), beyazyaka3.get_ad()],
    "Soyad": [calisan1.get_soyad(), maviyaka1.get_soyad(), beyazyaka1.get_soyad(), calisan2.get_soyad(), maviyaka2.get_soyad(), beyazyaka2.get_soyad(), calisan3.get_soyad(), maviyaka3.get_soyad(), beyazyaka3.get_soyad()],
    "Yas": [calisan1.get_yas(), maviyaka1.get_yas(), beyazyaka1.get_yas(), calisan2.get_yas(), maviyaka2.get_yas(), beyazyaka2.get_yas(), calisan3.get_yas(), maviyaka3.get_yas(), beyazyaka3.get_yas()],
    "Cinsiyet": [calisan1.get_cinsiyet(), maviyaka1.get_cinsiyet(), beyazyaka1.get_cinsiyet(), calisan2.get_cinsiyet(), maviyaka2.get_cinsiyet(), beyazyaka2.get_cinsiyet(), calisan3.get_cinsiyet(), maviyaka3.get_cinsiyet(), beyazyaka3.get_cinsiyet()],
    "Uyruk": [calisan1.get_uyruk(), maviyaka1.get_uyruk(), beyazyaka1.get_uyruk(), calisan2.get_uyruk(), maviyaka2.get_uyruk(), beyazyaka2.get_uyruk(), calisan3.get_uyruk(), maviyaka3.get_uyruk(), beyazyaka3.get_uyruk()],
    "Sektor": [calisan1.get_sektor(), maviyaka1.get_sektor(), beyazyaka1.get_sektor(), calisan2.get_sektor(), maviyaka2.get_sektor(), beyazyaka2.get_sektor(), calisan3.get_sektor(), maviyaka3.get_sektor(), beyazyaka3.get_sektor()],
    "Tecrube": [calisan1.get_tecrube(), maviyaka1.get_tecrube(), beyazyaka1.get_tecrube(), calisan2.get_tecrube(), maviyaka2.get_tecrube(), beyazyaka2.get_tecrube(), calisan3.get_tecrube(), maviyaka3.get_tecrube(), beyazyaka3.get_tecrube()],
    "Maas": [calisan1.get_maas(), maviyaka1.get_maas(), beyazyaka1.get_maas(), calisan2.get_maas(), maviyaka2.get_maas(), beyazyaka2.get_maas(), calisan3.get_maas(), maviyaka3.get_maas(), beyazyaka3.get_maas()],
    "Yipranma Payi": [0, maviyaka1.get_yipranma_payi(), 0, 0, maviyaka2.get_yipranma_payi(), 0, 0, maviyaka3.get_yipranma_payi(), 0],
    "Tesvik Prim": [0, 0, beyazyaka1.get_tesvik_primi(), 0, 0, beyazyaka2.get_tesvik_primi(), 0, 0, beyazyaka3.get_tesvik_primi()],
    "Yeni Maas": [calisan1.get_yeni_maas(), maviyaka1.get_yeni_maas(), beyazyaka1.get_yeni_maas(), calisan2.get_yeni_maas(), maviyaka2.get_yeni_maas(), beyazyaka2.get_yeni_maas(), calisan3.get_yeni_maas(), maviyaka3.get_yeni_maas(), beyazyaka3.get_yeni_maas()],
}


df = pd.DataFrame(data)
print(df)