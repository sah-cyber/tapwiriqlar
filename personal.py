import time


class Personal:
    personal = []
    bacariq = []
    esas = {}

    def __init__(self, isim):
        self.isim = isim
        self.menu()

    def personal_yaz(self):
        self.ad = input("Personalin adini qeyd edin: ")
        self.personal.append(self.ad)
        print('qeyd etdiyiniz {} personal  tarix {}'.format(self.ad,
                                                            time.strftime('ayin-%m gun-/%d saat %H:%M qeyd edildi')))
        self.bacariq_yaz()

    def bacariq_yaz(self):
        self.bacariqlar = input('bacariqlarini yaz: ')
        self.bacariq.append(self.bacariqlar)
        print('qeyd etdiyiniz {} bacariq qeyd edildi'.format(self.bacariqlar))

    def personal_goster(self):
        print("Personallar")
        for person in self.personal:
            print(person)

    def bacariq_goster(self):
        print('Bacariqlar')
        for bacar in self.bacariq:
            print(bacar)

    def sil(self):
        self.ad_sil = input('Silmek istediyinizadi qeyd edin: ')
        for i in self.personal:
            if self.ad_sil == i:
                self.personal.remove(i)
                print('{} silindi'.format(i))

    def luget(self):
        self.esas = zip(self.personal, self.bacariq)

        for k, v in self.esas:
            print(k, v)

    def menu(self):
        print()
        try:

            print("""Secim edin:
            1.Personal yaz.
            2.Personal goster
            3.Bacariqlari goster
            4.sil
            5.luget
            Q-cixiw""")
            self.menu_goster = input('Seciminiz: ')

            if self.menu_goster == '1':
                self.personal_yaz()
            elif self.menu_goster == '2':
                self.personal_goster()
            elif self.menu_goster == '3':
                self.bacariq_goster()
            elif self.menu_goster == '4':
                self.sil()
            elif self.menu_goster == '5':
                self.luget()
            elif self.menu_goster.lower() == 'q':
                print('Cixiw')
                exit()
            else:
                print("Secim edin")
            self.menu()
        except KeyboardInterrupt:
            print()
            print("baglaniw")


iwci = Personal('sah')
