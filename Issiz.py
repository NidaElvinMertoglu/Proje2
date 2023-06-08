from Insan import Insan

class Issiz(Insan):
    def __init__(self, ad, soyad, yas, cinsiyet, uyruk, tecrube_dict):
        
        super().__init__("", ad, soyad, yas, cinsiyet, uyruk)
        self.__tecrube_dict = tecrube_dict
        self.__en_uygun_statu = self.statu_bul()