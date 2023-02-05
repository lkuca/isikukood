from omamodel import *
ikood=""
while True:
    ikood=input("Sissesta isikukood:")
    if pikkus(ikood)==False:
        print("Liiga pikk või lühike isikukood")
    elif not ikood.isdigit():
        print("vaja ainult numbri sissestamine")
    else:
        print("11 sümbolid")
        s=sugu(ikood)
        if s=="viga":
            print("Esimene täht ei ole õige")
        else:
            print(s)
            sunnipaev(ikood)

            lause(ikood)
