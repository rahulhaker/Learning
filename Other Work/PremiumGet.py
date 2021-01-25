DirPath = r'C:\Users\rahul.5.sharma.INCOFORGETECH\OneDrive - Coforge Limited\Work\Python\NewPDFRead\NationwideNY-Auto.txt'
def FindHighLevelPremiumdetails(FileText,StartPointer,DiscountStart):
    '''Find Premium details of all vehicle level'''
    TempStart = StartPointer+9 #Without considering "Premium "
    HighLevelPremData = []
    while TempStart<=DiscountStart: 
            TempVehicleModel = FileText[TempStart:TempStart+4] 
            if TempVehicleModel.isnumeric()== True:
                break
            TempStart+=1
    while TempStart<DiscountStart:
        Temp = FileText.find (".",TempStart)+2
        for x in range(Temp,TempStart,-1): 
            if FileText[x:x+1].isspace() ==True: TempSpace = x;break
        TempVehicleModel = FileText[TempStart:TempStart+4]
        if  TempVehicleModel.isnumeric() == True: 
            TempModelYear = FileText[TempStart:TempStart+4]
            TempVehicleName = FileText[TempStart+5:TempSpace-1].rstrip()
            TempVehiclePrem = (FileText[TempSpace+1:Temp+1]+"$").lstrip()
        else: 
            TempModelYear = "XXXX"
            TempVehicleName = FileText[TempStart:TempSpace-1].split("$")[0].rstrip()
            TempVehiclePrem = (FileText[TempSpace+1:Temp+1]+"$").lstrip()
        HighLevelPremData.append([TempModelYear,TempVehicleName,TempVehiclePrem])
        TempStart=Temp+2
    return HighLevelPremData

def FindDriverDetails(FileText,DriverInfoStart,ScheduleInfoStart):
    FirstDriverStart = FileText.find("Vehicle\n",DriverInfoStart,ScheduleInfoStart)+8
    if FirstDriverStart != -1 and FirstDriverStart != 0:
        DriverDetailList = FileText[FirstDriverStart:ScheduleInfoStart-23].split()
        ind,DriverDetails = 0,[]
        while ind <len(DriverDetailList):
            DriverDetails.append([DriverDetailList[ind],DriverDetailList[ind+1]+" "+DriverDetailList[ind+2],DriverDetailList[ind+3],DriverDetailList[ind+4],DriverDetailList[ind+5],DriverDetailList[ind+6],DriverDetailList[ind+7]])
            ind = ind+8
    return DriverDetails
def FindPolicyDetails(FileText,StartPointer):
    '''This function finds details of the pointers and send data to appropriate functions to get details'''
    DiscountStart = FileText.find("How You Saved",StartPointer)
    DriverInfoStart = FileText.find("Driver(s)",StartPointer)
    ScheduleInfoStart = FileText.find("Schedule of Coverages",StartPointer)
    #Finding VehicleLevelPremium
    VehiclePremiumDetails = FindHighLevelPremiumdetails(FileText,StartPointer,DiscountStart)
    #Finding Driver information
    DriverDetails = FindDriverDetails(FileText,DriverInfoStart,ScheduleInfoStart)
    #Finding VIN Coverage  and Premium Details
    #print(VehiclePremiumDetails)

with open(DirPath,'r') as ResultFile:
    ResultFileText = ResultFile.read()
    PremDetPage = ResultFileText.find("Premium Summary")
    if PremDetPage != -1:
        PolicyDetails = FindPolicyDetails(ResultFileText,PremDetPage)
    else: 
        print("Nothing")

