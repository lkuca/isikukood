from omamodel import *
ikood=""
while True:
    ikood=input("Sissesta isikukood:")
    if pikkus(ikood)==False:
        print("Liiga pikk või lühike isikukood")
    else:
        print("11 sümbolid")
        s=sugu(ikood)
        if s=="viga":
            print("Esimene täht ei ole õige")
        else:
            print(s)
            if sunnipaev(ikood)=="viga":
                print("2-7 tähed on valesti sissetatud")
            else:
                lause(ikood)
                
