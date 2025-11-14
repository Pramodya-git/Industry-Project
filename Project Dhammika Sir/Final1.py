import mysql.connector
import getpass
import sys
#Hello World
sql  = mysql.connector.connect(
host = "localhost",
user = "root",
passwd = ""
)
 
Tec = []
mac0 = sql.cursor()
_dk = "show databases"
mac0.execute(_dk)
mac01 = mac0.fetchall()
for _p in mac01:
    for _t in _p :
        Tec.append(_t)  
if 'synex_industries' not in Tec :
    mac =sql.cursor()
    _UK = "create  database Synex_Industries"
    mac.execute(_UK)
    val = sql.cursor()
    ap   = "use synex_Industries"
    val.execute(ap)
    mac1 = sql.cursor()
    _E = "create table User_Password(UserName varchar (50) primary key unique,Password varchar (20) unique)"
    mac1.execute(_E)
    mac2 = sql.cursor()
    _F   ="create table User_Type(UserName varchar(50),UserType char (6) not null,foreign key(UserName)references user_password(UserName))"
    mac2.execute(_F)
    mac3 = sql.cursor()
    _G   = "insert into user_password values('Seller1','077069')"
    mac3.execute(_G)
    sql.commit()
    mac4 = sql.cursor()
    _H   = "insert into user_type values('Seller1','owner')"
    mac4.execute(_H)
    sql.commit()
    mac5 = sql.cursor()
    _I   = "insert into user_password values('Seller2','3036')"
    mac5.execute(_I)
    sql.commit()
    mac6 = sql.cursor()
    Sa   = "insert into user_type values('Seller2','admin')"
    mac6.execute(Sa)
    sql.commit()
    mac7 = sql.cursor()
    _L   = "insert into user_password values('Seller3','123')"
    mac7.execute(_L)
    sql.commit()
    mac8 = sql.cursor()
    _T   = "insert into user_type values('Seller3','owner')"
    mac8.execute(_T)
    sql.commit()

    KP = []
    val0 = sql.cursor()
    bt = "show tables"
    val0.execute(bt)
    b10 = val0.fetchall()
    for KG in b10:
       for B2 in KG :
           KP.append(B2)
    if 'profession' not in KP:       
        val1 = sql.cursor()
        a10 = "create table Profession(Profession varchar(30) not null,Profession_code char(50) primary key,Daily_Fee float(40,2) not null)"
        val1.execute(a10)    
        val2 = sql.cursor()
        CS   = "insert into profession values('Director','1',3000.00)"
        val2.execute(CS)   
        val3 = sql.cursor()
        Qw   = "insert into profession values('Scientist','2',2371.76)"
        val3.execute(Qw)   
        val4 = sql.cursor()
        Q_   = "insert into profession values('Engineer','3',1500.00)"
        val4.execute(Q_) 
        val5 = sql.cursor()
        K_   = "insert into profession values('Clerk','4',756.60)"
        val5.execute(K_)
        val6 = sql.cursor()
        R_   = "insert into profession values('Driver','5',500.00)"
        val6.execute(R_)
        print("\t\t******** Upload Data successfully ********")
else:
    sql  = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "",
    database = "synex_Industries"
    )        
print("\n")
print("\t\t============ Synex Industries ============\n")###############Begin######################

