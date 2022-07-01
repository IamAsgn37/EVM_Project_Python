#main Admin Page
import pyttsx3
import mysql.connector
from datetime import date
#import user
def voice():
    speak=pyttsx3.init()
    speak.say("Welcome in Electronic voting Machine 2022")
    speak.runAndWait()
#=======================================================================
#..........                     BLO MODULE                   ..........#
#=======================================================================
    
def blo():
    while(True):
        print("="*53)
        print("\t\tWELCOME TO BLO PAGE")
        print("="*53)
        print("\nPRESS 1. ADD VOTER IN LIST")
        print("PRESS 2. SHOW VOTER LIST")
        print("PRESS 3. DELETE VOTER FORM LIST")
        print("PRESS 4. MODIFY VOTER INFORMATION")
        print("PRESS 5. MAIN MENU")
        print("-"*53)
        B_INPUT=int(input("PLEASE ENTER YOUR CHOICE:->  "))
        print("-"*53)
        print()
        if B_INPUT==1:
            add_voter()
        elif B_INPUT==2:
            show_voter()
            
        elif B_INPUT==3:
            delete_voter()
        
        elif B_INPUT==4:
            modify_voter()
        else:
            print("\n\tSUCESSFULLY EXIT FROM BLO PAGE..!\n")
            break
#============================================================================================================
#                                                    ADD VOTER
#=============================================================================================================
def add_voter():
    connection = mysql.connector.connect(user='root', password='asgn', host='localhost', database='evm')
    Cursor = connection.cursor(prepared=True)
    print("-"*53)
    print("        ###   Fill the Registration Form   ###  ")
    print("              ==========================        ")
    Cursor.execute("select count(*) from voter_list")
    FIRST_NAME=input("\nENTER FIRST NAME :-        ").upper()
    LAST_NAME=input("ENTER LAST NAME :-         ").upper()
    FATHER_NAME=input("ENTER FATHER'S NAME:-      ").upper()
    AGE=int(input("ENTER AGE :-               "))
    ADD=input("ENTER YOUR ADDRESS :-      ").upper()
    PHONE_NO=int(input("ENTER YOUR MOB NUMBER :-   "))
    PIN_CODE=int(input("ENTER PIN CODE :-          "))
    print(" ")
    print(" ")
    print("\t",FIRST_NAME,"ADDED IN VOTER LIST SUCESSFULLY...")
    print("="*53)
    print("\t\t     YOUR DETAILS")
    print("="*53)
    k=(list(Cursor))
    for i in  k:
        m=(i[0])
    if(m<=8):
        m=m+1
        ID='EVM2022IN0'+str(m)
    else:
        m=m+1
        ID='EVM2022IN'+str(m)
    Qry=("INSERT INTO voter_list VALUES(%s, %s, %s, %s, %s, %s, %s, %s)")
    val=(ID,FIRST_NAME,LAST_NAME,FATHER_NAME,AGE,ADD,PHONE_NO,PIN_CODE)
    Cursor.execute(Qry,val)
    connection.commit()
    Cursor.close()
    print("VOTER ID :      ",ID)
    print("NAME :          ",FIRST_NAME,LAST_NAME)
    #print("LAST NAME :     ",LAST_NAME)
    print("FATHER'S NAME : ",FATHER_NAME)
    print("AGE IS :        ",AGE)
    print("ADDRESS IS :    ",ADD)
    print("PHONE NUMBER :  ",PHONE_NO)
    print("PIN CODE :      ",PIN_CODE)
    print("="*53)

