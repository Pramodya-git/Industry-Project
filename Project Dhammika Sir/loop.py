import mysql.connector
sql = mysql.connector.connect(
host = "localhost",
user = "root",
passwd = "",
database = "synex_industries"
)
'''def FullSallary(Index,Name,Place,January,February,March,April,May,June,July,August,September,October,November,December):
    Es = []
    vay = sql.cursor()
    se  = "select Profession,Daily_Fee from profession where Profession_code = '%s'"%Place 
    vay.execute(se)
    se1 = vay.fetchall()
    for yt in se1:
        yt1 = yt
        Es.append(Index)
        Es.append(Name)
        Es.append(January)
        Es.append(February)
        Es.append(March)
        Es.append(April)
        Es.append(May)
        Es.append(June)
        Es.append(July)
        Es.append(August)
        Es.append(September)
        Es.append(October)
        Es.append(November)
        Es.append(December)
        for yci in yt1:
            Es.append(yci)
    print(Es) 
    FullSallary =[]
    EPFLi = []
    Tax_  = []    
    Netsalary = []
    print(Tax_)
    for KDH in range(2,14):
        tip = Es[KDH]
        Full = tip*Es[15]#FullSallary
        EPF = Full*8/100#EPF -
        TAX = Full*10/100#Tax -
        paint = Full-500#Paint -
        minez =EPF+TAX+500
        Net_Salary = Full-minez
        FullSallary.append(Full)
        EPFLi.append(EPF)
        Tax_.append(TAX)
        Netsalary.append(Net_Salary)
    vae =sql.cursor()
    bee ="insert into monthly_details values('%s','%s','%s',%f,%f,%f,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d)"%(Es[0],Es[1],Es[14],FullSallary[0],EPFLi[0]+Tax_[0]+500,Netsalary[0],Tax_[0],FullSallary[1],EPFLi[1]+Tax_[1]+500,Netsalary[1],Tax_[1],FullSallary[2],EPFLi[2]+Tax_[2]+500,Netsalary[2],Tax_[2],FullSallary[3],EPFLi[3]+Tax_[3]+500,Netsalary[3],Tax_[3],FullSallary[4],EPFLi[4]+Tax_[4]+500,Netsalary[4],Tax_[4],FullSallary[5],EPFLi[5]+Tax_[5]+500,Netsalary[5],Tax_[5],FullSallary[6],EPFLi[6]+Tax_[6]+500,Netsalary[6],Tax_[6],FullSallary[7],EPFLi[7]+Tax_[7]+500,Netsalary[7],Tax_[7],FullSallary[8],EPFLi[8]+Tax_[8]+500,Netsalary[8],Tax_[8],FullSallary[9],EPFLi[9]+Tax_[9]+500,Netsalary[9],Tax_[9],FullSallary[10],EPFLi[10]+Tax_[10]+500,Netsalary[10],Tax_[10],FullSallary[11],EPFLi[11]+Tax_[11]+500,Netsalary[11],Tax_[11])    
    vae.execute(bee)
    sql.commit()    
R = []
vab0 = sql.cursor()
vax  = "select EMPIndex from employee_data"
vab0.execute(vax)
vax1 = vab0.fetchall()
for _Ti in vax1:
    _Ti1 = _Ti 
    for _yi in _Ti1:
        R.append(_yi)        
for tx in R:
    Dic = []
    vab = sql.cursor()
    vaf = "select * from employee_data where EMPIndex = '%s'"%tx
    vab.execute(vaf)
    vaf1 = vab.fetchall()
    sql.commit()
    for Tin in vaf1:
        fb = Tin
        for vaf2 in fb:
            fb1 = vaf2
            Dic.append(fb1)
    FullSallary(Dic[0],Dic[1],Dic[2],Dic[3],Dic[4],Dic[5],Dic[6],Dic[7],Dic[8],Dic[9],Dic[10],Dic[11],Dic[12],Dic[13],Dic[14])'''
