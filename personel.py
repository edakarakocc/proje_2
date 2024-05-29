class Personel:
    def __init__(self,personel_no,ad,soyad,departman,maas):
        self.__personel_no = personel_no
        self.__ad = ad
        self.__soyad = soyad
        self.__departman = departman
        self.__maas = maas
    
    def get__personel_no(self):
        return self.__personel_no
    def set__personel_no(self,personel_no):
        self.__personel_no = personel_no
    
    def get__ad(self):
        return self.__ad
    def set__ad(self,ad):
        self.__ad = ad

    def get__soyad(self):
        return self.__soyad
    def set__soyad(self,soyad):
        self.__soyad = soyad

    def get__departman(self):
        return self.__departman
    def set__departman(self,departman):
        self.__departman = departman    

    def get__maas(self):
        return self.__maas
    def set__maas(self,maas):
        self.__maas = maas   
        
    def __str__(self):
        personel_bilgi = f"Ad: {self.__ad}, Soyad: {self.__soyad}, Personel No: {self.__personel_no}, Depratman: {self.__departman}, Maaş: {self.__maas}"
        return personel_bilgi
    