#=============================================================================================================================
def modify_voter():
    connection = mysql.connector.connect(user='root', password='asgn', host='localhost', database='evm')
    Cursor = connection.cursor()
    N=input("ENTER YOUR VOTER ID NUMBER : ")
    print()
    query = ("SELECT * FROM voter_list where VOTER_ID = %s")
    rec_srch = (N,)
    Cursor.execute(query, rec_srch)
    Rec_count = 0
    for(VOTER_ID, FIRST_NAME, LAST_NAME, FATHER_NAME, AGE, ADDRESS, PHONE_NO, PIN_CODE) in Cursor:
            Rec_count += 1
            #print("=============================================================")
            #print("Member Code : ", mno)
            #print("Member Name : ", mname)
            #print("Date of Membership : ", Date_of_Membership)
            #print("Address : ", addr)
            #print("Mobile No. of Member : ", mob)
            #print("=============================================================")
    if Rec_count == 0:
        print("Record's  NOT found")
    else:
         print("PRESS 1. FOR FIRST NAME MODIFICATION")
         print()
         print("PRESS 2. FOR LAST NAME MODIFICATION")
         print()
         print("PRESS 3. FOR FATHER'S NAME MODIFICATION")
         print()
         print("PRESS 4. FOR  AGE MODIFICATION")
         print()
         print("PRESS 5. FOR  ADDRESS MODIFICATION")
         print()
         print("PRESS 6. FOR PHONE NUMBER MODIFICATION")
         print()
         print("PRESS 7. FOR PINCODE MODIFICATION\n")
         print("-"*53)
         Z=int(input("PLEASE ENTER YOUR CHOICE :->"))
         print("-"*53)
         if Z==1:
             K=input("ENTER NEW FIRST NAME TO MODIFY : ").upper()
             Qry = ("UPDATE voter_list SET FIRST_NAME=%s  WHERE VOTER_ID=%s")
             data = (K,N)
             Cursor.execute(Qry,data)
             print("\n\tDATA UPDATED SUCCESFULLY..!")
             connection.commit()
             Cursor.close()
             connection.close()
         elif Z==2:
             K=input("ENTER NEW LAST NAME TO MODIFY").upper()
             Qry = ("UPDATE voter_list SET LAST_NAME=%s  WHERE VOTER_ID=%s")
             data = (K,N)
             Cursor.execute(Qry,data)
             print("\n\tDATA UPDATED SUCCESFULLY..!")
             connection.commit()
             Cursor.close()
             connection.close()

         elif Z==3:
             K=input("ENTER FATHER'S NAME TO MODIFY").upper()
             Qry = ("UPDATE voter_list SET FATHER_NAME=%s  WHERE VOTER_ID=%s")
             data = (K,N)
             Cursor.execute(Qry,data)
             print("\n\tDATA UPDATED SUCCESFULLY..!")
             connection.commit()
             Cursor.close()
             connection.close()
         elif Z==4:
             K=(input("ENTER AGE TO MODIFY"))
             Qry = ("UPDATE voter_list SET AGE=%s  WHERE VOTER_ID=%s")
             data = (K,N)
             Cursor.execute(Qry,data)
             print("\n\tDATA UPDATED SUCCESFULLY..!")
             connection.commit()
             Cursor.close()
             connection.close()
         elif Z==5:

             K=input("ENTER NEW ADDRESS TO MODIFY").upper()
             Qry = ("UPDATE voter_list SET ADDRESS=%s  WHERE VOTER_ID=%s")
             data = (K,N)
             Cursor.execute(Qry,data)
             print("\n\tDATA UPDATED SUCCESFULLY..!")
             connection.commit()
             Cursor.close()
             connection.close()
         elif Z==6:
             K=input("ENTER NEW PHONE NUMBER TO MODIFY")
             Qry = ("UPDATE voter_list SET PHONE_NO=%s  WHERE VOTER_ID=%s")
             data = (K,N)
             Cursor.execute(Qry,data)
             print("\n\tDATA UPDATED SUCCESFULLY..!")
             connection.commit()
             Cursor.close()
             connection.close()
         elif Z==7:

             K=input("ENTER NEW PIN CODE TO MODIFY").upper()
             Qry = ("UPDATE voter_list SET PIN_CODE=%s  WHERE VOTER_ID=%s")
             data = (K,N)
             Cursor.execute(Qry,data)
             print("\n\tDATA UPDATED SUCCESFULLY..!")
             connection.commit()
             Cursor.close()
             connection.close()
         else:
            print()
            print("                    WORNG CHOICE")
            print("                  ****************")
#======================================================================================================================
def delete_voter():
    connection= mysql.connector.connect(user='root', password='asgn', host='localhost', database='evm')
    Cursor = connection.cursor(prepared=True)
    MNO = input("ENTER YOUR ID TO DELETE VOTER: ").upper()
    Qry =("""DELETE FROM voter_list WHERE voter_id = %s""")
    del_rec = (MNO,)
    Cursor.execute(Qry, del_rec)
    connection.commit()
    Cursor.close()
    connection.close()
    print(Cursor.rowcount, "VOTER(S) DELETED SECCESSFULLY.")
    print("                    ***                    ")
    print("\n\n="*53)
#=========================================================================================================================
def show_voter():
    print("="*53)
    print("\t\t\tSHOW VOTER")
    connection = mysql.connector.connect(user='root', password='asgn', host='localhost', database='evm')
    Cursor = connection.cursor()
        
    query = ("SELECT * FROM voter_list")

    Cursor.execute(query)
    Rec_count = 0
    for(ID, FIRST_NAME, LAST_NAME, FATHER_NAME, AGE, ADD, PHONE_NO, PIN_CODE) in Cursor:
        Rec_count += 1
        print("="*53)
        print("VOTER ID :      ",ID)
        print("FIRST NAME :    ",FIRST_NAME,LAST_NAME)
        #print("LAST NAME :     ",LAST_NAME)
        print("FATHER'S NAME : ",FATHER_NAME)
        print("AGE IS :        ",AGE)
        print("ADDRESS IS :    ",ADD)
        print("PHONE NUMBER :  ",PHONE_NO)
        print("PIN CODE :      ",PIN_CODE)
    print("="*53)
    if Rec_count==0:
        print("\n\tNO VOTER FOUND.....!")
    