def Login():############################################User Name,Password පරික්ෂා කිරීම####################################### 
   back = input("\t\tTo Exit :")
   print("\n")
   if back == '000':
       sys.exit()
   else :
       UName = input("\t\tEnter User Name :")
       var   = sql.cursor()
       a     = "select UserType from User_Type where UserType = '%s'"%UName
       var.execute(a)
       a1    = var.fetchall()# 
       sql.commit()
       for i in a1:
            x = i
            for h in x:
                k = h#පළමු වතාවට ඇතුලත් කරන  User Name හරි නම් මෙහි ඇත 
       if len(a1) > 0 : 
            Paswd = getpass.getpass("\t\tEnter Password :")
            var2 = sql.cursor()
            f    = "select User_type.userType from user_type inner join user_password on user_type.UserName = user_password.UserName where password = '%s'"%Paswd        
            var2.execute(f)
            f1   = var2.fetchall()
            sql.commit()
            for T1 in f1:
                for T2 in T1:
                    SK = T2
            if len(f1) == 1 and SK == k:
                T = k+','+Paswd
                return T#ඇතුළත් කරන ලද  User Name එක Password සමග ගැළපේ නම් එය output වේ.(කලින් කරේ database එකේ ඒ  User Name හෝ  Password එක තියනව ද කියල විතරයි.)
            else:
                while True:
                    print("\t\t__________________________________________")
                    print("\t\t****You Password is wrong & not match.****")
                    print("\t\t------------------------------------------")
                    Paswd1 = getpass.getpass("\t\tEnter Password :")
                    var3 = sql.cursor()
                    Y1   = "select User_type.userType from user_type inner join user_password on user_type.UserName = user_password.UserName where password = '%s'"%Paswd1                   
                    var3.execute(Y1)
                    Y2 = var3.fetchall()
                    sql.commit()
                    for IT in Y2:
                        FG = IT
                        for D5 in FG:
                            GT = D5
                    if (len(Y2) == 1):
                        if GT == k:
                           ER = k+','+Paswd1
                           return ER
                           break
                    
       if len(a1) == 0:
           while True:
                print("\t\t__________________________________________")
                print("\t\t********** Your user name wrong **********")
                print("\t\t------------------------------------------")                
                UName = input("\t\tEnter User Name :")
                var1   = sql.cursor()
                b     = "select UserType from User_Type where UserType = '%s'"%UName
                var1.execute(b)
                b1    = var1.fetchall()#අපි  දෙන  User Name වැරදියි  නම්  empty list එකක්  සැදේ 
                sql.commit()
                for s in b1:
                    d = s 
                    for f in d:
                        g = f#පළමු වතාවට ඇතුලත් කරලා User Name වැරදිලා ඉන් පසු නිවැරදිව ඇතුළත් ඇතුළත් කරන ලද User Name එක මෙහි ඇත
                if len(b1) > 0 :
                    break                
           if len(b1) > 0 :
                Paswd2 = getpass.getpass("\t\tEnter Password :")
                var4   = sql.cursor()
                F      = "select User_type.userType from user_type inner join user_password on user_type.UserName = user_password.UserName where password = '%s'"%Paswd2                
                var4.execute(F)
                F1     = var4.fetchall()
                sql.commit()
                for V in F1:
                    for JL in V :
                        FR = JL
                if len(F1) == 1 and FR == g :
                    Lp = g+','+Paswd2
                    return Lp                    
                else : 
                    while True:
                        print("\t\t__________________________________________")
                        print("\t\t****You Password is wrong & not match.****")
                        print("\t\t------------------------------------------")
                        Paswd3 = getpass.getpass("\t\tEnter Password :")
                        var5   = sql.cursor()
                        U      = "select User_type.userType from user_type inner join user_password on user_type.UserName = user_password.UserName where password = '%s'"%Paswd3
                        var5.execute(U)
                        U1     = var5.fetchall()
                        sql.commit()
                        for WE in U1 :
                            Dk = WE
                            for ET in Dk :
                                Fj = ET
                        if len(U1) == 1 :
                            if Fj == g:
                                ex = g+','+Paswd3
                                return ex
                                break                                                             
dk = Login()
######################################### User Name සහ Password පරික්ෂා කිරිම ####################################################### 
A = dk.split(',')#[owner,077069]පරික්ෂා කර ලබා ගන්නා  User Name,Password ඇතුළත් ලැයිස්තුව

def Owner():
    print("\n")
    print("\t\tPress 1 for App Manager")
    print("\t\tPress 2 for Emp Manager")
    print("\n")
    print("\t\t-------------------------------------------")
    chi = input("\t\tEnter your choice :")
    if (chi != '1') and (chi != '2'):
        while True:
            print("\t\t___________________________________________")
            print("\t\t-------- Your choice out of range. --------")
            print("\t\t-------------------------------------------")
            chi = input("\t\tEnter your choice :")
            if (chi == '1') or (chi == '2'):
                break
    return chi# '1' or '2' 
def EmpManger():
    print("\n")
    print("\t\t----- Synex Salary Management System ------") 
    print("\n")
    back1 = input("\t\tGo Back :")
    if (back1 == '000') and (A[0] == 'owner'):
        EV = Owner()#EV = 1 or 2
        if EV == '1':
            print("\n")
            print("\t\t----------- Super User(Owner) -------------")
            print("\n")
            back0 = input("\t\tGo Back :")
            if back0 == '000':
                FD = Owner()#FD = 1 or 2
                if FD == '1':
                    FD = AppManger()
                elif FD == '2' :
                    FD = EmpManger()        
            else:
                print("\n")
                print("\t\t________________ Owner Menu _______________")
                print("\n")        
                print("\t\tPress 1 for Add New App User.")
                print("\t\tPress 2 for Remove App User.")
                print("\t\tPress 3 for Add New Profession.")
                print("\t\tPress 4 for Change the Profession Details.")
                print("\t\tPress 5 for Delete Profession.")
                print("\t\tPress 6 for Load Data File.")
                print("\t\tPress 7 for Delete Employee Date.")
                print("\t\t___________________________________________")
                MNO = input("\t\tEnter Your Choice :")
                if int(MNO) > 7 :
                    while True :
                       print("\n")
                       print("\t\t******** Your Choice Out Of Range ********")
                       print("\t\t__________________________________________") 
                       MNO = input("\t\tEnter Your Choice :")
                       if int(MNO) <= 7 :######################################### MNO(APP Manager) ################################
                           break
                if MNO == '1':
                    Appusers()
                if MNO == '2':
                    RAppuser()
                if MNO == '3':
                    NProfession()
                if MNO == '4':
                    CProfession()
                if MNO == '5':
                    DelProfession() 
                if MNO == '6':
                    LoadData()
                if MNO == '7':
                    deldata()                    
        if EV == '2':
            EmpManger()
    elif (back1 == '000') and (A[0] == 'admin'):
        print("\n")
        Login()
        EmpManger()
              
    else:
        print("\n")
        print("\t\t________________ Admin Menu _______________")
        print("\n")
        print('''\t\t*Press 1 for Creating Employee Salary Sheet 
                 for Company.''')
        print('''\t\t*Press 2 for Calculating total taxes from all 
                 employees in each month.''')
        print('''\t\t*Press 3 for Calculating the Company Profit 
                 in Each Month.''')
        print('''\t\t*Press 4 for Creating Year Salary Report for 
                 Employee.''')
        print('''\t\t*Press 5 for Creating Salary Report of an 
                 Employee for Specific Month.''')
        print("\t\t___________________________________________")
        KLJ = input("\t\tEnter Your Choice :")
        if int(KLJ) > 5 :
            while True :
                print("\n")
                print("\t\t******** Your Choice Out Of Range ********")
                print("\t\t__________________________________________") 
                KLJ = input("\t\tEnter Your Choice :")
                if int(KLJ) <= 5 :######################################### KLJ(EMP Manager) ############################
                    break                                           
        if KLJ == '1':
            SalarySheet()
        if KLJ == '2':
            TaxSheet()
        if KLJ == '3':
            ComSallary()
        if KLJ == '4':
            yearemp() 
        if KLJ == '5':
            MonthEmp()            
