from random import *
def pikkus(ikood:int)->bool:
    """Funktsioon tagastab True, kkui pikkus on 11 sümbolid
     sümbolid
     param int ikood: Inimese isikukood
     rtypr:bool
    """
    if len(ikood)==11:
        flag=True 
    else:
        flag=False 
    return flag
def sugu(ikood: str)->str:
    """Kui esimene täht on[1,2,3,4,5,6], siis
        määrame sugu
        param str ikood: Isikukood
        rtype:str
    """
    ikood_list=list(map(int,ikood)) #["1","2",...]
    if ikood_list[0] in [1,3,5]:
        s="mees"
    elif ikood_list[0] in [2,4,6]:
        s="naine"
    else:
        s="viga"
    return s
def sunnipaev(ikood:str)->bool:
    """kui teine ja seitsmes arv vastab sünnipäeva data
    param int ikood:isikukood sünnipäev
    rtype:bool
    """
    ikood_age=list(map(int,ikood))
    if ikood_age[1] in [0,1,2,3,4,5,6,7,8,9] and ikood_age[2] in [0,1,2,3,4,5,6,7,8,9]:
        t=2006
    else:
        t=False 
    return t
def sunnikoht(ikood: str)->str:
    ikood_list=list(ikood)
    tahed_8910=ikood_list[7]+ikood_list[8]+[9]
    t=int(tahed_8910)
    if 1<t<10:
        haigla="kuegogsoig b"
    elif 11<t<19:
        haigla="tartu fsdfjsf"
    elif 21<t<220:
        haigla="jdfjgdfgdfgdfgd"
    else:
        haigla="ohio"
    return haigla
def lause(ikood: str)->str:
    print(f"see on {sugu(ikood)} ta on sündinud {sunnipaev(ikood)},tema sünnikoht on {sunnikoht(ikood)}")