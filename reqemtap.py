import random



class ReqemTap:
    def __init__(self,reqem,ad,xal=6):
        self.reqem = reqem
        self.ad = ad
        self.xal = xal
        self.start()

    def start(self):
        self.ad = input("Zehmet olmasa adinizi qeyd edin: ")
        if self.ad == '':
            print("Adi duz qeyd edin")
        else:
            print('Xow gelmisiniz ',self.ad)

        self.reqem =random.randint(1,10)
        print(self.ad,'Kampyuter 1-20 arasi reqem tutub buyurun tapin ve sizin 6 gediwiniz var')
        print('Byurun reqeminiz?')
        while True:
            self.reqemtut = int(input("Reqeminiz? : "))

            if self.reqemtut != self.reqem:
                print("Bir daha cehd edin")
                self.xal -=1
                print("Bir gediw haqqiniz cixildi sizin {} xaliniz var".format(self.xal))
                if self.xal <= 0:
                     print("siz udunuzdunuz ")
                     exit()
                elif self.reqem < self.reqem:
                    print("tutulan reqem kicikdir")
                elif self.reqem > self.reqem:
                    print("tutulan reqem boyukdur")
            else:
                print("Siz qalib geldiniz")
                exit()



yr = ReqemTap(5,'sah')