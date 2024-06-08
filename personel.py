class Personel:
    def __init__(self,personel_no,ad,soyad,departman,maas): #Personel sınıfının yapıcı metodu
        self.__personel_no = personel_no
        self.__ad = ad
        self.__soyad = soyad
        self.__departman = departman
        self.__maas = maas
    
    def get_personel_no(self): #personel_no değişkenini döndürür (getter metodu)
        return self.__personel_no
    def set_personel_no(self,personel_no): #personel_no değişkenini ayarlar (setter metodu)
        self.__personel_no = personel_no
    
    def get_ad(self): #ad değişkenini döndürür (getter metodu)
        return self.__ad
    def set_ad(self,ad): #ad değişkenini ayarlar (setter metodu)
        self.__ad = ad

    def get_soyad(self): #soyad değişkenini döndürür (getter metodu)
        return self.__soyad
    def set_soyad(self,soyad): #soyad değişkenini ayarlar (setter metodu)
        self.__soyad = soyad

    def get_departman(self): #departman değişkenini döndürür (getter metodu)
        return self.__departman
    def set_departman(self,departman): #departman değişkenini ayarlar (setter metodu)
        self.__departman = departman    

    def get_maas(self): #maas değişkenini döndürür (getter metodu)
        return self.__maas
    def set_maas(self,maas): #maas değişkenini ayarlar (setter metodu)
        self.__maas = maas
        
    def __str__(self): #personel_bilgi değişkenini ekrana yazdırır (__str__: ekrana yazdırma metodu)
        personel_bilgi = f"Ad: {self.__ad}, Soyad: {self.__soyad}, Personel No: {self.__personel_no}, Depratman: {self.__departman}, Maaş: {self.__maas}"
        return personel_bilgi
    