class Hasta:
    def __init__(self, hasta_no, ad, soyad, dogum_tarihi, hastalik, tedavi, doktor=None, hemsire= None):
        self.__hasta_no = hasta_no
        self.__ad = ad
        self.__soyad = soyad
        self.__dogum_tarihi = dogum_tarihi
        self.__hastalik = hastalik
        self.__tedavi = tedavi
        self.__doktor = doktor
        self.__hemsire = hemsire
    
    def get_hasta_no(self):
        return self.__hasta_no
    def set_hasta_no(self,hasta_no):
        self.__hasta_no = hasta_no
    
    def get_ad(self):
        return self.__ad
    def set_ad(self,ad):
        self.__ad = ad

    def get_soyad(self):
        return self.__soyad
    def set_soyad(self,soyad):
        self.__soyad = soyad   
        
    def get_dogum_tarihi(self):
        return self.__dogum_tarihi
    def set_dogum_tarihi(self,dogum_tarihi):
        self.__dogum_tarihi = dogum_tarihi
    
    def get_hastalik(self):
        return self.__hastalik
    def set_hastalik(self,hastalik):
        self.__hastalik = hastalik
        
    def get_tedavi(self):
        return self.__tedavi
    def set_tedavi(self,tedavi):
        self.__tedavi = tedavi
    
    def get_doktor(self):
        return self.__doktor
    def set_doktor(self, doktor):
        self.__doktor = doktor

    def get_hemsire(self):
        return self.__hemsire
    def set_hemsire(self, hemsire):
        self.__hemsire = hemsire 
    
    def tedavi_suresi_hesapla(self):    
        if self.__tedavi:
            tedavi_suresi = len(self.__tedavi) * 5
            return tedavi_suresi
        else:
            return None
    
    def __str__(self):
        tedavi_suresi = self.tedavi_suresi_hesapla()
        hasta_bilgi = f"Hasta no: {self.__hasta_no}, Hasta Adı: {self.__ad}, Hasta Soyadı: {self.__soyad}, Doğum Tarihi: {self.__dogum_tarihi}, Hastalık: {self.__hastalik}, Tedavi: {self.__tedavi}"
        if tedavi_suresi:
            hasta_bilgi += f", Tedavi Süresi: {tedavi_suresi} Gün"
        if self.__doktor:
            hasta_bilgi += f", Doktor: {self.__doktor.get_ad()}{self.__doktor.get_soyad()}"
        if self.__hemsire:
            hasta_bilgi += f", Hemşire: {self.__hemsire.get_ad()}{self.__hemsire.get_soyad()}"
        return hasta_bilgi
                
        