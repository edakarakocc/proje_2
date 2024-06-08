from personel import Personel #Personel sınıfını içe aktarır

class Doktor(Personel): #Personel sınıfından miras alır
    def __init__(self, personel_no, ad, soyad, departman, maas,uzmanlik,deneyim_yili,hastane): #Doktor sınıfının başlatıcı metodu
        super().__init__(personel_no, ad, soyad, departman, maas)
        self.__uzmanlik = uzmanlik
        self.__deneyim_yili = deneyim_yili
        self.__hastane = hastane
    
    def get_uzmanlik(self): #uzmanlik değişkenini döndürür (getter metodu)
        return self.__uzmanlik
    def set_uzmanlik(self,uzmanlik): #uzmanlik değişkenini ayarlar (setter metodu)
        self.__uzmanlik = uzmanlik
    
    def get_deneyim_yili(self): #deneyim_yili değişkenini döndürür (getter metodu)
        return self.__deneyim_yili
    def set_deneyim_yili(self,deneyim_yili): #deneyim_yili değişkenini ayarlar (setter metodu)
        self.__deneyim_yili = deneyim_yili
        
    def get_hastane(self): #hastane değişkenini döndürür (getter metodu)
        return self.__hastane
    def set_hastane(self,hastane): #hastane değişkenini ayarlar (setter metodu)
        self.__hastane = hastane
        
    def __str__(self): #doktor_bilgi değişkenini ekrana yazdırır (__str__: ekrana yazdırma metodu)
        doktor_bilgi = super().__str__() + f", Uzmanlık Alanı: {self.__uzmanlik}, Deneyim Yılı: {self.__deneyim_yili}, Hastane: {self.__hastane}"
        return doktor_bilgi
    
    def maas_arttir(self,oran): #Belirli bir oranda maaşı arttırmak için oluşturulan metot
        prim = self.get_maas() * (self.__deneyim_yili/10) #Doktorun çalıştığı her yıl için maaşının 1/10'u kadar prim almasını sağlar
        zamli_maas = self.get_maas() + self.get_maas() * (oran/100) + prim #Maaşa belirli bir oranda zam yaparak prim miktarını üzerine ekler ve maaşı arttırır
        self.set_maas(zamli_maas) #Yeni maaşı, eski maaşın zamlı hali değiştirir
    
        