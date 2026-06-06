import os
import time

def ekrani_temizle():
    """Terminal ekranını temizler (Mac/Linux ve Windows uyumlu)."""
    if os.name == 'nt': 
        os.system('cls')
    else:               
        os.system('clear')

def baslik_yazdir(baslik_metni):
    """Menüler için şık bir başlık oluşturur."""
    print("\n" + "=" * 50)
    print(f" {baslik_metni.upper()} ".center(50, "★"))
    print("=" * 50 + "\n")

def hata_yazdir(hata_metni):
    """Kırmızı veya dikkat çekici şekilde hata mesajı yazdırır."""
    print(f"\n❌ DİKKAT: {hata_metni}\n")

def basari_yazdir(basari_metni):
    """Başarılı işlemleri belirgin şekilde yazdırır."""
    print(f"\n✅ BAŞARILI: {basari_metni}\n")

def guvenli_sayi_al(mesaj):
    """
    Kullanıcıdan sadece tam sayı girmesini ister. 
    Harf girilirse programın çökmesini engeller ve tekrar sorar.
    """
    while True:
        try:
            deger = input(mesaj)
            return int(deger)
        except ValueError:
            hata_yazdir("Lütfen harf veya boşluk bırakmadan sadece bir sayı giriniz!")

def beklet(saniye=1):
    """Programı belirtilen saniye kadar duraklatır."""
    time.sleep(saniye)