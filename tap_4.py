

def tek_cut():
    try:
        eded = int(input("Ededi daxil edin: "))
        if eded == 0:
            print(f"Sizin daxil etdiyiniz {eded} sifirdir")
        elif eded %2 == 0:
            print(f"Sizin daxil etdiyiniz {eded} cut ededdir")
        else:
            print(f"Sizin daxil etdiyiniz {eded} tek ededdir")


    except ValueError:
        print("Zehmet olmasa eded daxil edin")

tek_cut()