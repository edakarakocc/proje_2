import pandas as pd
import personel
import doktor
import hemsire
import hasta

try:
    personel1 = personel.Personel(1, "Eda", "Karakoç", "BIT", 10000)
    personel2 = personel.Personel(2, "Ela", "Yılmaz", "IK", 5000)
    personeller = [personel1, personel2]

    doktor1 = doktor.Doktor(3,"Ezgi","Karakoç","Beslenme ve Diyetetik",20000,"Obezite",7,"Klinik")
    doktor2 = doktor.Doktor(56,"Erkan","Esen","KBB",1900578,"Rinoplasti",10,"Galen")
    doktor3 = doktor.Doktor(8,"Ece","Karakoç","FTR",221323,"Pilates","None","None")
    doktorlar = [doktor1,doktor2,doktor3]

    hemsire1 = hemsire.Hemsire(77,"Damla","Suna","Polikinlik",3500,7,"None","Keşan Devlet Hastanesi")
    hemsire2 = hemsire.Hemsire(98,"Arda","Tufan","Acil",13000,12,"İlaç yapımı","Medar")
    hemsire3 = hemsire.Hemsire(49,"Aslı","Demir","KBB",4500,3,"Sağlıkta Yapay Zeka","Tokat Devlet Hastanesi")
    hemsireler = [hemsire1,hemsire2,hemsire3]

    hasta1 = hasta.Hasta(9875,"Saffet","Amca","11.10.1998","Lösemi","Kemoterapi","None","None")
    hasta2 = hasta.Hasta(1283,"Eslem","Tufan","10.02.2012","Vertigo","None","Erkan Esen","Aslı Demir")
    hasta3 = hasta.Hasta(102,"Ayşe","Kuş","20.07.2010","Obezite","Mide Ameliyatı","Ezgi Karakoç","None")
    hastalar = [hasta1,hasta2,hasta3]

    personelBilgi = []
    for personel in personeller:
        personelBilgi.append((personel.get_personel_no(),personel.get_ad(),personel.get_soyad(),personel.get_departman(),personel.get_maas()))
    doktorBilgi = []
    for doktor in doktorlar:
        doktorBilgi.append((doktor.get_personel_no(),doktor.get_ad(),doktor.get_soyad(),doktor.get_departman(),doktor.get_maas(),doktor.get_uzmanlik(),doktor.get_deneyim_yili(),doktor.get_hastane()))
    hemsireBilgi = []
    for hemsire in hemsireler:
        hemsireBilgi.append((hemsire.get_personel_no(),hemsire.get_ad(),hemsire.get_soyad(),hemsire.get_departman(),hemsire.get_maas(),None,None,None,hemsire.get_hastane(),hemsire.get_calisma_saati(),hemsire.get_sertifika()))
    hastaBilgi = []
    for hasta in hastalar:
        hastaBilgi.append((None,hasta.get_ad(),hasta.get_soyad(),None,None,None,None,None,None,None,hasta.get_hasta_no(),hasta.get_dogum_tarihi(),hasta.get_hastalik(),hasta.get_tedavi()))
    
    bilgiler = personelBilgi + doktorBilgi + hemsireBilgi + hastaBilgi
    
    columns = ["personel_no","ad","soyad","departman","maas","uzmanlik","deneyim_yili","hastane","calisma_saati","sertifika","hasta_no","dogum_tarihi","hastalik","tedavi"]
    df = pd.DataFrame(bilgiler, columns=columns)    
    df.fillna(0,inplace=True)
    print(df)


except Exception as e:
    print("Bir hata oluştu:", e)