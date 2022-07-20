import mysql.connector as c
mydb=c.connect(host="localhost",user="root",passwd="root")
mycursor=mydb.cursor()
nopp=0
lol=[]
lethim="NO"
try:
    query="create database client_info"
    mycursor.execute(query)
except:
    pass
try:
    query=("use client_info")
    mycursor.execute(query)
    query="create table account(name varchar(50),local_address varchar(50),email_address varchar(50),phone_number bigint,cc int primary key)" #cc=customer code
    mycursor.execute(query)
except:
    pass
try:
    query="create table points(name varchar(20),cc int primary key,pointss int default 0)"
    mycursor.execute(query)
except:
    pass
try:
    query="create database pc"
    mycursor.execute(query)
except:
    pass
try:
    query=("use pc")
    mycursor.execute(query)
    query="create table specifications(processor varchar(50),ram int,graphics_card varchar(20),storage_type varchar(20),psu int,pcc int primary key)" #pcc=pc code
    mycursor.execute(query)
except:
    pass
try:
    query="create table passwords(pcc int primary key,password int)"
    mycursor.execute(query)
except:
    pass
try:
    query="create database sign_out"
    mycursor.execute(query)
except:
    pass
try:
    query=("use sign_out")
    mycursor.execute(query)
    query="create table bill(cc int,name varchar(20),amount int)" 
    mycursor.execute(query)
except:
    pass
try:
    query=("use sign_out")
    mycursor.execute(query)
    query="create table utilization(cc int,hrs int,mins int)" 
    mycursor.execute(query)
except:
    pass
query=("use pc")
mycursor.execute(query)    
try:
    query="insert into specifications values('AMD Ryzen 9 3950X',16,'RTX 3080','SSD',650,101)"
    mycursor.execute(query)
except:
    pass
adminpass="123abcxyz"
try:
    query="insert into specifications values('Intel Core i5-10600K',12,'RTX 3060','SSD',550,102)"
    mycursor.execute(query)
except:
    pass
try:
    query="insert into specifications values('AMD Ryzen Threadripper 3960X',16,'RTX 3070','SSD',670,103)"
    mycursor.execute(query)
except:
    pass
try:
    query="insert into specifications values('Intel Core i9 12900K',32,'RTX 3090','SSD,HDD',820,104)"
    mycursor.execute(query)
except:
    pass
try:
    query="insert into specifications values('AMD Ryzen 7 5800X',8,'RTX 2060ti','HDD',630,105)"
    mycursor.execute(query)
except:
    pass
def insert_specs():
    pccode="invalid"
    ps=input("Enter the processor name:")
    rm=int(input("Enter the ram amount:"))
    gc=input("Enter the graphics card name:")
    st=input("Enter the storage type:")
    pw=int(input("Enter the power supply unit in watts:"))
    while pccode=="invalid":
        ppc=input("Enter the pc code:")  
        query=("use pc")
        mycursor.execute(query)
        query="insert into specifications values('{}',{},'{}','{}',{},{})".format(ps,rm,gc,st,pw,ppc)
        try:
            mycursor.execute(query)
            pccode="valid"
        except:
            print("Enter valid pc code")
            pccode="invalid"
    mydb.commit()
query=("use pc")
mycursor.execute(query)
try:
    query="insert into passwords values(101,79924)"
    mycursor.execute(query)
except:
    pass
try:
    query="insert into passwords values(102,87453)"
    mycursor.execute(query)
except:
    pass
try:
    query="insert into passwords values(103,90321)"
    mycursor.execute(query)
except:
    pass
try:
    query="insert into passwords values(104,45389)"
    mycursor.execute(query)
except:
    pass
try:
    query="insert into passwords values(105,18374)"
    mycursor.execute(query)
except:
    pass
def insert_password():
    pccode="invalid"
    psd=int(input("Enter the password you want to set:"))
    while pccode=="invalid":
        ppc=input("Enter the pc code:")  
        query=("use pc")
        mycursor.execute(query)
        query="insert into passwords values({},{})".format(ppc,psd)
        try:
            mycursor.execute(query)
            pccode="valid"
        except:
            print("Enter valid pc code:")
            pccode="invalid"
    mydb.commit()
