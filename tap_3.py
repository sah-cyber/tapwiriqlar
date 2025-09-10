#İki ədəd və bir riyazi əməliyyat (+, -, *, /) al və nəticəni göstər.



def kalkulyator():
    print("Her iki ededi yazdiqdan sonra zehmet olmasa emeliyat secin")

    try:
        birinci_eded = float(input("Birinci ədədi daxil edin: "))
        ikinci_eded = float(input("İkinci ədədi daxil edin: "))
    except ValueError:
        print("Zəhmət olmasa yalnız ədəd daxil edin.")
        return

    emeliyyat = input("Əməliyyatı daxil edin (+, -, *, /): ")

    if emeliyyat == "+":
        cem = birinci_eded+ikinci_eded
        print(f"{birinci_eded}+{ikinci_eded}={cem}")
    elif emeliyyat == "-":
        cem = birinci_eded - ikinci_eded
        print(f"{birinci_eded}-{ikinci_eded}={cem}")

    elif emeliyyat == "*":
        cem = birinci_eded * ikinci_eded
        print(f"{birinci_eded}*{ikinci_eded}={cem}")

    elif emeliyyat == "/":
        cem = birinci_eded / ikinci_eded
        print(f"{birinci_eded}/{ikinci_eded}={cem}")

    else:
        print("Zəhmət olmasa düzgün əməliyyat seçin: +, -, *, /")

kalkulyator()


