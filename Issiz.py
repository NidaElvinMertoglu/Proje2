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

    def statu_bul(self):
        try:
            max_effect = 0
            en_uygun_statu = None
            for statu, tecrube in self.__tecrube_dict.items():
                effect = 0
                if statu == "mavi yaka":
                    effect = tecrube * 0.20
                elif statu == "beyaz yaka":
                    effect = tecrube * 0.35
                elif statu == "yonetici":
                    effect = tecrube * 0.45

                if effect > max_effect:
                    max_effect = effect
                    en_uygun_statu = statu

            return en_uygun_statu
        except Exception as e:
            print(f"An error occurred while determining the most suitable status: {str(e)}")
            return None

    def __str__(self):
        return super().__str__() + f"Tecrubeler: {self.__tecrube_dict}\nEn Uygun Statu: {self.get_en_uygun_statu()}\n"
    