def SalarySheet():
    print("\n")
    print("\t\t_______Creating Employee Salary Sheet______")
    print("\n")
    back9 = input("\t\tGo Back :")
    if back9 == '000':
        EmpManger()
    elif back9 == '': 
        print("\n")        
        rat = []
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
        tex.close() 
        print("\t\t___Your SalarySheet Create successfully.___")     
        print("\n")
        back9 = input("\t\tGo Back :")
        if back9 == '000':
            EmpManger() 
def TaxSheet():
    print("\n")
    print("\t\tToatal tax in each month from all employees")
    print("\n")    
    back10 = input("\t\tGo Back :")
    if back10 == '000':
        EmpManger()
    elif back10 == '':
        det = ["_1Tax","_2Tax","_3Tax","_4Tax","_5Tax","_6Tax","_7Tax","_8Tax","_9Tax","_10Tax","_11Tax","_10Tax",]
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
            total.append(bik0) 
        del total[12]    
        List = ['January  ','February ','March    ','April    ','May      ','June     ','July     ','August   ','September','October  ','November ','December ']
        print("\n")
        for htt in range(12):
            print("\t\t",List[htt],':',total[htt])
    print("\n")    
    back10 = input("\t\tGo Back :")
    if back10 == '000':
        EmpManger() 
def ComSallary():
    print("\n")
    print("\t\t_______Company Profit in Each Month________")
    print("\n")
    back11 = input("\t\tGo Back :")
    print("\n")
    if back11 == '000':
        EmpManger()
    elif back11 == '':
        dep = ["_1FullSalary","_2FullSalary ","_3FullSalary","_4FullSalary","_5FullSallary"," _6FullSallary ","_7FullSallary","_8FullSalary","_9FullSallary","_10FullSallary","_11FullSallary","_12FullSallary",]        
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
            print('\t\t',monthk[tep],':',profit[tep])
    print("\n")
    back11 = input("\t\tGo Back :")
    if back11 == '000':
        EmpManger()  
def yearemp():
    print("\n")
    print("\t\t____Creating Employee Year Salary Sheet.___")
    print("\n")
    back12 = input("\t\tGo Back :")
    print("\n")
    if back12 == '000':
        EmpManger()
    elif back12 == '':
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
                print("\t\t___________________________________________")
                print("\t\t******This Index is not our databases******")
                print("\n")
                Input = input("\t\tEnter Index Number :")
                if Input in index:
                    break     
        if  Input in index:
            days = ['January   :','February  :','March     :','April     :','May       :','June      :','July      :','August    :','September :','October   :','November  :','December  :']
            grosssalary = ['_1FullSalary','_2FullSalary','_3FullSalary','_4FullSalary','_5FullSallary ','_6FullSallary','_7FullSallary','_8FullSalary','_9FullSallary','_10FullSallary','_11FullSallary','_12FullSallary']
            Deducation = ['_1deducations','_2deducations','_3deducations','_4deducations','_5deducations','_6deducations','_7deducations','_8deducations ','_9deducations','_10deducations','_11deducations','_12deducations']
            netsallary = ['_1NetSallary','_2NetSallary','_3NetSallary','_4NetSallary','_5NetSallary','_6NetSallary','_7NetSallary','_8NetSallary','_9NetSallary','_10NetSallary','_11NetSallary','_12NetSallary']
            nik = []
            name = sql.cursor()
            van = "select Name from monthly_details where EIndex = '%s'"%Input
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
                pt.writelines(days[fy]+"\t"+tes.pop(0)+"\t\t\t"+tes.pop(0)+"\t\t\t"+tes.pop(0)+"\n")
            pt.close() 
            print("\n")
            print("\t\t********Your Salary Report Created.********")   
    print("\n")
    back12 = input("\t\tGo Back :")
    if back12 == '000':
        EmpManger()        
def MonthEmp():
    print("\n")
    print("\t\t______Report Of An Employee For Month______")
    print("\n")
    back13 = input("\t\tGo Back :")
    if back13 == '000':
        EmpManger()
    elif back13 == '':
        print("\n")
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
                print("\t\t___________________________________________")
                print("\t\t*****This Index is not our databases*******")
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
                 NAME = nik[0]
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
                 print("\t\t********Your Salary Report Created.********")    
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
            print("\n")
            back13 = input("\t\tGo Back :")
            if back13 == '000':
                EmpManger()                
