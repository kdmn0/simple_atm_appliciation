# SIMPLE ATM

import os
import time

# Programdaki fazlalık yazıları siler
def oncekileri_sil():
    os.system("cls")


bakiye = 2000
user_password = "12345"
kalan_hak = 3
oncekileri_sil()

# Giriş döngüsü
while True:
    print(user_password)
    password = str(input("""
********* ATM *********
Lütfen şifrenizi girin: """))
    kalan_hak -= 1

    if password == user_password:
        oncekileri_sil()
        print("Giriş Başarılı.\n")
        print("Ana menüye yönlendiriliyorsunuz...")
        time.sleep(2)

        # Ana menü döngüsü
        while True:
            oncekileri_sil()
            print("""
***** ATM ANA MENÜ *****
1. Bakiye Görüntüle
2. Hesap Bilgilerini Görüntüle
3. Para Yatır
4. Para Çek
5. Çıkış Yap
************************
""")
            try:
                islem = int(input("Yapmak istediğiniz işlemi seçin: "))

            except ValueError:
                oncekileri_sil()
                print("Lütfen Menüdeki işlemlerden birini seçin.")
                time.sleep(2)
                continue
            
            if islem == 1:
                oncekileri_sil()
                print(f"Bakiyeniz {bakiye} TL")

                devam = str(input("Ana menüye dönmek için entera basın... "))

                continue

            elif islem == 2:
                oncekileri_sil()

                print(f"""
-Hesap Sahibi: Yiğit Arda Kıdıman
-İban Numarası: TR***********************
-Güncel Bakiye: {bakiye} TL
                    """)

                devam = str(input("Ana menüye dönmek için entera basın... "))
                continue

            elif islem == 3:
                oncekileri_sil()

                yatirma = int(input("Ne kadar Para yatırmak istiyorsunuz: "))
                bakiye += yatirma

                print("İşleminiz Yapılıyor...")
                time.sleep(1)
                oncekileri_sil()

                print(f"Yeni bakiyeniz {bakiye} TL")
                devam = str(input("Ana menüye dönmek için entera basın... "))

                continue

            elif islem == 4:
                oncekileri_sil()

                cekme = int(input("Ne kadar Para çekmek istiyorsunuz: "))

                if cekme > bakiye:
                    print("Bankada o kadar paranız yok.")

                    devam = str(input("Ana menüye dönmek için entera basın... "))
                    continue

                else:
                    bakiye -= cekme
                    print("İşleminiz Yapılıyor...")
                    time.sleep(1)
                    oncekileri_sil()

                    print(f"Güncel Bakiyeniz {bakiye} TL")

                    devam = str(input("Ana menüye dönmek için entera basın... "))
                    continue

            elif islem == 5:
                oncekileri_sil()

                emin = str(input("Çıkış yapmak istediğinize emin misiniz(E/H): "))
                if emin.lower() == "e":
                    oncekileri_sil()

                    print("Çıkış yapılıyor...")
                    time.sleep(1)

                    break  # Ana menü döngüsünden çık
                else:
                    oncekileri_sil()

                    print("Ana menüye geri aktarılıyorsunuz...")
                    time.sleep(1)

                    continue
            else:
                oncekileri_sil()
                print("Lütfen geçerli bir işlem seçin...")
                time.sleep(1)
                continue

            # Menü seçimi dışındaki bir durumda döngüyü sonlandır
            break
        break  # Giriş döngüsünden çık

    # Şifre hatalı ise
    else:
        oncekileri_sil()
        print(f"Hatalı giriş, {kalan_hak} hakkınız kaldı")

        if kalan_hak == 0:
            oncekileri_sil()
            print("3 hatalı giriş yaptınız hesabınız bloklandı,\nLütfen bankayla iletişime geçin.")
            break  # Giriş döngüsünden çık