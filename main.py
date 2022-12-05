# QAP 4
# Nov 29, 2022

Repeat = "Yes"
f = ""

while Repeat == "Yes":
    f = open("OSICDef.dat", "r")

    ClientName = input(" First/Last name: ").title()
    StAdd = input("Street Address: ")
    City = input("Enter Client city: ")
    Prov = input("Enter the Clients Provience: ")
    PostCode =input ("Enter the CLients Postal Code: ")
    PhoNum = input("Enter the Clients Phone Number: ")
    MulitplIn = int(input("Total Cars being insured:"))
    ExtraLia = input("Would you like Extra Liability up to (1,000,000) (Y / N): ")
    GlassCov = input("Would you like Glass Coverage (Y/N): ")
    LoanCar = input("Would you like a loan car (Y/N")
    PayMent = input("Would you like pay in Full or Monthly intervals? (F / M): ")

    POLICYNUM = int(f.readline())
    InsuranceRate = float(f.readline())
    InsurPrem = float(f.readline())
    ExtraLiability = float(f.readline())
    GlassCovrage = float(f.readline())
    LoanerCar = float(f.readline())
    HSTRate = float(f.readline())
    ProcessingFee = float(f.readline())

    g = open("Policies.dat", "a")
    g.write("{}".format(ClientName))
    g.write(", {}".format(StAdd))
    g.write((", {}".format(City)))
    g.write((", {}".format(Prov)))
    g.write(", {}".format(PostCode))
    g.write((", {}".format(PhoNum)))
    g.write(", {}".format(MulitplIn))
    g.write((", {}".format(ExtraLiability)))
    g.write(",{}".format(GlassCovrage))
    g.write(", {}".format(LoanerCar))
    g.write(", {}".format((PayMent)))

    # Math
    StartingRate = ""
    if MulitplIn == 1:
       StartingRate = InsuranceRate
    if MulitplIn > 1:
        StartingRate = InsuranceRate + (MulitplIn - 1) * (InsurPrem * InsuranceRate)
    if ExtraLia == "Y":
        StartingRate += ExtraLiability * InsurPrem
    if GlassCovrage == "Y":
        StartingRate += GlassCov * MulitplIn
    if LoanerCar == "Y":
        StartingRate += LoanerCar + InsuranceRate
    Taxes = StartingRate +( StartingRate * HSTRate)
    TotalPrice = Taxes
    MonthlyPrice = (Taxes + ProcessingFee) / 8

    g.write((", {}/n".format(TotalPrice)))
    g.close()

    print()
    print(f"       One Stop Insurance Company")
    print(f" Insurance Policy for: {ClientName:>12}")
    print("=" * 23)
    print(f"Client Name: {ClientName:>12}")
    print(f"Street Address: {StAdd:>12}")
    print(f"City:        {City:>12}")
    print(f"Province:    {Prov:>12}")
    print(f"Postal Code: {PostCode:>12}")
    print(f"Phone Number: {PhoNum:>12}")
    print(f"Cars Being Insured: {MulitplIn:>12}")

    if ExtraLiability == "Y":
        print("You have purchesed Extra Liability: ")
    if ExtraLiability == "N":
        print("You have opted out of Extra Liability:")
    if GlassCovrage == "Y":
        print("You have purchased Glass Coverage: ")
    if GlassCovrage == "N":
        print("You have opted out of Glass Coverage: ")
    if LoanerCar == "Y":
        print("You have purchased a loan Car: ")
    if LoanerCar == "N":
        print("You have opted out of a loan car: ")
    if PayMent == "F":
        "You have paid your balance in full:"
    if PayMent == "M":
        print("You have opted for Monthly Payments (Thanks you for your soul)")
    print("=" * 23)
    print("          Insurance              ")
    TotalPrice = "${:,.2f}".format(TotalPrice)
    print(f" Total Cost : {TotalPrice:>18}")
    MonthlyPrice = "${:,.2f}".format((MonthlyPrice))
    print(f" Monthly Payments: {MonthlyPrice:>12}")
    print()
    print(" Insuranced Policy information saved thank you for your business.")
    Repeat = input("Would you like to process another Policy? (Yes/No): ")

    POLICYNUM += 1
    f = open("OSICDef.dat", "r")
    f.write(str(POLICYNUM))
    f.write("\n{}".format(str(InsuranceRate)))
    f.write("\n{}".format(str(InsurPrem)))
    f.write("\n{}".format(str(ExtraLiability)))
    f.write("\n{}".format(str(GlassCovrage)))
    f.write("\n{}".format(str(LoanerCar)))
    f.write("\n{}".format(str(HSTRate)))
    f.write("\n{}".format(str(ProcessingFee)))

f.close()