def EmpManger():
    print("\n") 
    print("\t\t----- Synex Salary Management System ------") 
    print("\n")
    back1 = input("\t\tGo Back :")
    if (back1 == '000') and (A[0] == 'owner'):
        EV = Owner()#EV = 1 or 2
        if EV == '1':
            print("\n")
            print("\t\t----------- Super User(Owner) -------------")
            print("\n")
            back0 = input("\t\tGo Back :")
            if back0 == '000':
                FD = Owner()#FD = 1 or 2
                if FD == '1':
                    FD = AppManger()
                elif FD == '2' :
                    FD = EmpManger()        
            else:
                print("\n")
                print("\t\t________________ Owner Menu _______________")
                print("\n")        
                print("\t\tPress 1 for Add New App User.")
                print("\t\tPress 2 for Remove App User.")
                print("\t\tPress 3 for Add New Profession.")
                print("\t\tPress 4 for Change the Profession Details.")
                print("\t\tPress 5 for Delete Profession.")
                print("\t\tPress 6 for Load Data File.")
                print("\t\tPress 7 for Delete Employee Date.")
                print("\t\t___________________________________________")
                MNO = input("\t\tEnter Your Choice :")
                if int(MNO) > 7 :
                    while True :
                       print("\n")
                       print("\t\t******** Your Choice Out Of Range ********")
                       print("\t\t__________________________________________") 
                       MNO = input("\t\tEnter Your Choice :")
                       if int(MNO) <= 7 :######################################### MNO(APP Manager) ################################
                           break
                if MNO == '1':
                    Appusers()
                if MNO == '2':
                    RAppuser()
                if MNO == '3':
                    NProfession()
                if MNO == '4':
                    CProfession()
                if MNO == '5':
                    DelProfession() 
                if MNO == '6':
                    LoadData()
                if MNO == '7':
                    deldata()                    
        if EV == '2':
            EmpManger()
    elif (back1 == '000') and (A[0] == 'admin'):
        print("\n")
        Login()
        EmpManger()
              
    else:
        print("\n")
        print("\t\t________________ Admin Menu _______________")
        print("\n")
        print('''\t\t*Press 1 for Creating Employee Salary Sheet 
                 for Company.''')
        print('''\t\t*Press 2 for Calculating total taxes from all 
                 employees in each month.''')
        print('''\t\t*Press 3 for Calculating the Company Profit 
                 in Each Month.''')
        print('''\t\t*Press 4 for Creating Year Salary Report for 
                 Employee.''')
        print('''\t\t*Press 5 for Creating Salary Report of an 
                 Employee for Specific Month.''')
        print("\t\t___________________________________________")
        KLJ = input("\t\tEnter Your Choice :")
        if int(KLJ) > 5 :
            while True :
                print("\n")
                print("\t\t******** Your Choice Out Of Range ********")
                print("\t\t__________________________________________") 
                KLJ = input("\t\tEnter Your Choice :")
                if int(KLJ) <= 5 :######################################### KLJ(EMP Manager) ############################
                    break                                           
        if KLJ == '1':
            SalarySheet()
        if KLJ == '2':
            TaxSheet()
        if KLJ == '3':
            ComSallary()
        if KLJ == '4':
            yearemp()
        if KLJ == '5':
            MonthEmp()
