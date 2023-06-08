from Insan import Insan

class Issiz(Insan):
    def __init__(self, ad, soyad, yas, cinsiyet, uyruk, tecrube_dict):

        super().__init__("", ad, soyad, yas, cinsiyet, uyruk)
        self.__tecrube_dict = tecrube_dict
        self.__en_uygun_statu = self.statu_bul()

    def get_tecrube_dict(self):
        return self.__tecrube_dict

    def set_tecrube_dict(self, tecrube_dict):
        self.__tecrube_dict = tecrube_dict
        self.__en_uygun_statu = self.statu_bul()

    def get_en_uygun_statu(self):
        return self.__en_uygun_statu