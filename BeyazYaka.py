from Calisan import Calisan


class BeyazYaka(Calisan):
    def __init__(self, tc_no, ad, soyad, yas, cinsiyet, uyruk, sektor, tecrube, maas, tesvik_primi):
        super().__init__(tc_no, ad, soyad, yas, cinsiyet, uyruk, sektor, tecrube, maas)

        self.__tesvik_primi = tesvik_primi

    def get_tesvik_primi(self):
        return self.__tesvik_primi

    def set_tesvik_primi(self, tesvik_primi):
        self.__tesvik_primi = tesvik_primi

    def get_yeni_maas(self):
        return super().get_yeni_maas() + self.__tesvik_primi

    def __uygun_statu(self):
        return "Beyaz Yaka"

    def zam_hakki(self):
        if self.get_tecrube() <= 2:
            return 0
        elif 2 < self.get_tecrube() <= 4 and self.get_maas() < 15000:
            return (self.get_maas() * self.get_tecrube() / 100) + self.__tesvik_primi
        elif self.get_tecrube() > 4 and self.get_maas() < 25000:
            return (self.get_maas() * self.get_tecrube() * 4 / 100) + self.__tesvik_primi
        else:
            return 0