def Appusers():
    print("\n")
    print("\t\t_______________Add New App User____________")
    print("\n")
    back2 = input("\t\tGo Back :") 
    if back2 == '000':
        AppManger()
    elif back2 == "" :
        L1 = []
        print("\n")
        U_Name = input("\t\tEnter User Name :")
        var8 = sql.cursor()
        SD   = "select UserName from user_password"
        var8.execute(SD)
        FGH = var8.fetchall()
        for KF in FGH:
            y1 = KF
            for v8 in y1:
                L1.append(v8)
        if U_Name in L1 :#user name එක වගුවේ  තිබේ නම් එය නැවත නැවත ලබා ගැනීම
            while True:
                print("\t\t____________________________________________")
                print("\t\t******* You can't use this user name. ******")
                print("\t\t--------------------------------------------")
                U_Name = input("\t\tEnter User Name :")
                if U_Name not in L1 :
                    break         
        if U_Name not in L1:#user name එක වගුවේ නැත්නම් එය ඇතුළත් කර ගැනීම
            UPaswd = getpass.getpass("\t\tEnter User Password :")
            UPaswd1 = getpass.getpass("\t\tConfirm Password :")
            if UPaswd != UPaswd1 :#මුර පද දෙක ම අසමානනම් එය නැවත නැවත ලබා ගැනීම
                while True:
                    print("\t\t____________________________________________")
                    print("\t\t******** Your Password is not match ********")
                    print("\t\t--------------------------------------------")
                    UPaswd1 = getpass.getpass("\t\tConfirm Password :")
                    if UPaswd == UPaswd1 :
                        break
            if UPaswd == UPaswd1 :            
                L2 = []
                var10 = sql.cursor()
                Q     = "select password from user_password"
                var10.execute(Q)
                Q1 = var10.fetchall()
                for Ot in Q1:
                    Ot1 = Ot
                    for Ot2 in Ot1:
                        L2.append(Ot2)#DataBase එකෙන් ගත්ත ඔක්කොම Password ලැයිස්තුව
                   
                if UPaswd1 in L2:#Data Basse එකේ  Password තැබේ දැයි බැලීම
                    while True:
                        print("\t\t____________________________________________")
                        print("\t\t******* You Can't Use this Password ********")
                        print("\t\t--------------------------------------------")
                        UPaswd =  getpass.getpass("\t\tEnter User Password :")  
                        UPaswd1 = getpass.getpass("\t\tConfirm Password :")
                        if UPaswd != UPaswd1 :
                            while True:
                                print("\t\t____________________________________________")
                                print("\t\t******** Your Password is not match ********")
                                print("\t\t--------------------------------------------")
                                UPaswd1 = getpass.getpass("\t\tConfirm Password :")
                                if UPaswd == UPaswd1 and UPaswd1 not in L2 :
                                    break 
                   
                if UPaswd1 not in L2 :
                    var11 = sql.cursor()
                    Du    = "insert into user_password values('%s','%s')"%(U_Name,UPaswd1)
                    var11.execute(Du)
                    sql.commit()
                    UType = input("\t\tEnter User Type (admin/owner):")
                    if (UType == 'admin') or (UType == 'owner') :
                        var12 = sql.cursor()
                        Oz    = "insert into user_type values('%s','%s')"%(U_Name,UType)
                        var12.execute(Oz)
                        sql.commit()
                        
                    else:
                        while True:
                            print("\t\t____________________________________________")                        
                            print("\t\t*Your can select user types admin or owner*")
                            print("\t\t--------------------------------------------")
                            UType = input("\t\tEnter User Type (admin/owner):")
                            if (UType == 'admin') or (UType == 'owner'):
                                break
                        var12 = sql.cursor()
                        Oz    = "insert into user_type (UserName,UserType)values('%s')"%U_Name,UType
                        var12.execute(Oz)
                        sql.commit()
                print("\t\t____________ Change successfully.___________") 
    back2 = input("\t\tGo Back :") 
    if back2 == '000':
        AppManger()            
                
def RAppuser():
    print("\n")
    print("\t\t______________ Remove App User _____________")
    print("\n")
    back3 = input("\t\tGo Back :")
    if back3 == '000':
        AppManger() 
    elif back3 == '' :
        print("\n")
        DName = input("\t\tEnter User Name :")
        Sure  = input("\t\tAre You Sure??,You want to remove (Y/N) :")
        if Sure == "Y" :
            var13 = sql.cursor()
            UK    = "delete from user_type where UserName = '%s'"%DName
            var13.execute(UK)
            sql.commit()
            var14 = sql.cursor()
            Uk    = "delete from user_password where UserName = '%s'"%DName
            var14.execute(Uk)
            sql.commit()
            print("\n")
            print("\t\t________ your removed successfully. ________")
        else :
            print("\n")
            print("\t\t____________________ Ok ____________________")  
    print("\n")
    back3 = input("\t\tGo Back :")
    if back3 == '000':
        AppManger()              
    
def NProfession():
    print("\n")
    print("\t\t____________ Add New Profession ___________")
    print("\n")    
    back4 = input("\t\tGo Back :")
    if back4 == '000':
        AppManger()
    elif back4 == '':
        print("\n")
        RX    = []#profession code සියල්ල මෙම ලැයිස්තුවේ ඇත(DataBase එකෙන් ලබා ගත්)
        vas   = sql.cursor()
        KD_   = "select profession_code from profession"
        vas.execute(KD_)
        KD1_  = vas.fetchall()
        for qc in KD1_ :
            for qc1 in qc:
                RX.append(qc1)             
        Code  = input("\t\tEnter Profession Code :")
        if Code in RX :#profession code එක  RX ලැයිස්තුවේ නොමැති දැයි පරික්ෂා කිරීම
            while True:
                print("\t\t___________________________________________")
                print("\t\t*This profession code is currently in use**")
                print("\t\t-------------------------------------------")
                Code = input("\t\tEnter Profession Code :")
                if Code not in RX :
                    break  
        do = []#Profession Name සියල්ල මෙම ලැයිස්තුවේ ඇත(DataBase එකෙන් ලබා ගත්)
        vas0 = sql.cursor()
        qk   = "select profession from  profession"
        vas0.execute(qk)
        qk1  = vas0.fetchall()
        for kl in qk1:
            for dk_ in kl:
                do.append(dk_)                 
        PName = input("\t\tEnter Profession :") 
        if PName in do :
            while True: 
                print("\t\t___________________________________________")
                print("\t\t*This profession name is currently in use**")
                print("\t\t-------------------------------------------")
                PName = input("\t\tEnter Profession :") 
                if PName not in do :
                    break                
        Rate  = float(input("\t\tEnter Daily Rate :"))
        vas1 = sql.cursor()
        pi   = "insert into profession values('%s','%s',%.2f)"%(PName,Code,Rate)
        vas1.execute(pi)
        sql.commit()
        print("\t\t__________ Your Add successfully ___________")   
    print("\n")    
    back4 = input("\t\tGo Back :")
    if back4 == '000':
        AppManger()    
