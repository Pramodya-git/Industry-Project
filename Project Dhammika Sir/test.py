def Login():
   back = input("\t\tTo Exit :")
   print("\n")
   if back == '000':
       sys.exit()
   else :
       UName = input("\t\tEnter User Name :")
       var   = sql.cursor()
       a     = "select UserType from User_Type where UserType = '%s'"%UName
       var.execute(a)
       a1    = var.fetchall()#අපි  දෙන  User Name වැරදියි  නම්  empty list එකක්  සැදේ 
       sql.commit()
       for i in a1:
            x = i
            for h in x:
                k = h#
                if UName == k:#User Name හරි  නම්  මුර පදය ලබා ගනී
                    UPaswd = getpass.getpass("\t\tEnter Password :")
                    var1 = sql.cursor()
                    b    = "select Password from User_Password where Password = '%s'"%UPaswd
                    var1.execute(b)
                    b1   = var1.fetchall()#අපි  දෙන  මුර පදය වැරදියි  නම්  empty list එකක්  සැදේ 
                    sql.commit()
                    var9 = sql.cursor()
                    QW = "select User_type.userType from user_type inner join user_password on user_type.UserName = user_password.UserName where password = '%s'"%UPaswd
                    var9.execute(QW)
                    XS = var9.fetchall()
                    sql.commit()
                    if XS[0][0] == UName:
                        for u in b1:
                           o = u
                           for p in o:
                               f = p#
                               sc = k+','+f
                               return sc
                    else:
                        while True:
                            print("\t\t                    
                if len(b1) == 0 :
                        while True:
                            print("\t\t__________________________________________")
                            print("\t\t----------Your Password is Wrong.---------")
                            print("\t\t------------------------------------------")
                            UPaswd1 = getpass.getpass("\t\tEnter Password :")
                            var2 = sql.cursor()
                            c    = "select Password from User_Password where Password = '%s'"%UPaswd1
                            var2.execute(c)
                            c1 = var2.fetchall()
                            sql.commit()
                            for y in c1:
                                s = y
                                for z in s:
                                   e = z#නිවැරදී   මුර  පදය
                                   kl = k+','+e
                                   return kl
                                   print(e)
                            if len(c1) > 0 :
                                break
       if len(a1) == 0:
            while True:
                print("\t\t__________________________________________")
                print("\t\t-----------Your User Name Wrong.----------")
                print("\t\t------------------------------------------")
                UName2 = input("\t\tEnter User Name :")
                var3 = sql.cursor()
                v    = "select UserType from User_Type where UserType = '%s'"%UName2
                var3.execute(v)
                q    = var3.fetchall()
                sql.commit()
                if len(q) == 1:
                     break
            for k1 in q:
                k2 = k1
                for j1 in k2:
                    r1 = j1#නිවැරදී  User Name එක
            if UName2 == r1:
                UPaswd2 = getpass.getpass("\t\tEnter Password :")    
                var4 = sql.cursor()    
                z1   = "select Password from User_Password where Password = '%s'"%UPaswd2
                var4.execute(z1)
                bd = var4.fetchall()
                sql.commit()
                for km in bd :
                    rx = km
                    for lp in rx:
                        rs = lp
                        ms = r1+','+rs
                        return ms                        
            if  len(bd)==0:
                    while True:
                        print("\t\t__________________________________________")
                        print("\t\t----------Your Password is Wrong.---------")
                        print("\t\t------------------------------------------")
                        UPaswd3 = getpass.getpass("\t\tEnter Password :")
                        var5 = sql.cursor()
                        ef    = "select Password from User_Password where Password = '%s'"%UPaswd3
                        var5.execute(ef)
                        lm    = var5.fetchall()
                        sql.commit()
                        for fg in lm:
                            dk = fg
                            for sl in dk:
                                er = sl
                                kj = r1+','+er
                                return kj
                        if len(lm) > 0:
                            break                        
dk = Login()#owner,077069