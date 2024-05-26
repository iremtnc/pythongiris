# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 20:07:29 2024

@author: itsme
"""

#Sınıflar 

class Araba(): 
    marka="Mini cooper" 
    model="Mini işte" 
    motorHacmi=3.0 
    yili=2024
    renk="Koyu yeşil" 
    
araba1=Araba() 
print(araba1) 

print(araba1.model) 
print(araba1.renk) 

dir(araba1) 


############################

class Personel(): 
    def __init__(self,isim,soyisim,no,maas,yetenekleri) :
        self.isim=isim 
        self.soyisim=soyisim
        self.no=no
        self.maas=maas 
        self.yetenekleri=yetenekleri 
        
    
    def bilgileriGetir(self):
        print("""
              Çalışan Bilgileri:
              İsim: {}
              Soyisim: {}
              Sicil No: {}
              Maaş: {}
              Yetenekleri: {} 
              
             
              """.format(self.isim,self.soyisim,self.no,self.maas,self.yetenekleri)) 
            
    
    def yetenekEkle(self,yeniyetenek): 
        self.yetenekleri.append(yeniyetenek) 
        print("Yeni yetenek eklendi") 
        
        
    def zamYap(self,zamMiktari): 
        self.maas += zamMiktari
        print("Zam yapıldı") 
        
personel1=Personel("İrem", "Tuna", 102, 50000,["Excel","Python","C#"])  

personel1.bilgileriGetir() 

personel1.yetenekEkle("Java") 

personel1.bilgileriGetir() 
  

personel2=Personel("Gülnihal", "Akın", 107, 50000, ["HTML", "CSS"]) 

personel2.bilgileriGetir() 
    
personel2.zamYap(5000) 

personel2.bilgileriGetir()     
    

class Yonetici(Personel): 
    def __init__(self, isim, soyisim, no, maas,
                 yetenekleri,kisisayisi):
        
       #1. yöntem 
       # self.isim=isim 
       # self.soyisim=soyisim
       # self.no=no
       # self.maas=maas 
       # self.yetenekleri=yetenekleri
       # self.kisisayisi=kisisayisi 


       #2. yöntem 
       super().__init__(isim, soyisim, no, maas, yetenekleri)
       self.kisisayisi=kisisayisi  
       
       
    def bilgileriGetir(self):
          print("""
                Yönetici Bilgileri:
                İsim: {}
                Soyisim: {}
                Sicil No: {}
                Maaş: {}
                Yetenekleri: {} 
                Sorumlu olduğu kişi sayısı: {} 
                
               
                """.format(self.isim,self.soyisim,self.no,self.maas,self.yetenekleri,self.kisisayisi)) 



y1=Yonetici("Emir", "Yıldız", 101, 100000, ["Excel","Java","Python"], 15) 

y1.bilgileriGetir() 

y1.zamYap(10000) 

y1.bilgileriGetir() 

y1.yetenekEkle("C#")  
y1.bilgileriGetir() 


#Kumanda 

class Kumanda(): 
    def __init__(self,tvDurumu="Kapalı",tvSes=0,kanalListesi=["TRT"], kanal="TRT"): 
        self.tvDurumu=tvDurumu 
        self.tvSes=tvSes 
        self.kanalListesi=kanalListesi 
        self.kanal=kanal 
        
        
    def tvAc(self): 
        if (self.tvDurumu=="Açık"): 
            print("Tv zaten açık") 
        else: 
            print("TV açıldı") 
            self.tvDurumu="Açık" 
            
            
    def tvKapat(self): 
         if (self.tvDurumu=="Kapalı"): 
             print("Tv zaten kapalı") 
         else: 
             print("TV kapandı") 
             self.tvDurumu="Kapalı"  
             
             
             
    def sesAyari(self): 
        cevap=input("Sesi azalt: '<' Sesi arttır: '>' ") 
        if (cevap=="<"): 
            if (self.tvSes!=0): 
                self.tvSes-=1 
                print("Ses:",self.tvSes) 
            else: 
                print("Sessizde") 
                
        elif(cevap==">"): 
            if (self.tvSes!=30): 
                self.tvSes=+1 
                print("Ses:",self.tvSes) 
            else: 
                print("Yükses ses sağlığa zararlı") 
                
        else: 
            print("Ses güncellendi.")  
            
            

    def kanalEkle(self,yenikanal): 
        self.kanalListesi.append(yenikanal) 
        print("Yeni kanal eklendi") 
    
    
    def __len__(self): 
        return len(self.kanalListesi) 
    
    def __str__(self): 
     return "Tv Durumu: {}\n Tv Ses: {}\n Kanal Listesi: {}\n Şu anki Kanal: {}\n".format(self.tvDurumu,self.tvSes,self.kanalListesi,self.kanal) 


kumanda=Kumanda() 

kumanda.kanalListesi 
kumanda.kanal 
kumanda.tvDurumu 

print("""
1. Tv Aç 
2. Tv Kapat 
3. Ses Ayarları
4.Kanal Ekle 
5. Kanal Sayısı öğren
6. Tv bilgileri 
Çıkış: q
      """)

while True: 
    islem=input("İşlem seçiniz:") 
    if(islem=="q"): 
        print("Program kapatılıyor...") 
        break 
    elif(islem=="1"): 
        kumanda.tvAc() 
    elif(islem=="2"): 
        kumanda.tvKapat() 
    elif(islem=="3"): 
        kumanda.sesAyari() 
    elif(islem=="4"): 
        yenikanal=input("Yeni kanal:")
        kumanda.kanalEkle(yenikanal) 
    elif(islem=="5"): 
        print("Kanal sayısı:", len(kumanda)) 
    elif(islem=="6"): 
        print(kumanda) 
    else: 
        print("Geçersiz işlem") 
        
        
        

    
    
    
    
    
    
    
    
    
    
    
    