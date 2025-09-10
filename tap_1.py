#1. Rəqəm Təyini

#İstifadəçidən bir ədəd al və bu ədədin müsbət, mənfi və ya sıfır olduğunu müəyyən et.


def reqem_teyini():

    try:
        reqem_sec = int(input("bir reqem giriniz: "))

        if reqem_sec >0:
            print(f"Sizin qeyd etdiyiniz {reqem_sec} musbet ededdir")
        elif reqem_sec == 0:
            print(f"Sizin qeyd etdiyiniz {reqem_sec} -dir")
        else:
            print(f"Sizin qeyd etdiyiniz {reqem_sec} menfi ededdir")
    except ValueError:
        print("Zehmet olmasa reqem seciniz")

reqem_teyini()