##############################################Monthly Details
'''rat = []
vaz0 = sql.cursor()
vap  = "select EIndex from monthly_details"
vaz0.execute(vap)
vap1 = vaz0.fetchall()
sql.commit()
for tea in vap1:
    uc = tea
    for kj in uc:
        rat.append(kj)
Rap =[]  
for duk in rat:         
    RAP =['Employee Name :','Profession :','January :','February :','March :','April :','May :','June :','July :','August :','September :','October :','November :','December :' ]
    vaz = sql.cursor()
    what = "select Name,Pro,_1NetSallary,_2NetSallary,_3NetSallary,_4NetSallary,_5NetSallary,_6NetSallary,_7NetSallary,_8NetSallary,_9NetSallary,_10NetSallary,_11NetSallary,_12NetSallary from monthly_details where EIndex ='%s'"%duk    
    vaz.execute(what)
    what1 = vaz.fetchall()
    for Kfc in what1:
        for jbl in Kfc:
            Rap.append(str(jbl))                            
print(Rap)
tex = open("SalarySheetForCompany.txt","w")
for kfc in range(1027):
    Rex = [RAP[0]+Rap.pop(0),RAP[1]+Rap.pop(0)]
    monthl = [RAP[2]+Rap.pop(0),RAP[3]+Rap.pop(0),RAP[4]+Rap.pop(0),RAP[5]+Rap.pop(0),RAP[6]+Rap.pop(0),RAP[7]+Rap.pop(0),RAP[8]+Rap.pop(0),RAP[9]+Rap.pop(0),RAP[10]+Rap.pop(0),RAP[11]+Rap.pop(0),RAP[12]+Rap.pop(0),RAP[13]+Rap.pop(0)]     
    tes    = ["_____________________________________________________________________________________________________________\n"]
    content = '\t\t\t\t\t'.join(Rex)
    content0 = '\n','\n','\n'.join(monthl)
    content1 = '\n','\n'.join(tes)
    tex.writelines(content)
    tex.writelines(content0)
    tex.writelines(content1)
tex.close()''' 
#################################################SalarySheetForCompany
'''det = ["_1Tax","_2Tax","_3Tax","_4Tax","_5Tax","_6Tax","_7Tax","_8Tax","_9Tax","_10Tax","_11Tax","_10Tax",]
det1 = []
fir = []
for deep in range(12):
    vaf = sql.cursor()
    gt  = "select %s from monthly_details"%det[deep]
    vaf.execute(gt)
    gt1 = vaf.fetchall()
    for goi in gt1:
        goi0 = goi
        for gt2 in goi0:
            fir.append(gt2)            
total = []
for jef in range(13):
        bik0 = 0
        kfa = 0
        jk = 0
        while kfa < 1027:
            if len(fir)==0:
                break
            else:    
                jet = fir.pop(jk)
                bik0 += jet
            kfa  += 1
        total.append(bik0)'''
################################################################Tax        
'''dep = ["_1FullSalary","_2FullSalary ","_3FullSalary","_4FullSalary","_5FullSallary"," _6FullSallary ","_7FullSallary","_8FullSalary","_9FullSallary","_10FullSallary","_11FullSallary","_12FullSallary",]        
det1 = []
for deep0 in range(12):
    vay = sql.cursor()
    b2k = "select %s from monthly_details"%dep[deep0]
    vay.execute(b2k)
    b1k = vay.fetchall()
    for bei in b1k:
        b0k = bei
        for bei0 in b0k:
            det1.append(bei0)                       
sum = []#Monthly full sallary
epf = []#monthly full epf
tac = []#monthly full tax
for jel in range(12):
    bit = 0
    neb = 0
    while neb < 1027:
        jey = det1.pop(0)
        bit += jey
        neb += 1
    sum.append(bit)
    epf.append(bit*8/100)
    tac.append(bit*10/100)
bex = 1600000000
profit = []
monthk = ['January','February','March','April','May','June','July','August','September','October','November','December']
for tep in range(12):
    xy = sum[tep]-(epf[tep]+tac[tep])
    yx = bex-xy
    profit.append(yx)
    print(monthk[tep],':',profit[tep]) '''   