def points():
    if alc=="y" or alc=="Y":
        query="use client_info"
        mycursor.execute(query) 
        query=("use client_info")
        mycursor.execute(query)
        query="select pointss from points where cc={}".format(cccc)
        mycursor.execute(query)
        np=mycursor.fetchall()
        def price():
            global nopp
            for uw in np:
                for wu in uw:
                    nopp=wu
            print("Available points",nopp)
        price()
        mydb.commit()
    else:
        query="use client_info"
        mycursor.execute(query)
        query=("use client_info")
        mycursor.execute(query)
        query="insert into points(name,cc)values('{}',{})".format(naam,cccc)
        mycursor.execute(query)
        query="select pointss from points where cc={}".format(cccc)
        mycursor.execute(query)
        np=mycursor.fetchall()
        def price():
            global nopp
            for uw in np:
                for wu in uw:
                    nopp=wu
            print("Available points",nopp)
        price()
        mydb.commit()
def usage():
    query="use sign_out"
    mycursor.execute(query)
    hrs=int(input("working hours:"))
    mins=int(input("working minutes:"))
    if alc not in ("y","Y"):
        query=("use sign_out")
        mycursor.execute(query)
        query="insert into utilization values({},{},{})".format(cccc,hrs,mins)
        mycursor.execute(query)
        mydb.commit()
    else:
        query=("use sign_out")
        mycursor.execute(query)
        query="insert into utilization values({},{},{})".format(cccc,hrs,mins)
        mycursor.execute(query)
        mydb.commit()
    def billing():
        k=mins+(hrs*60)
        amt=k*5
        if alc not in ("y","Y"):
            mydb.commit()
            points()
            bolde=input("Do you want to redeem your points(Y,N):")
            if bolde in ("Y","y"):
                offerp=amt-(nopp)*2
                if offerp<1:
                    offerp=1
                query="use client_info"
                mycursor.execute(query)
                query="update points set pointss=0 where cc={}".format(cccc)
                mycursor.execute(query)
                mydb.commit()
                if nopp==0:
                    query="update points set pointss=pointss+2 where cc={}".format(cccc)
                    mycursor.execute(query)
                    mydb.commit()
                print("AMOUNT BEFORE DISCOUNT",amt)
                print("THANK YOU YOUR DISCOUNTED AMOUNT IS",offerp)
                query="use sign_out"
                mycursor.execute(query)
                query="insert into bill values({},'{}',{})".format(cccc,naam,offerp)
                mycursor.execute(query)
                mydb.commit()
            else:
                print("THANK YOU YOUR AMOUNT IS",amt)
                query="use sign_out"
                mycursor.execute(query)
                query="insert into bill values({},'{}',{})".format(cccc,naam,amt)
                mycursor.execute(query)
                query="use client_info"
                mycursor.execute(query)
                query="update points set pointss=pointss+2 where cc={}".format(cccc)
                mycursor.execute(query)
                mydb.commit()
        else:
            points()
            bolde=input("Do you want to redeem your points(Y,N):")
            if bolde in ("Y","y"):
                offerp=amt-(nopp)*2
                if offerp<1:
                    offerp=1
                query="use client_info"
                mycursor.execute(query)
                query="update points set pointss=0 where cc={}".format(cccc)
                mycursor.execute(query)
                mydb.commit()
                if nopp==0:
                    query="update points set pointss=pointss+2 where cc={}".format(cccc)
                    mycursor.execute(query)
                    mydb.commit()
                print("AMOUNT BEFORE DISCOUNT",amt)
                print("THANK YOU YOUR DISCOUNTED AMOUNT IS",offerp)
                query="use sign_out"
                mycursor.execute(query)
                query="insert into bill values({},'{}',{})".format(cccc,naam,offerp)
                mycursor.execute(query)
                query="use client_info"
                mycursor.execute(query)
                query="update points set pointss=pointss+2 where cc={}".format(cccc)
                mycursor.execute(query)
                mydb.commit()
            else:
                query="update points set pointss=pointss+2 where cc={}".format(cccc)
                mycursor.execute(query)
                mydb.commit()
                print("THANK YOU YOUR AMOUNT IS",amt)
                query="use sign_out"
                mycursor.execute(query)
                query="insert into bill values({},'{}',{})".format(cccc,naam,amt)
                mycursor.execute(query)
                mydb.commit()
    billing()
def account():
    global cccc
    global naam
    global alc
    if telltruth in ("Y","y"):
        ccccc=int(input("Enter the customer code:"))
        if ccccc in lol:
            alc="y"
            cccc=ccccc
        else:
            print("We checked in our records you are not registered yet")
            alc="n"
    elif telltruth not in ("Y","y"):
        alc="n"
    if alc not in ("y","Y"):
        query="use client_info"
        mycursor.execute(query)
        ccode="invalid"
        naam=input("Enter the name:")
        la=input("Enter the local address:")
        ea=input("Enter the email address:")
        pn=int(input("Enter the phone number:"))
        while ccode=="invalid":
            cccc=input("Enter new customer code:")  
            query=("use client_info")
            mycursor.execute(query)
            query="insert into account values('{}','{}','{}',{},{})".format(naam,la,ea,pn,cccc)
            try:
                mycursor.execute(query)
                print("SUCCESSFULLY REGISTERD")
                ccode="valid"
            except Exception as f:
                print(f)
                print("Enter valid customer code, the one you entered is already in use:")
                pccode="invalid"
        mydb.commit()
    else:
        naam=input("Enter the name:")
        print("SUCCESSFULLY REGISTERD")