def CProfession():
    print("\n")
    print("\t\t________ Change Profession Details ________")
    print("\n")
    back5 = input("\t\tGo Back :")
    if back5 == '000':
        AppManger()
    elif back5 == '':
        print("\n")
        qj = input("\t\tEnter Profession Code :")
        ec = []
        vas2 = sql.cursor()
        bk   = "select profession_code from profession"
        vas2.execute(bk)
        E_ = vas2.fetchall()
        sql.commit()
        for gz in E_:
            for gz1 in gz :
                ec.append(gz1)
        if qj not in ec :
            while True:
                print("\t\t___________________________________________")
                print('''\t\t****There is no details related to this**** 
                                profession code.''')
                print("\t\t-------------------------------------------")                
                qj = input("\t\tEnter Profession Code :")
                if qj in ec :
                    break                
        if qj in ec:
            print("\t\t____________________________________________")
            JI = []
            vas3 = sql.cursor()
            xo   = "select * from profession where profession_code ='%s'"%qj
            vas3.execute(xo)
            xo1  = vas3.fetchall()
            sql.commit()
            for Tk in xo1:
                Tk1 = Tk
                for TK in Tk1:
                   JI.append(TK) 
            print("\t\t\tProfession Code :%s"%JI[1])
            print("\t\t\tProfession :%s"%JI[0])
            print("\t\t\tDaily Rate :%.2f"%JI[2])  
            print("\t\t____________________________________________")
            print("\t\tWhat do you want to changes?")
            print("\t\t\tProfession Name(N)")
            print("\t\t\tDaily Rate(R)")
            print("\t\t\tBoth(B)") 
            print("\n")
            CHo  = input("\t\tEnter Choice :")
            U_K = ['N','R','B']
            if CHo not in U_K :
                while True:
                    print("\t\t____________________________________________")
                    print("\t\t******** Your choice out of range. *********")
                    print("\t\t--------------------------------------------")                    
                    CHo  = input("\t\tEnter Choice :")
                    if CHo in U_K :
                        break
            if CHo == 'N':
                Use = input("\t\tEnter New Profession Name :")
                vas4 = sql.cursor()
                se   = "update profession set profession = '%s' where profession_code = '%s'"%(Use,qj)#qj තමා  profession_code එක
                vas4.execute(se)
                sql.commit()
                print("\t\t___________ Change successfully ___________")
            elif CHo == 'R':
                Use1 = float(input("\t\tEnter New Daily Rate(Fee) :"))
                vas5 = sql.cursor()
                ly   = "update profession set Daily_Fee = %.2f where profession_code = '%s'"%(Use1,qj)
                vas5.execute(ly)
                sql.commit()
                print("\t\t___________ Change successfully ___________")                
            elif CHo == 'B':
                Use2 = input("\t\tEnter New Profession Name :")
                Use3 = float(input("\t\tEnter New Daily Rate :"))
                vas6 = sql.cursor()
                T_U  = "update profession set profession = '%s',Daily_Fee = %.2f where profession_code = '%s'"%(Use2,Use3,qj)
                vas6.execute(T_U)
                sql.commit()
                print("\t\t___________ Change successfully ___________")
    print("\n")
    back5 = input("\t\tGo Back :")
    if back5 == '000':
        AppManger() 
def DelProfession():
    print("\n")
    print("\t\t----------- Delete Profession -------------")
    print("\n")
    back6 = input("\t\tGo Back :")
    if back6 == '000':
        AppManger()
    elif back6 == '':
        print("\n")
        DEL = []
        DelP =input("\t\tEnter Profession Code You Want to Delete :")
        vak  = sql.cursor()
        In   = "select Profession_code from profession"
        vak.execute(In)
        In1 = vak.fetchall()
        for _ET in In1:
            for In2 in _ET :
                DEL.append(In2)       
        if DelP not in DEL :
            while True:
                 print("\t\t__________________________________________")
                 print("\t\t******This profession code not inuse******")
                 print("\t\t------------------------------------------")
                 print("\n")
                 DelP =input("\t\tEnter Profession Code You Want to Delete :")
                 if DelP in DEL:
                    break
        Lik = ['Y','N']
        Like = input("\t\tAre You Sure??,You Want to Remove(Y/N) :")
        if Like not in Lik:
            while True:
                print("\t\t__________________________________________")
                print("\t\t********* Your select is wrong ***********")  
                print("\t\t------------------------------------------")
                Like = input("\t\tAre You Sure??,You Want to Remove(Y/N) :")
                if Like in Lik:
                    break
        if Like == 'Y' :
            vak1 = sql.cursor()
            SF_  = "delete from profession where profession_code = '%s'"%DelP
            vak1.execute(SF_)
            sql.commit()
            print("\n")
            print("\t\t___Your Delete Profession successfully____") 
        if Like == 'N':
            print("\n")
            print("\t\t_______Your Delete Profession Cancel______")
    print("\n")
    back6 = input("\t\tGo Back :")
    if back6 == '000':
        AppManger()            
