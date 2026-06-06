def ders_ekle(ders_adı, ders_kodu, kredi):
    print(f"{ders_adı} ({ders_kodu}) dersi eklendi. Kredi: {kredi}")
    for i in range(1, 4):
        print(f"{i}. hafta: {ders_adı} dersi işlendi.")

def ders_sil(ders_adı):
    print(f"{ders_adı} dersi silindi.")