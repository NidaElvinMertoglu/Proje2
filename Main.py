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