def LoadData():
    print("\n")
    print("\t\t----------- Load Employee Data ------------")
    print("\n")
    back7 = input("\t\tGo Back :")
    if back7 == '000':
        AppManger()
    elif back7 == '':
        print("\n")
        Ful = []
        vat0 = sql.cursor()
        Hu   = "show tables"
        vat0.execute(Hu)
        Hu1 = vat0.fetchall()
        sql.commit()
        for DKJ in Hu1:
            for DKJ1 in DKJ:
                Ful.append(DKJ1)
        if 'employee_data'not in Ful:        
             vat = sql.cursor()
             pu  = "create table Employee_Data(EMPIndex char(6) primary key,EMPName varchar (80),code char(50),January int(5),February int(5),March int(5),April int(5),May int(5),June int(5),July int(5),August int(5),September int(5),Octob int(5),Novem int(5),Decem int(5))"
             vat.execute(pu)
             sql.commit()    
             GET = input("\t\tEnter Data File Name  :")        
             FUK = open(GET,'r')
             for line in FUK:
                Ra =line.split("\t")#[]
                p_s =Ra.pop(14)
                esa =p_s.split()
                Ra.append(esa[0])
                vat1 = sql.cursor()
                Bc   = "insert into employee_data values('%s','%s','%s',%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f)"%(Ra[0],Ra[1],Ra[2],int(Ra[3]),int(Ra[4]),int(Ra[5]),int(Ra[6]),int(Ra[7]),int(Ra[8]),int(Ra[9]),int(Ra[10]),int(Ra[11]),int(Ra[12]),int(Ra[13]),int(Ra[14]))
                vat1.execute(Bc)
                sql.commit()
             FUK.close()   
             vau0 = sql.cursor()
             i3   = "create table Monthly_Details(EIndex char(6)primary key,Name varchar(80),Pro varchar(20),_1FullSalary float(50),_1deducations float(50),_1NetSallary float(50),_1Tax float(50),_2FullSalary float(50),_2deducations float(50),_2NetSallary float(50),_2Tax float(50),_3FullSalary float(50),_3deducations float(50),_3NetSallary float(50),_3Tax float(50),_4FullSalary float(50),_4deducations float(50),_4NetSallary float(50),_4Tax float(50),_5FullSallary float(50),_5deducations float(50),_5NetSallary float(50),_5Tax float(50),_6FullSallary float(50),_6deducations float(50),_6NetSallary float(50),_6Tax float(50),_7FullSallary float(50),_7deducations float(50),_7NetSallary float(50),_7Tax float(50),_8FullSalary float(50),_8deducations float(50),_8NetSallary float(50),_8Tax float(50),_9FullSallary float(50),_9deducations float(50),_9NetSallary float(50),_9Tax float(50),_10FullSallary float(50),_10deducations float(50),_10NetSallary float(50),_10Tax float(50),_11FullSallary float(50),_11deducations float(50),_11NetSallary float(50),_11Tax float(50),_12FullSallary float(50),_12deducations float(50),_12NetSallary float(50),_12Tax float(50))"              
             vau0.execute(i3)
             sql.commit()
             def FullSallary(Index,Name,Place,January,February,March,April,May,June,July,August,September,October,November,December):
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
                FullSallary =[]
                EPFLi = []
                Tax_  = []    
                Netsalary = []
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
                bee ="insert into monthly_details values('%s','%s','%s',%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f)"%(Es[0],Es[1],Es[14],FullSallary[0],EPFLi[0]+Tax_[0]+500,Netsalary[0],Tax_[0],FullSallary[1],EPFLi[1]+Tax_[1]+500,Netsalary[1],Tax_[1],FullSallary[2],EPFLi[2]+Tax_[2]+500,Netsalary[2],Tax_[2],FullSallary[3],EPFLi[3]+Tax_[3]+500,Netsalary[3],Tax_[3],FullSallary[4],EPFLi[4]+Tax_[4]+500,Netsalary[4],Tax_[4],FullSallary[5],EPFLi[5]+Tax_[5]+500,Netsalary[5],Tax_[5],FullSallary[6],EPFLi[6]+Tax_[6]+500,Netsalary[6],Tax_[6],FullSallary[7],EPFLi[7]+Tax_[7]+500,Netsalary[7],Tax_[7],FullSallary[8],EPFLi[8]+Tax_[8]+500,Netsalary[8],Tax_[8],FullSallary[9],EPFLi[9]+Tax_[9]+500,Netsalary[9],Tax_[9],FullSallary[10],EPFLi[10]+Tax_[10]+500,Netsalary[10],Tax_[10],FullSallary[11],EPFLi[11]+Tax_[11]+500,Netsalary[11],Tax_[11])    
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
                FullSallary(Dic[0],Dic[1],Dic[2],Dic[3],Dic[4],Dic[5],Dic[6],Dic[7],Dic[8],Dic[9],Dic[10],Dic[11],Dic[12],Dic[13],Dic[14])        
             print("\t\t____________________________________________")             
             print("\t\t***********Upload data Successfully*********")
             print("\t\t--------------------------------------------")             
             
        else:
             print("\t\t____________________________________________")
             print("\t\t*******This data is already included********")
             print("\t\t--------------------------------------------")             
        print("\n")
        back7 = input("\t\tGo Back :")
        if back7 == '000':
            AppManger()             