def update_pc():
    query="use pc"
    mycursor.execute(query)
    pce=int(input("Enter the pc code:"))
    choice="y"
    while choice in ("y","Y"):
        p=int(input("1 for processor\n2 for ram\n3 for graphics card\n4 for storage type\n5 for psu\nEnter the hardware to be upgraded"))
        if p==1:
            up=input("Enter the upgraded processor:")
            query="update specifications set processor='{}' where pcc={}".format(up,pce)
            mycursor.execute(query)
            mydb.commit()
        elif p==2:            
            up=int(input("Enter the upgraded ram:"))
            query="update specifications set ram={} where pcc={}".format(up,pce)
            mycursor.execute(query)
            mydb.commit()
        elif p==3:            
            up=input("Enter the upgraded graphics card:")
            query="update specifications set graphics_card='{}' where pcc={}".format(up,pce)
            mycursor.execute(query)
            mydb.commit()
        elif p==4:            
            up=input("Enter the upgraded storage type:")
            query="update specifications set storage_type='{}' where pcc={}".format(up,pce)
            mycursor.execute(query)
            mydb.commit()
        elif p==5:            
            up=int(input("Enter the upgraded psu:"))
            query="update specifications set psu={} where pcc={}".format(up,pce)
            mycursor.execute(query)
            mydb.commit()
        choice=input("Do you want to upgrade something else? (y/n):")
        if choice in ("Y","y"):
            choice="y"
            b=input("Do you want to upgrade the same pc or different one(s/d):?")
            if b in ("s","S"):
                pass
            elif b in ("d","D"):
                pce=int(input("Enter the pc code:"))
        elif choice in ("n","N"):
            choice="complete"
def change_password():
    choice2="y"
    while choice2 in ("y","Y"):
        query="use pc"
        mycursor.execute(query)
        validity="invalid"
        pct=int(input("Enter the pc code:"))
        new=int(input("Enter the new password:"))
        query="update passwords set password={} where pcc={}".format(new,pct)
        mycursor.execute(query)
        mydb.commit()
        bro=input("Do you want to change any other password(y,n):")
        if bro not in ("y","Y"):
            choice2="n"
print("ミ★ 𝘞𝘌𝘓𝘊𝘖𝘔𝘌 𝘛𝘖 𝘈𝘓𝘗𝘏𝘈 𝘊𝘠𝘉𝘌𝘙 𝘊𝘈𝘍𝘌 ★彡")
def clear_databases():
    query="drop database client_info"
    mycursor.execute(query)
    query="drop database pc"
    mycursor.execute(query)
    query="drop database sign_out"
    mycursor.execute(query)
    mydb.commit()
