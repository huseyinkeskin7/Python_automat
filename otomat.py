import time

print('Written by Hüseyin Berk Keskin')

while True:

    print('<<<İstenilen Ürünün Numarasini Giriniz>>>')
    print('1. Su')
    print('2. Redbull')
    print('3. Meyveli soda')
    print('4. Ülker Çikolatali Gofret')
    print('5. Hoşbeş')
    print('6. Cikis' )
    choice=int(input('Seçimizi tuşlayiniz: '))
    time.sleep(2)

    if choice==1:
        print('<< 3 TL >>')
        print('<<Ödeme Yöntemi Seçiniz>>')
        print('1. Kart ile')
        print('2. Nakit')
        odeme=int(input('Seçiminiz: '))
        if odeme==1:
            print('<Kartinizi Okutunuz>')
            time.sleep(3)
            print('Ürün Veriliyor...')
            print('İşlem Gerçekleşti, İyi Günler Dileriz...')
        elif odeme==2:
            print('<Madeni Para Atiniz>')
            time.sleep(2)
            print('Ürün Veriliyor...')
            time.sleep(2)
            print('İşlem Gerçekleşti, İyi Günler Dileriz...')

    elif choice==2:         
        print('<< 10 TL >>')
        print('<<Ödeme Yöntemi Seçiniz>>')
        print('1. Kart ile')
        print('2. Nakit')
        odeme=int(input('Seçiminiz: '))
        if odeme==1:
            print('<Kartinizi Okutunuz>')
            time.sleep(3)
            print('Ürün Veriliyor...')
            print('İşlem Gerçekleşti, İyi Günler Dileriz...')
        elif odeme==2:
            print('<Madeni Para Atiniz>')
            time.sleep(2)
            print('Ürün Veriliyor...')
            time.sleep(2)
            print('İşlem Gerçekleşti, İyi Günler Dileriz...')
            time.sleep(3)

    elif choice==3:         
        print('<< 7 TL >>')
        print('<<Ödeme Yöntemi Seçiniz>>')
        print('1. Kart ile')
        print('2. Nakit')
        odeme=int(input('Seçiminiz: '))
        if odeme==1:
            print('<Kartinizi Okutunuz>')
            time.sleep(3)
            print('Ürün Veriliyor...')
            print('İşlem Gerçekleşti, İyi Günler Dileriz...')
        elif odeme==2:
            print('<Madeni Para Atiniz>')
            time.sleep(2)
            print('Ürün Veriliyor...')
            time.sleep(2)
            print('İşlem Gerçekleşti, İyi Günler Dileriz...')
            time.sleep(3)

    elif choice==4:         
        print('<< 6 TL >>')
        print('<<Ödeme Yöntemi Seçiniz>>')
        print('1. Kart ile')
        print('2. Nakit')
        odeme=int(input('Seçiminiz: '))
        if odeme==1:
            print('<Kartinizi Okutunuz>')
            time.sleep(3)
            print('Ürün Veriliyor...')
            print('İşlem Gerçekleşti, İyi Günler Dileriz...')
        elif odeme==2:
            print('<Madeni Para Atiniz>')
            time.sleep(2)
            print('Ürün Veriliyor...')
            time.sleep(2)
            print('İşlem Gerçekleşti, İyi Günler Dileriz...')
            time.sleep(3)

    elif choice==5:         
        print('<< 8 TL >>')
        print('<<Ödeme Yöntemi Seçiniz>>')
        print('1. Kart ile')
        print('2. Nakit')
        odeme=int(input('Seçiminiz: '))
        if odeme==1:
            print('<Kartinizi Okutunuz>')
            time.sleep(3)
            print('Ürün Veriliyor...')
            print('İşlem Gerçekleşti, İyi Günler Dileriz...')
        elif odeme==2:
            print('<Madeni Para Atiniz>')
            time.sleep(2)
            print('Ürün Veriliyor...')
            time.sleep(2)
            print('İşlem Gerçekleşti, İyi Günler Dileriz...')
            time.sleep(3)

    elif choice==6:
        break
    else:
        print('Hatali Ürün Tuşlamasi Yaptiniz') 
        time.sleep(3)
            
        