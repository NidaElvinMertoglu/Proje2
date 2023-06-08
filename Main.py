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