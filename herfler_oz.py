import webbrowser


class AzDili:

    def __init__(self):
        #Sait sesler
        self.saitler = 'AaEeƏəIıİiOoÖöUuÜü'
        self.sait_herfler = []

        self.qalin_saitler = 'AaIıOoUu'
        self.qalin_sait_sesler = []

        self.ince_saitler ='EeƏəİiÖöÜü'
        self.ince_sait_sesler = []

        self.qapali_saitler ='İiIıUuÜü'
        self.qapali_sait_sesler =[]

        self.aciq_saitler = 'AaEeƏəOoÖö'
        self.aciq_sait_sesler =[]

        self.dodaqlanan = 'OoÖöUuÜü'
        self.dodaqlanan_sait_sesler =[]

        self.dodaqlanmayan = 'AAEeƏəİiIı'
        self.dodaqlanmayan_sait_sesler =[]




        #Samit sesler
        self.samitler = 'BbCcÇçDdFfGgĞğHhXxJjKkQqLlMmNnPpRrSsŞşTtVvYyZz'
        self.samit_herfler = []

        self.kar_samitler = 'PpKkFfXxTtŞşSsÇçHh'
        self.kar_samit_sesler = []

        self.cingiltili_samitler = 'BbQqVvĞğDdJjZzYyGgCcLlMmNnRr'
        self.cingiltili_samit_sesler = []

        self.burun_samitler = 'MmNn'
        self.burun_samit_sesler = []

        self.sonor_samitler = 'LlMmNnRr'
        self.sonor_samit_sesler = []

        #simvollar

        self.simvol = '.+-*/"!@#$%&*()_-=<>,?'
        self.simvollar = []

        #self.ekrana_yaz()
        self.start()


    def ekrana_yaz(self):
        try:

            self.kelime = input("Cümlə Yazın: ")
            if self.kelime == '':
                print("Zəhmət olmasa cümlə yazınız")
                self.ekrana_yaz()
            elif self.kelime.isdigit():
                print("Reqem olmaz")
                self.ekrana_yaz()
            elif self.kelime == ' ':
                print("Zəhmət olmasa cümlə yazınız")
                self.ekrana_yaz()


        except KeyboardInterrupt:
            print()
            print("Cixis")



        else:
            if self.kelime[0] not in self.simvol:
                print('{} cümlısinde'.format(self.kelime))
                print('*'* len(self.kelime))
                self.sait_sesler()
                self.sait_qalin()
                self.sait_ince()
                self.sait_qapali()
                self.sait_aciq()
                self.sait_dodaqlanan()
                self.sait_dodaqlanmayan()
                print('*'*30)
                self.samit_sesler()
                self.samit_kar()
                self.samit_cingiltili()
                self.samit_burun()
                self.samit_sonor()
                print('*'*30)
                self.xusisi_simvollar()
                print('*'*30)
                self.say_herfler()
            else:
                print('Bu bir simvoldur')
                self.ekrana_yaz()




    def sait_sesler(self):
        for sait in self.saitler:
            if sait in self.kelime:
                self.sait_herfler.append(sait)
        if self.sait_herfler == []:
            print("Cümlədə Sait səsli hərf yoxdur")
        else:
            print('Cümlədə keçən Sait hərflər {}'.format(self.sait_herfler))

            print('*'*30)



    def samit_sesler(self):
        for samit in self.samitler:
            if samit in self.kelime:
                self.samit_herfler.append(samit)
        if self.samit_herfler == []:
            print("Cümlədə Samit seslı hərf yoxdur")
        else:
            print('Cümlədə keçən Samit hərflər {}'.format(self.samit_herfler))

    def sait_qalin(self):
        for s_qalin in self.qalin_saitler:
            if s_qalin in self.kelime:
                self.qalin_sait_sesler.append(s_qalin)
        if self.qalin_sait_sesler == []:
            print("Cümlədə Qalın Sait (dil arxası) sesli hərf yoxdur")
        else:
            print('Bunlardan Qalın Sait (dil arxası) səslər {} '.format(self.qalin_sait_sesler))

    def sait_ince(self):
        for s_ince in self.ince_saitler:
            if s_ince in self.kelime:
                self.ince_sait_sesler.append(s_ince)
        if self.ince_sait_sesler == []:
            print("Cümlədə İncə Sait (dil önü) sesli hərf yoxdur")
        else:
            print('Bunlardan İncə Sait (dil önü) səslər {}'.format(self.ince_sait_sesler))



    def sait_qapali(self):
        for s_qapali in self.qapali_saitler:
            if s_qapali in self.kelime:
                self.qapali_sait_sesler.append(s_qapali)
        if self.qapali_sait_sesler == []:
            print('Cümlədə Qapalı Sait (dar saitlər) səsli hərf yoxdur')
        else:
            print('Bunlardan Qapalı Sait  (dar saitlər) səslər {}'.format(self.qapali_sait_sesler))


    def sait_aciq(self):
        for s_aciq in self.aciq_saitler:
            if s_aciq in self.kelime:
                self.aciq_sait_sesler.append(s_aciq)
        if self.aciq_sait_sesler == []:
            print('Cümlədə Açıq (gen saitlər) səsli hərf yoxdur')
        else:
            print('Bunlardan Açıq Sait (gen saitlər) səslər {}'.format(self.aciq_sait_sesler))


    def sait_dodaqlanan(self):
        for s_dodaqlanan in self.dodaqlanan:
            if s_dodaqlanan in self.kelime:
                self.dodaqlanan_sait_sesler.append(s_dodaqlanan)
        if self.dodaqlanan_sait_sesler == []:
            print('Cümlədə dodaqlanan Sait səsli hərf yoxdur')
        else:
            print('Bunlardan Dodaqlanan Sait səslər {}'.format(self.dodaqlanan_sait_sesler))

    def sait_dodaqlanmayan(self):
        for s_dodaqlananmayan in self.dodaqlanmayan:
            if s_dodaqlananmayan in self.kelime:
                self.dodaqlanmayan_sait_sesler.append(s_dodaqlananmayan)
        if self.dodaqlanmayan_sait_sesler == []:
            print('Cümlədə dodaqlanmayan Sait hərf yoxdur')
        else:
            print('Bunlardan Dodaqlanmayan Sait səslər {}'.format(self.dodaqlanmayan_sait_sesler))


    def samit_kar(self):
        for s_kar in self.kar_samitler:
            if s_kar in self.kelime:
                self.kar_samit_sesler.append(s_kar)
        if self.kar_samit_sesler == []:
            print("Cümlədə kar Samit səsli hərf yoxdur")
        else:
            print("Bunlardan Kar Samit səslər {}".format(self.kar_samit_sesler))


    def samit_cingiltili(self):
        for s_cingiltili in self.cingiltili_samitler:
            if s_cingiltili in self.kelime:
                self.cingiltili_samit_sesler.append(s_cingiltili)
        if self.cingiltili_samit_sesler ==[]:
            print('Cümlədə Cingiltili Samit səsli hərf yoxdur')
        else:
            print('Bunlardan Cingiltili Samit səslər {}'.format(self.cingiltili_samit_sesler))

    def samit_burun(self):
        for s_burun in self.burun_samitler:
            if s_burun in self.kelime:
                self.burun_samit_sesler.append(s_burun)
        if self.burun_samit_sesler ==[]:
            print('Cümlədə Burun Samit səsli hərf yoxdur')
        else:
            print('Bunlardan Burun Samit səslər {}'.format(self.burun_samit_sesler))

    def samit_sonor(self):
        for s_sonor in self.sonor_samitler:
            if s_sonor in self.kelime:
                self.sonor_samit_sesler.append(s_sonor)
        if self.sonor_samit_sesler == []:
            print('Cümlədə Sonor Samit səsli hərf yoxdur')
        else:
            print('Bunlardan Sonor Samit səslər {}'.format(self.sonor_samit_sesler))


    def xusisi_simvollar(self):
        for s_simvol in self.simvol:
            if s_simvol in self.kelime:
                self.simvollar.append(s_simvol)
        if self.simvollar == []:
            print('Cümlədə Simvol yoxdur')
        else:
            print('Simvollar {}'.format(self.simvollar))


    def say_herfler(self):
        print('Sait Seslər')
        print('Cümlədə keçən  Sait seslerin sayı - {}'.format(len(self.sait_herfler)))
        print('Cümlədə keçən  Qalın Sait (dil arxası) seslerin sayı - {}'.format(len(self.qalin_sait_sesler)))
        print('Cümlədə keçən İncə Sait (dil önü) seslerin sayı - {}'.format(len(self.ince_sait_sesler)))
        print('Cümlədə keçən  Qapalı Sait (dar saitlər) seslerin sayı - {}'.format(len(self.qapali_sait_sesler)))
        print('Cümlədə keçən  Açıq Sait (gen saitlər) seslerin sayı - {}'.format(len(self.aciq_sait_sesler)))
        print('Cümlədə keçən  Dodaqlanan Sait seslerin sayı - {}'.format(len(self.dodaqlanan_sait_sesler)))
        print('Cümlədə keçən  Dodaqlanmayan Sait seslerin sayı - {}'.format(len(self.dodaqlanmayan_sait_sesler)))
        print('*'*30)
        print('Samit Seslər')
        print('Cümlədə keçən  Samit seslerin sayı - {}'.format(len(self.samit_herfler)))
        print('Cümlədə keçən  Kar Samit seslerin sayı - {}'.format(len(self.kar_samit_sesler)))
        print('Cümlədə keçən  Cingiltili Samit seslerin sayı - {}'.format(len(self.cingiltili_samit_sesler)))
        print('Cümlədə keçən  Burun Samit seslerin sayı - {}'.format(len(self.burun_samit_sesler)))
        print('Cümlədə keçən  Sonor Samit seslerin sayı - {}'.format(len(self.sonor_samit_sesler)))



    def start(self):
        url = 'https://az.wikipedia.org/wiki/Az%C9%99rbaycan_%C9%99lifbas%C4%B1'
        print("""Azərbaycan dili proqramına xoş gelmisiniz!
        **** Menu ****
        #.Vikipediyaya Kecid etmək istəyirsinizsə 'K' hərfini,
        #.Proqrama başlamaq istəyirsinizsə 'enter' düyməsini,
        #.Çıxış etmek üçün 'q' düyməsini basın""")
        while True:

            self.menu = input("Seçiminiz: ")

            if self.menu.lower() == 'k':
                print("Siz internet sehifəsindən linkə kecid etdiniz")
                webbrowser.open(url)
                input('Enter')
            elif self.menu.lower() == 'q':
                print('Salamat qal')
                break
                exit()
            else:
                print('Proqrama Xoş gəlmisiniz!')
                self.ekrana_yaz()




hefler = AzDili()