##############################################################Company Profit
'''index = []
fat = sql.cursor()
fac = "select EIndex from monthly_details"
fat.execute(fac)
fac0 = fat.fetchall()
sql.commit()
for tire in fac0:
     fac1 = tire
     for fac2 in fac1:
        index.append(fac2)
Input = input("\t\tEnter Index Number :")
if Input not in index:
    while True:
        print("\t\t_______________________________")
        print("\t\tThis Index is not our databases")
        print("\n")
        Input = input("\t\tEnter Index Number :")
        if Input in index:
            break        
elif  Input in index:      
    days = ['January   :','February  :','March     :','April     :','May       :','June      :','July      :','August    :','September :','October   :','November  :','December  :']
    grosssalary = ['_1FullSalary','_2FullSalary','_3FullSalary','_4FullSalary','_5FullSallary ','_6FullSallary','_7FullSallary','_8FullSalary','_9FullSallary','_10FullSallary','_11FullSallary','_12FullSallary']
    Deducation = ['_1deducations','_2deducations','_3deducations','_4deducations','_5deducations','_6deducations','_7deducations','_8deducations ','_9deducations','_10deducations','_11deducations','_12deducations']
    netsallary = ['_1NetSallary','_2NetSallary','_3NetSallary','_4NetSallary','_5NetSallary','_6NetSallary','_7NetSallary','_8NetSallary','_9NetSallary','_10NetSallary','_11NetSallary','_12NetSallary']
    nik = []
    name = sql.cursor()
    van = "select Name from monthly_details where EIndex = '%s'"%Input###################Name eka
    name.execute(van)
    van0 = name.fetchall()
    sql.commit()
    for li in van0:
        pu = li
        for pu0 in pu:
            nik.append(pu0)
    tes = []
    for you in range(12):
        vae = sql.cursor()
        met = "select %s,%s,%s from monthly_details where EIndex ='%s'"%(grosssalary[you],Deducation[you],netsallary[you],Input)
        vae.execute(met)
        met0 = vae.fetchall()
        sql.commit()
        for beet in met0:
            met1 = beet
            for beet0 in met1:  
                tes.append(str(beet0))           
    pt = open(nik[0],"a")
    pt.writelines("Salary Sheet Of\t"+nik[0]+"\n")
    pt.writelines("=========================================================================================================\n")
    pt.writelines("Month\t\tGross Salary\t\tTotal Deducation\t\tNet Salary\n\n")
    for fy in range(12):
        pt.writelines(days[fy]+"\t"+tes.pop(0)+"\t\t"+tes.pop(0)+"\t\t\t"+tes.pop(0)+"\n")
    pt.close() 
    print("\t\tYour Salary Report Created.)    '''

############################################################################################
index = []
fat = sql.cursor()
fac = "select EIndex from monthly_details"
fat.execute(fac)
fac0 = fat.fetchall()
sql.commit()
for tire in fac0:
     fac1 = tire
     for fac2 in fac1:
        index.append(fac2)        
Input = input("\t\tEnter Index Number :")
if Input not in index:
    while True:
        print("\t\t_______________________________")
        print("\t\tThis Index is not our databases")
        print("\n")
        Input = input("\t\tEnter Index Number :")
        if Input in index:
            break        
