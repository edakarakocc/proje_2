class Hasta:
    def __init__(self, hasta_no, ad, soyad, dogum_tarihi, hastalik, tedavi, doktor=None, hemsire= None): #Hasta sınıfının yapıcı metodu
        self.__hasta_no = hasta_no
        self.__ad = ad
        self.__soyad = soyad
        self.__dogum_tarihi = dogum_tarihi
        self.__hastalik = hastalik
        self.__tedavi = tedavi
        self.__doktor = doktor
        self.__hemsire = hemsire
    
    def get_hasta_no(self): #hasta_no değişkenini döndürür (getter metodu)
        return self.__hasta_no
    def set_hasta_no(self,hasta_no): #hast_no değişkenini ayarlar (setter metodu)
        self.__hasta_no = hasta_no
    
    def get_ad(self): #ad değişkenini döndürür (getter metodu)
        return self.__ad
    def set_ad(self,ad): #ad değişkenini ayarlar (setter metodu)
        self.__ad = ad

    def get_soyad(self): #soyad değişkenini döndürür (getter metodu)
        return self.__soyad
    def set_soyad(self,soyad): #soyad değişkenini ayarlar (setter metodu)
        self.__soyad = soyad   
        
    def get_dogum_tarihi(self): #dogum_tarihi değişkenini döndürür (getter metodu)
        return self.__dogum_tarihi
    def set_dogum_tarihi(self,dogum_tarihi): #dogum_tarihi değişkenini ayarlar (setter metodu)
        self.__dogum_tarihi = dogum_tarihi
    
    def get_hastalik(self): #hastalik değişkenini döndürür (getter metodu)
        return self.__hastalik
    def set_hastalik(self,hastalik): #hastalik değişkenini ayarlar (setter metodu)
        self.__hastalik = hastalik
        
    def get_tedavi(self): #tedavi değişkenini döndürür (getter metodu)
        return self.__tedavi
    def set_tedavi(self,tedavi): #tedavi değişkenini ayarlar (setter metodu)
        self.__tedavi = tedavi
    
    def get_doktor(self): #doktor değişkenini döndürür (getter metodu)
        return self.__doktor
    def set_doktor(self, doktor): #doktor değişkenini ayarlar (setter metodu)
        self.__doktor = doktor

    def get_hemsire(self): #hemsire değişkenini döndürür (getter metodu)
        return self.__hemsire
    def set_hemsire(self, hemsire): #hemsire değişkenini ayarlar (setter metodu)
        self.__hemsire = hemsire 
    
    def tedavi_suresi_hesapla(self): #Hastanın tedavi süresini hesaplamak için oluşturulan metot
        if self.__tedavi:
            tedavi_suresi = len(self.__tedavi) * 5 #Tedavi adının uzunluğunu 5 ile çarparak tedavi süresini hesaplar ve o değeri döndürür
            return tedavi_suresi
        else:
            return None
    
    def __str__(self): #hasta_bilgi değişkenini ve eğer varsa tedavi_suresi değişkenini ekrana yazdırır (__str__: ekrana yazdırma metodu)
        tedavi_suresi = self.tedavi_suresi_hesapla()
        hasta_bilgi = f"Hasta no: {self.__hasta_no}, Hasta Adı: {self.__ad}, Hasta Soyadı: {self.__soyad}, Doğum Tarihi: {self.__dogum_tarihi}, Hastalık: {self.__hastalik}, Tedavi: {self.__tedavi}"
        if tedavi_suresi:
            hasta_bilgi += f", Tedavi Süresi: {tedavi_suresi} Gün"
        if self.__doktor:
            hasta_bilgi += f", Doktor: {self.__doktor.get_ad()}{self.__doktor.get_soyad()}"
        if self.__hemsire:
            hasta_bilgi += f", Hemşire: {self.__hemsire.get_ad()}{self.__hemsire.get_soyad()}"
        return hasta_bilgi
                
        