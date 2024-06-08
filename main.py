import pandas as pd
import personel
import doktor
import hemsire
import hasta

try:
    #Personel nesneleri oluşturulmuştur
    personel1 = personel.Personel(1, "Eda", "Karakoç", "BIT", 10000)
    personel2 = personel.Personel(2, "Ela", "Yılmaz", "IK", 5000)
    personeller = [personel1, personel2]
    
    #Doktor nesneleri oluşturulmuştur
    doktor1 = doktor.Doktor(3,"Ezgi","Karakoç","Beslenme ve Diyetetik",20000,"Obezite",7,"Klinik")
    doktor2 = doktor.Doktor(56,"Erkan","Esen","KBB",1900578,"Rinoplasti",10,"Galen")
    doktor3 = doktor.Doktor(8,"Ece","Karakoç","FTR",221323,"Pilates",1,"None")
    doktorlar = [doktor1,doktor2,doktor3]
    
    #Hemşire nesneleri oluşturulmuştur
    hemsire1 = hemsire.Hemsire(77,"Damla","Suna","Polikinlik",3500,7,"Serum yapımı","Keşan Devlet Hastanesi")
    hemsire2 = hemsire.Hemsire(98,"Arda","Tufan","Acil",13000,12,"İlaç yapımı","Medar")
    hemsire3 = hemsire.Hemsire(49,"Aslı","Demir","KBB",4500,3,"Sağlıkta Yapay Zeka","Tokat Devlet Hastanesi")
    hemsireler = [hemsire1,hemsire2,hemsire3]
    
    #Hasta nesneleri oluşturulmuştur
    hasta1 = hasta.Hasta(9875,"Saffet","Amca","11.10.1850","Lösemi","Kemoterapi","None","None")
    hasta2 = hasta.Hasta(1283,"Eslem","Tufan","10.02.2012","Vertigo","Nootropil","Erkan Esen","Aslı Demir")
    hasta3 = hasta.Hasta(102,"Ayşe","Kuş","20.07.2010","Obezite","Mide Ameliyatı","Ezgi Karakoç","None")
    hastalar = [hasta1,hasta2,hasta3]
    
    personelBilgi = [] #Personel bilgilerini tutmak için oluşturulan liste
    for personel in personeller:  #Gerekli olan bilgiler personelBilgi listesine eklenir
        personelBilgi.append((personel.get_personel_no(),personel.get_ad(),personel.get_soyad(),personel.get_departman(),personel.get_maas()))
    
    doktorBilgi = [] #Doktor bilgilerini tutmak için oluşturulan liste
    for doktor in doktorlar:  #Gerekli olan bilgiler doktorBilgi listesine eklenir
        doktorBilgi.append((doktor.get_personel_no(),doktor.get_ad(),doktor.get_soyad(),doktor.get_departman(),doktor.get_maas(),doktor.get_uzmanlik(),doktor.get_deneyim_yili(),doktor.get_hastane()))
    
    hemsireBilgi = [] #Hemşire bilgilerini tutmak için oluşturulan liste
    for hemsire in hemsireler:  #Gerekli olan bilgiler hemsireBilgi listesine eklenir
        hemsireBilgi.append((hemsire.get_personel_no(),hemsire.get_ad(),hemsire.get_soyad(),hemsire.get_departman(),hemsire.get_maas(),None,None,None,hemsire.get_hastane(),hemsire.get_calisma_saati(),hemsire.get_sertifika()))
    
    hastaBilgi = [] #Hasta bilgilerini tutmak için oluşturulan liste
    for hasta in hastalar:  #Gerekli olan bilgiler hastaBilgi listesine eklenir
        hastaBilgi.append((None,hasta.get_ad(),hasta.get_soyad(),None,None,None,None,None,None,None,hasta.get_hasta_no(),hasta.get_dogum_tarihi(),hasta.get_hastalik(),hasta.get_tedavi()))
    
    bilgiler = personelBilgi + doktorBilgi + hemsireBilgi + hastaBilgi
    
    #DataFrame'in sütunlarını oluşturur
    columns = ["personel_no","ad","soyad","departman","maas","uzmanlik","deneyim_yili","hastane","calisma_saati","sertifika","hasta_no","dogum_tarihi","hastalik","tedavi"]
    df = pd.DataFrame(bilgiler, columns=columns)    
    #DataFrame içerisindeki 'None' değerlerini '0' ile değiştirir
    df.fillna(0,inplace=True)
    print(df) #DataFrame'i ekrana yazdırır
    
    #Doktorları uzmanlık alanlarına göre gruplandırıp sayılarını yazmak için oluşturulmuştur
    doktor_uzmanligi = df[df['uzmanlik'] != 0].groupby('uzmanlik').size()
    for uzmanlik, sayi in doktor_uzmanligi.items(): 
        print(f"{uzmanlik} alanında uzman doktor sayısı: {sayi}")
    
    #Deneyim yılı 5'ten fazla olan doktor sayısını yazdırmak için oluşturulmuştur    
    deneyimi_fazla = len(df[(df['deneyim_yili'] > 5)])
    print("\n5 yıldan fazla deneyimi olan doktor sayısı: ",deneyimi_fazla)
    
    #Hasta adına göre sıralanmış DataFrame'i yazdırmak için oluşturulmuştur
    duzenlenmis_df = df.sort_values(by='ad')
    print("\nHasta adına göre düzenlenmiş DataFrame:")
    print(duzenlenmis_df)
    
    #Maaşı 7000 TL üzerinde olan personelleri yazdırmak için oluşturulmuştur
    yuksek_maas = df[df['maas']> 7000]
    print("\nMaaşı 7000 TL üzerinde olan personeller: ")
    print(yuksek_maas)
    
    #Doğum yılı 1990 ve sonrası olan hastaları yazdırmak için oluşturulmuştur
    dogum_yillari = [] #Doğum yıllarını tutmak için oluşturulan liste
    for dogum_tarihi in df['dogum_tarihi']:
        if dogum_tarihi != 0: #dogum_tarihi değişkeni '0' ifadesi içermiyorsa bu kod bloğu çalışır
            #dogum_tarihi değişkeninden '.' ifadeleri çıkartılır ve son kısmı alınarak int bir değişkene dönüştürülerek 'dogum_yillari' listesine eklenir
            dogum_yillari.append(int(dogum_tarihi.split('.')[-1])) 
        else:
            dogum_yillari.append(0) #eğer dogum_tarihi değişkeni '0' içeriyorsa 'dogum_yillari' listesine '0' olarak eklenir
    df['dogum_yili'] = dogum_yillari #DataFrame'in içerisine 'dogum_yili' adında bir sütun açılır ve 'dogum_yillari' listesinin içeriği buraya yerleştirilir
    
    genc_hasta = df[df['dogum_yili'] >= 1990] #Doğum yılı 1990 ve üzeri olan hastalar ekrana yazdırılır
    print("\nDoğum tarihi 1990 ve sonrası olan hastalar:")
    print(genc_hasta)
    
    #Belirli değişkenlere göre oluşturulan yeni DataFrame'i yazdırmak için oluşturulmuştur
    yeni_df = df[['ad', 'soyad', 'departman', 'maas', 'uzmanlik', 'deneyim_yili', 'hastalik', 'tedavi']]
    print("\nYeni DataFrame:")
    print(yeni_df)

except Exception as e:
    print("Bir hata oluştu:", e)