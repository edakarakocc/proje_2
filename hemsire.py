from personel import Personel

class Hemsire(Personel):
    def __init__(self, personel_no, ad, soyad, departman, maas, calisma_saati, sertifika, hastane):
        super().__init__(personel_no, ad, soyad, departman, maas)
        self.__calisma_saati = calisma_saati
        self.__sertifika = sertifika
        self.__hastane = hastane
    
    def get_calisma_saati(self):
        return self.__calisma_saati
    def set_calisma_saati(self, calisma_saati):
        self.__calisma_saati = calisma_saati
    
    def get_sertifika(self):
        return self.__sertifika
    def set_sertifika(self,sertifika):
        self.__sertifika = sertifika
    
    def get_hastane(self):
        return self.__hastane
    def set_hastane(self,hastane):
        self.__hastane = hastane
    
    def __str__(self):
        hemsire_bilgi = super().__str__() + f", Çalışma Saati: {self.__calisma_saati}, Sertifika: {self.__sertifika}, Hastaen: {self.__hastane}"
        return hemsire_bilgi
    
    def maas_arttir(self, oran):
        prim = self.get_maas() * (self.__calisma_saati/10)
        zamli_maas = self.get_maas() + self.get_maas()* (oran/ 100) + prim
        self.set_maas(zamli_maas)
    