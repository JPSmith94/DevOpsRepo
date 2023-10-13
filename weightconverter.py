weight = input("Enter KG or LBs")
if weight == ("KG") :
    KGs = float(input("What is your weight in KG's?"))
    LBs = KGs * 2.20462
    print(LBs)
else:
    print("invalid Weight Format")
if weight == ("LBs"):
    LBs = float(input("What is your weight in LB's?"))
    KGs = LBs / 2.20462
    print(KGs)
else:
    print("invalid Format")