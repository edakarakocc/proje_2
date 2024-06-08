from personel import Personel #Personel sınıfını içe aktarır

class Hemsire(Personel): #Personel sınıfından miras alır
    def __init__(self, personel_no, ad, soyad, departman, maas, calisma_saati, sertifika, hastane): #Hemsire sınıfının başlatıcı metodu
        super().__init__(personel_no, ad, soyad, departman, maas) 
        self.__calisma_saati = calisma_saati
        self.__sertifika = sertifika
        self.__hastane = hastane
    
    def get_calisma_saati(self): #calisma_saati değişkenini döndürür (getter metodu)
        return self.__calisma_saati
    def set_calisma_saati(self, calisma_saati): #calisma_saati değişkenini ayarlar (setter metodu)
        self.__calisma_saati = calisma_saati
    
    def get_sertifika(self): #sertifika değişkenini döndürür (getter metodu)
        return self.__sertifika
    def set_sertifika(self,sertifika): #sertifika değişkenini ayarlar (setter metodu)
        self.__sertifika = sertifika
    
    def get_hastane(self): #hastane değişkenini döndürür (getter metodu)
        return self.__hastane
    def set_hastane(self,hastane): #hastane değişkenini ayarlar (setter metodu)
        self.__hastane = hastane
    
    def __str__(self): #hemsire_bilgi değişkenini ekrana yazdırır (__str__: ekrana yazdırma metodu)
        hemsire_bilgi = super().__str__() + f", Çalışma Saati: {self.__calisma_saati}, Sertifika: {self.__sertifika}, Hastaen: {self.__hastane}"
        return hemsire_bilgi
    
    def maas_arttir(self, oran): #Belirli bir oranda maaşı arttırmak için oluşturulan metot
        prim = self.get_maas() * (self.__calisma_saati/10) #Hemşirenin çalıştığı her saat başına maaşının 1/10'u kadar prim almasını sağlar
        zamli_maas = self.get_maas() + self.get_maas()* (oran/ 100) + prim #Maaşa belirli bir oranda zam yaparak prim miktarını üzerine ekler ve maaşı arttırır
        self.set_maas(zamli_maas) #Yeni maaşı, eski maaşın zamlı hali değiştirir
    