def deldata():
    print("\n")
    print("\t\t--------- Delete Employee Data ------------")
    print("\n")
    back8 = input("\t\tGo Back :")
    if back8 == '000':
        AppManger()
    elif back8 == '':
        print("\n")
        Pasc = getpass.getpass("\t\tEnter Login Password :")
        if Pasc != A[1] :
            while True:
                print("\t\t___________________________________________")
                print("\t\t********* Your Password is wrong **********")            
                print("\t\t-------------------------------------------")
                print("\n")
                Pasc = getpass.getpass("\t\tEnter Login Password :")
                if Pasc == A[1]:
                    break                
        if Pasc == A[1] :
            Shu = input('''\t\tAre You Sure?You want to delete all 
                                employee data?(Y/N) :''') 
            tuk = ['Y','N']
            if Shu not in tuk:
                while True:
                    print("\t\t___________________________________________")
                    print("\t\t*********You selected wrong type***********")
                    print("\t\t-------------------------------------------")
                    Shu = input('''\t\tAre You Sure?You want to delete all 
                                employee data?(Y/N) :''')
                    if Shu in tuk :
                        break
            if Shu in tuk :
                if Shu == 'Y':
                    van = sql.cursor()
                    lop = "drop table employee_data"
                    van.execute(lop)
                    sql.commit()
                    vag = sql.cursor()
                    lop1 = "drop table monthly_details"
                    vag.execute(lop1)
                    sql.commit()
                    print("\t\t__________Successfull Delete Data__________")
                if Shu == 'N':
                    print("\t\t____________ Cancel Delete Data ___________")   
        print("\n")
        back8 = input("\t\tGo Back :")
        if back8 == '000':
            AppManger()            
def AppManger():
    print("\n")
    print("\t\t----------- Super User(Owner) -------------")
    print("\n")
    back0 = input("\t\tGo Back :")
    if back0 == '000':
        FD = Owner()#FD = 1 or 2
        if FD == '1':
            FD = AppManger()
        elif FD == '2' :
            FD = EmpManger()        
    else:
        print("\n")
        print("\t\t________________ Owner Menu _______________")
        print("\n")        
        print("\t\tPress 1 for Add New App User.")
        print("\t\tPress 2 for Remove App User.")
        print("\t\tPress 3 for Add New Profession.")
        print("\t\tPress 4 for Change the Profession Details.")
        print("\t\tPress 5 for Delete Profession.")
        print("\t\tPress 6 for Load Data File.")
        print("\t\tPress 7 for Delete Employee Date.")
        print("\t\t___________________________________________")
        MNO = input("\t\tEnter Your Choice :")
        if int(MNO) > 7 :
                while True :
                    print("\n")
                    print("\t\t******** Your Choice Out Of Range ********")
                    print("\t\t__________________________________________") 
                    MNO = input("\t\tEnter Your Choice :")
                    if int(MNO) <= 7 :######################################### MNO(APP Manager) ################################
                        break
        if MNO == '1':
            Appusers()
        if MNO == '2':
            RAppuser() 
        if MNO == '3':
            NProfession()
        if MNO == '4':
            CProfession()
        if MNO == '5':
            DelProfession()
        if MNO == '6':
            LoadData()
        if MNO == '7':
            deldata()        
def change():
    L = []
    print('\n')
    cha1 = input("\t\tWould you change your password(Y/N) :")
    if cha1 == 'Y':
        print("\n")
        cha2 = getpass.getpass("\t\tEnter your new password :")
        var7 = sql.cursor()
        K    = "select password from user_password"
        var7.execute(K)
        Fg  = var7.fetchall()
        sql.commit()
        for DF in Fg:
            for KO in DF:
                L.append(KO)
        if cha2 in L:
            while True :
                print("\t\t___________________________________________")
                print("\t\t-------You can 't use this password.-------")
                print("\t\t-------------------------------------------")
                cha2 = getpass.getpass("\t\tEnter your new password :")
                if cha2 not in L:
                    break                 
            var6 = sql.cursor()
            ds   = "update user_password set password ='%s' where password = '077069'"%cha2
            var6.execute(ds)
            sql.commit()
            print("\n")
            print("\t\t---- Your password change sucsesfully. ----")
            print("\n")
            h2 = Owner()#h2 = '1' or '2'
            return h2
        else:
            var6 = sql.cursor()
            ds   = "update user_password set password ='%s' where password = '077069'"%cha2
            var6.execute(ds)
            sql.commit()
            print("\n")
            print("\t\t---- Your password change sucsesfully. ----")
            print("\n")
            h2 = Owner()#h2 = '1' or '2'
            return h2        
    else:   
        mn = Owner()
        return mn       
#__________________________________________________________________________________________________________________________        
if A[1] == '077069':#     පළමු වතාවට ලොග් උනහම පමණි 
    print("\n")
    print("\t\t********* You are logged as owner *********")  
    xz = change()#1 or 2
    if xz == '1':
        AppManger()
               
    if xz == '2':
        EmpManger()
        
elif (A[1] != '077069') and (A[0] == 'owner'):# ඉන් පසු ඕනෙම අවස්ථාවක  owner ලොග් ඌ විට
    print("\n")
    print("\t\t********* You are logged as owner *********")
    xy = Owner()#1 or 2
    if xy == '1':
        AppManger()            
    if xy == '2':
        EmpManger()
        
elif (A[1] != '077069') and (A[0] == 'admin'):#admin ගේ අවස්ථාව
    EmpManger()        


#__________________________________________________________________________________________________________________________