#===================================================================================================================================

        
##...............ADMIN MODULE............##

def start_voting():
    connection = mysql.connector.connect(user='root', password='asgn', host='localhost', database='evm')
    Cursor = connection.cursor()
    LN=0
    name=[]
    party_name=[]
    symbol=[]
    voting_list=[]
    n=int(input("ENTER TOTAL NUMBER OF CANDIDATE : "))
    VOTING=[0]*n
    for i in range(n):
        k=input("ENTER CANDIDATE NAME : ")
        name.append(k)
        m=input("ENTER PARTY NAME : ")
        party_name.append(m)
        z=input("ENTER SYMBOL : ")
        symbol.append(z)
    END_SESSION=input("ENTER END SESSION KEY : ")
    L=0
    while(L!=END_SESSION):
        N=input("ENTER YOUR VOTER ID NUMBER : ")
        print()
        query = ("SELECT * FROM voter_list where VOTER_ID = %s")
        rec_srch = (N,)
        Cursor.execute(query, rec_srch)
        Rec_count = 0
        for(VOTER_ID, FIRST_NAME, LAST_NAME, FATHER_NAME, AGE, ADDRESS, PHONE_NO, PIN_CODE) in Cursor:
            Rec_count += 1

        if Rec_count == 0:
            print("Record's  NOT found")

        else:

            if N not in voting_list:
                voting_list.append(N)
                for i in range(n):
                    print("PRESS",LN,"FOR", "CANDIDATE NAME",name[LN],"PARTY NAME :->",party_name[LN],"SYMBOL :->",symbol[LN])
                    LN+=1
                LN=0
                inp=int(input())
                VOTING[inp]+=1
                L=input("ALLOW VOTER OR END SESSION")
    print(VOTING)
    print(voting_list)
    date_of_voting=date.today()
    LN=0
    for i in range(n):
        Qry=("INSERT INTO voting_result VALUES(%s, %s, %s, %s, %s)")
        val=(name[LN],party_name[LN],symbol[LN],date_of_voting,VOTING[LN])
        LN+=1
        Cursor.execute(Qry,val)
        print("data saved")
    connection.commit()
    Cursor.close()
def admin():
    while(True):
        print("="*53)
        print("\t\tWELCOME TO ADMIN PAGE\t\t")
        print("="*53)
        print("\nPRESS 1. START VOTING")
        print("PRESS 2. SHOW VOTER LIST")
        print("PRESS 3. SHOW TOTAL VOTE COUNT")
        print("PRESS 4. SHOW LEADING CANDIDATE")
        print("PRESS 5. EXIT")
        print("="*53)
    
        A_INPUT=int(input("PLEASE ENTER YOUR CHOICE:->  "))
        if A_INPUT==1:
            print("="*53)
            print("\n\t\tVOTING STARTING NOW....")
            #user()
            start_voting()
            print("="*53)
        elif A_INPUT==2:
            show_voter()
        elif A_INPUT==3:
            print("="*53)
            print("\t\tTOTAL VOTES ARE COUNTED")
            print("="*53)
        elif A_INPUT==4:
            print("="*53)
            print("\t\t\tWINNER")
            print("="*53)
        else:
            print("="*53)
            print("\t\nSUCCESSFULLY EXIT FROM ADMIN PAGE...!")
            print("="*53)
            break
    
#==============================================================================
        #               VOTING
#=================================================================================




        
#=================================================================================
#..........USER MODULE.........#
#==================================================================================
def user():
    print("\n WAIT FOR USER")
    
    
################################################################
##                      MAIN PAGE START                       ##
################################################################
    
print("*****************************************************")
print("*****************************************************")
print("**                                                 **")
print("**         ELECTION  VOTING  MACHINE - 2022        **")
print("**                                                 **")
print("*****************************************************")
print("*****************************************************")
print(" ")
voice()
while(True):
    print("="*53)
    print("\t\t WELCOME TO EVM")
    print("="*53)
    print("\nPRESS 1. Admin LOGIN \nPRESS 2. BLO LOGIN\nPRESS 0. EXIT")
    print("="*53)
    INPUT=int(input("Enter Your Choice: <0 TO 2> :-"))
    print("")
    if INPUT==1:
        admin()
    elif INPUT==2:
        blo()
    elif INPUT==0:
        
        print("\n     ##...THANK YOU FOR USING MY SERVICE...##     \n")
        break
    else:
        print("             ## INVALID INPUT...! ##  \n")
        print("\n     ##...THANK YOU FOR USING MY SERVICE...##     \n")
        break

