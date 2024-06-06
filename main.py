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
    doktor3 = doktor.Doktor(8,"Ece","Karakoç","FTR",None,"Pilates",None,None)
    doktorlar = [doktor1,doktor2,doktor3]
    
    hemsire1 = hemsire.Hemsire(77,"Damla","Suna","Polikinlik",3500,7,None,"Keşan Devlet Hastanesi")
    hemsire2 = hemsire.Hemsire(98,"Arda","Tufan","Acil",13000,12,"İlaç yapımı","Medar")
    hemsire3 = hemsire.Hemsire(49,"Aslı","Demir","KBB",4500,3,"Sağlıkta Yapay Zeka","Tokat Devlet Hastanesi")
    hemsireler = [hemsire1,hemsire2,hemsire3]
    
    hasta1 = hasta.Hasta(9875,"Saffet","Amca","11.10.1998","Lösemi","Kemoterapi",None,None)
    hasta2 = hasta.Hasta(1283,"Eslem","Tufan","10.02.2012","Vertigo",None,"Erkan Esen","Aslı Demir")
    hasta3 = hasta.Hasta(102,"Ayşe","Kuş","20.07.2010","Obezite","Mide Ameliyatı","Ezgi Karakoç",None)
    hastalar = [hasta1,hasta2,hasta3]
            
except Exception as e:
    print("Bir hata oluştu:", e)
