from Insan import Insan

class Calisan(Insan):
    def __init__(self, tc_no, ad, soyad, yas, cinsiyet, uyruk, sektor, tecrube, maas):
        super().__init__(tc_no, ad, soyad, yas, cinsiyet, uyruk)

        self.__sektor = sektor
        self.__tecrube = tecrube
        self.__maas = maas

    def get_sektor(self):
        return self.__sektor

    def set_sektor(self, sektor):
        self.__sektor = sektor

    def get_tecrube(self):
        return self.__tecrube

    def set_tecrube(self, tecrube):
        self.__tecrube = tecrube

    def get_maas(self):
        return self.__maas

    def set_maas(self, maas):
        self.__maas = maas

    def get_yeni_maas(self):
        try:
            zam_orani = self.zam_hakki()
            return self.__maas + zam_orani
        except Exception as e:
            print(f"Error occurred while calculating new salary: {e}")
            return None

    def __uygun_statu(self):
        pass

    def zam_hakki(self):
        try:
            if self.__tecrube < 2:
                return 0
            elif 2 <= self.__tecrube <= 4 and self.__maas < 15000:
                return self.__maas * (self.__tecrube / 100)
            elif self.__tecrube > 4 and self.__maas < 25000:
                return (self.__maas * self.__tecrube) / 200
        except Exception as e:
            print(f"Error occurred while calculating salary increase: {e}")
            return None