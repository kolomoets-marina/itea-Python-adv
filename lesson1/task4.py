def bank(Deposit,Year,Percent):
    Summa=Deposit+(Deposit*Percent/100)*Year
    print(Summa)


bank(10000,3,10)