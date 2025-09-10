
#İstifadəçidən bir söz və ya cümlə al və onun uzunluğunu ekrana yaz.

def soz_uzunlugu():
    soz = input('Zehmet olmasa soz veya cumle yazin: ')

    if soz.strip() =="":
        print("Zehmet olmasa  soz veya cumle yaizniz bow metn daxil etmeyin")
        return

    herf_sayisi = sum(1 for herf in soz if herf.isalpha())
    


    print('Sizin yazdiginiz {} sozde herf sayisi {} herfe beraberdir'.format(soz,herf_sayisi))



soz_uzunlugu()