if  Input in index:      
    Mon = input("\t\tEnter Month :")
    nik = []
    name = sql.cursor()
    van = "select Name from monthly_details where EIndex = '%s'"%Input###################Name eka
    name.execute(van)
    van0 = name.fetchall()
    sql.commit()
    for li in van0:
        pu = li
        for pu0 in pu:
            nik.append(pu0)##########################Name eka
    NAME = nik[0]        
    def Print(FullSallary,Deducation,Netsalary):
         global NAME
         ref = []
         ref.append(FullSallary)
         ref.append(Deducation)
         ref.append(Netsalary)
         pt = open(NAME,"a")
         pt.writelines("Salary Sheet Of\t"+NAME+"\n")
         pt.writelines("=========================================================================================================\n")
         pt.writelines("Month\t\tGross Salary\t\tTotal Deducation\t\tNet Salary\n\n")     
         pt.writelines(Mon+'  :'+"\t"+str(ref[0])+"\t\t\t"+str(ref[1])+"\t\t\t\t"+str(ref[2])+"\n")  
         pt.close() 
         print("\n")
         print("\t\tYour Salary Report Created.")    
    def January():
        output = []
        January = ["_1FullSalary "," _1deducations" ," _1NetSallary" ]
        vag = sql.cursor()
        met = "select %s,%s,%s from monthly_details where EIndex ='%s'"%(January[0],January[1],January[2],Input)
        vag.execute(met)
        met0 = vag.fetchall()
        for tup in met0:
           tup0 = tup
           for tip in tup0:
               output.append(tip)
        Print(output[0],output[1],output[2]) 
    def February():
        output = []
        February = ["_2FullSalary "," _2deducations" ," _2NetSallary" ]
        vag = sql.cursor()
        met = "select %s,%s,%s from monthly_details where EIndex ='%s'"%(February[0],February[1],February[2],Input)
        vag.execute(met)
        met0 = vag.fetchall()
        for tup in met0:
           tup0 = tup
           for tip in tup0:
               output.append(tip)
        Print(output[0],output[1],output[2])
    def March():
        output = []
        March = ["_3FullSalary "," _3deducations" ," _3NetSallary" ]
        vag = sql.cursor()
        met = "select %s,%s,%s from monthly_details where EIndex ='%s'"%(March[0],March[1],March[2],Input)
        vag.execute(met)
        met0 = vag.fetchall()
        for tup in met0:
           tup0 = tup
           for tip in tup0:
               output.append(tip)
        Print(output[0],output[1],output[2]) 
    def April():
        output = []
        April = ["_4FullSalary "," _4deducations" ," _4NetSallary" ]
        vag = sql.cursor()
        met = "select %s,%s,%s from monthly_details where EIndex ='%s'"%(April[0],April[1],April[2],Input)
        vag.execute(met)
        met0 = vag.fetchall()
        for tup in met0:
           tup0 = tup
           for tip in tup0:
               output.append(tip)
        Print(output[0],output[1],output[2])
    def May():
        output = []
        May = ["_5FullSallary "," _5deducations" ," _5NetSallary" ]
        vag = sql.cursor()
        met = "select %s,%s,%s from monthly_details where EIndex ='%s'"%(May[0],May[1],May[2],Input)
        vag.execute(met)
        met0 = vag.fetchall()
        for tup in met0:
           tup0 = tup
           for tip in tup0:
               output.append(tip)
        Print(output[0],output[1],output[2])
    def June():
        output = []
        June = ["_6FullSallary"," _6deducations" ," _6NetSallary" ]
        vag = sql.cursor()
        met = "select %s,%s,%s from monthly_details where EIndex ='%s'"%(June[0],June[1],June[2],Input)
        vag.execute(met)
        met0 = vag.fetchall()
        for tup in met0:
           tup0 = tup
           for tip in tup0:
               output.append(tip)
        Print(output[0],output[1],output[2])
    def July():
        output = []
        July = ["_7FullSallary"," _7deducations" ," _7NetSallary" ]
        vag = sql.cursor()
        met = "select %s,%s,%s from monthly_details where EIndex ='%s'"%(July[0],July[1],July[2],Input)
        vag.execute(met)
        met0 = vag.fetchall()
        for tup in met0:
           tup0 = tup
           for tip in tup0:
               output.append(tip)
        Print(output[0],output[1],output[2])
    def August():
        output = []
        August = ["_8FullSalary"," _8deducations" ," _8NetSallary" ]
        vag = sql.cursor()
        met = "select %s,%s,%s from monthly_details where EIndex ='%s'"%(August[0],August[1],August[2],Input)
        vag.execute(met)
        met0 = vag.fetchall()
        for tup in met0:
           tup0 = tup
           for tip in tup0:
               output.append(tip)
        Print(output[0],output[1],output[2])
    def September():
        output = []
        September = ["_9FullSallary"," _9deducations" ," _9NetSallary" ]
        vag = sql.cursor()
        met = "select %s,%s,%s from monthly_details where EIndex ='%s'"%(September[0],September[1],September[2],Input)
        vag.execute(met)
        met0 = vag.fetchall()
        for tup in met0:
           tup0 = tup
           for tip in tup0:
               output.append(tip)
        Print(output[0],output[1],output[2])        
    def October():
        output = []
        October = ["_10FullSallary"," _10deducations" ," _10NetSallary" ]
        vag = sql.cursor()
        met = "select %s,%s,%s from monthly_details where EIndex ='%s'"%(October[0],October[1],October[2],Input)
        vag.execute(met)
        met0 = vag.fetchall()
        for tup in met0:
           tup0 = tup
           for tip in tup0:
               output.append(tip)
        Print(output[0],output[1],output[2])
    def November():
        output = []
        November = ["_11FullSallary"," _11deducations" ," _11NetSallary" ]
        vag = sql.cursor()
        met = "select %s,%s,%s from monthly_details where EIndex ='%s'"%(November[0],November[1],November[2],Input)
        vag.execute(met)
        met0 = vag.fetchall()
        for tup in met0:
           tup0 = tup
           for tip in tup0:
               output.append(tip)
        Print(output[0],output[1],output[2])
    def December():
        output = []
        December = ["_12FullSallary"," _12deducations" ," _12NetSallary" ]
        vag = sql.cursor()
        met = "select %s,%s,%s from monthly_details where EIndex ='%s'"%(December[0],December[1],December[2],Input)
        vag.execute(met)
        met0 = vag.fetchall()
        for tup in met0:
           tup0 = tup
           for tip in tup0:
               output.append(tip)
        Print(output[0],output[1],output[2])        
    if Mon == 'January':
        January()
    if Mon == 'February':
        February()  
    if Mon == 'March':
        March()
    if Mon == 'April':
        April()
    if Mon == 'May':
        May()    
    if Mon == 'June':
        June()
    if Mon == 'July':
        July()
    if Mon == 'August':
        August()
    if Mon == 'September':
        September()
    if Mon == 'October':
        October()
    if Mon == 'November':
        November()
    if Mon == 'December':
        December()    


