super_choice="y"
while super_choice in ("y","Y"):    
    print("1.Enter as customer\n2.check out\n3.view all pc specs\n4.add a new pc\n5.change component of a pc\n6.view passwords \n7.create password for a pc\n8.change password\n9.view details of all customers")
    print("10.view points of all customer\n11.view usage of all customers\n12.view total sales\n0.clear all databases")
    say=int(input("Enter a choice:"))
    if say==1:
        telltruth=input("Are you already a customer(y/n):")
        def reality():
            global lol
            query="use client_info"
            mycursor.execute(query)
            query="select cc from account"
            mycursor.execute(query)
            zz=mycursor.fetchall()
            for hol in zz:
                for zzz in hol:
                    lol.append(zzz)
            mydb.commit()
        reality()
        account()
        mydb.commit()
        super_choice=input("Do you want to continue:")
        if super_choice not in ("y","Y"):
            super_choice="k"
        lethim="yes"
    elif say==2:
        if lethim=="yes":            
            usage()
            mydb.commit()
            super_choice=input("Do you want to continue:")
            if super_choice not in ("y","Y"):
                super_choice="k"
        else:
            print("KINDLY FIRST ENTER AS CUSTOMER")
    elif say==3:
        adminpass=input("Enter admin password")
        if adminpass=="123abcxyz":
            query="use pc"
            mycursor.execute(query)
            query="select * from specifications"
            mycursor.execute(query)
            ds=mycursor.fetchall()
            print(" PROCESSOR, RAM, GRAPHICS CARD, STORAGE TYPE, PSU IN WATTS, PC CODE")
            for f1 in ds:
                print(f1,end="")
                print("\n")
            mydb.commit()
            super_choice=input("Do you want to continue:")
            if super_choice not in ("y","Y"):
                super_choice="k"
    elif say==4:
        adminpass=input("Enter admin password")
        if adminpass=="123abcxyz":
            insert_specs()
            print("successfully installed")
            mydb.commit()
            super_choice=input("Do you want to continue:")
            if super_choice not in ("y","Y"):
                super_choice="k"
    elif say==5:
        adminpass=input("Enter admin password")
        if adminpass=="123abcxyz":
            update_pc()
            print("successfully updated")
            mydb.commit()
            super_choice=input("Do you want to continue:")
            if super_choice not in ("y","Y"):
                super_choice="k"
    elif say==6:
        adminpass=input("Enter admin password")
        if adminpass=="123abcxyz":
            query="use pc"
            mycursor.execute(query)
            query="select * from passwords"
            mycursor.execute(query)
            ds2=mycursor.fetchall()
            print("password, pc code")
            for f2 in ds2:
                print(" ",f2,end=" ")
                print("\n")
            mydb.commit()
            super_choice=input("Do you want to continue:")
            if super_choice not in ("y","Y"):
                super_choice="k"
    elif say==7:
        adminpass=input("Enter admin password")
        if adminpass=="123abcxyz":
            insert_password()
            print("successfully created")
            mydb.commit()
            super_choice=input("Do you want to continue:")
            if super_choice not in ("y","Y"):
                super_choice="k"
    elif say==8:
        adminpass=input("Enter admin password")
        if adminpass=="123abcxyz":
            change_password()
            print("password successfully changed")
            super_choice=input("Do you want to continue:")
            mydb.commit()
            if super_choice not in ("y","Y"):
                super_choice="k"
    elif say==9:
        adminpass=input("Enter admin password")
        if adminpass=="123abcxyz":
            print(" NAME, LOCAL ADDRESS, EMAIL ADDRESS, PHONE NUMBER, CUSTOMER CODE")
            query="use client_info"
            mycursor.execute(query)
            query="select * from account"
            mycursor.execute(query)
            ds3=mycursor.fetchall()
            for f3 in ds3:
                print(f3,end=" ")
                print("\n")
            mydb.commit()
            super_choice=input("Do you want to continue:")
            if super_choice not in ("y","Y"):
                super_choice="k"
    elif say==10:
        adminpass=input("Enter admin password")
        if adminpass=="123abcxyz":
            query="use client_info"
            mycursor.execute(query)
            query="select * from points"
            mycursor.execute(query)
            ds4=mycursor.fetchall()
            print(" NAME, pc code, POINTS")
            for f4 in ds4:
                print(" ",f4,end=" ")
                print("\n")
            mydb.commit()
            super_choice=input("Do you want to continue:")
            if super_choice not in ("y","Y"):
                super_choice="k"
    elif say==11:
        adminpass=input("Enter admin password")
        if adminpass=="123abcxyz":
            query="use sign_out"
            mycursor.execute(query)
            query="select * from utilization"
            mycursor.execute(query)
            ds5=mycursor.fetchall()
            print(" CUSTOMER CODE, HOURS, MINUTES")
            for f5 in ds5:
                print("      ",f5,end=" ")
                print("\n")
            mydb.commit()
            super_choice=input("Do you want to continue:")
            if super_choice not in ("y","Y"):
                super_choice="k"
    elif say==12:
        adminpass=input("Enter admin password")
        if adminpass=="123abcxyz":
            query="use sign_out"
            mycursor.execute(query)
            query="select * from bill"
            mycursor.execute(query)
            ds6=mycursor.fetchall()
            print(" CUSTOMER CODE, NAME, AMOUNT")
            for f6 in ds6:
                print("   ",f6,end=" ")
                print("\n")
            mydb.commit()
            super_choice=input("Do you want to continue:")
            if super_choice not in ("y","Y"):
                super_choice="k"
    elif say==0:
        adminpass=input("Enter admin password")
        if adminpass=="123abcxyz":
            confirm=input("YOU ARE ABOUT TO CLEAR ALL DATABASES ARE YOU SURE!!(YES,NO):")
            if confirm in ("yes","YES"):
                clear_databases()
                print("ALL DATA CLEARED")
                super_choice="k"
                print("KINDLY RESTART THE PROGRAM")
        else:
            print("Invalid choice")
        

