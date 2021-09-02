import tkinter
from tkinter.font import Font
from tkinter import messagebox

username=['0']
password=['0']
books=['0']
window=tkinter.Tk()
window.geometry('1000x800')
window.title("LIBRARY MANAGEMENT")
global file1,file2,flag1,flag2
bg = tkinter.PhotoImage(file = "picwindow1.png")
canvas1 =tkinter.Canvas(window, width = 1000, height =1000)   
canvas1.pack() 
canvas1.create_image(0,10, image = bg,anchor = "nw")
canvas1.create_text( 500,50, text = "WELCOME TO THE LIBRARY MANAGEMENT SYSTEM",fill="brown",font=("Calibri Bold",25))

#############################################################################################################################
def newuser_cred_submit():
    usr1=tkinter.StringVar()
    i=tkinter.StringVar()
    flag1=0
    flag2=0
    file1=open("username.txt","r+")
    username=file1.readlines()
    usr1=usr.get()
    for i in username:
        if i==(usr1+"\n"):
            flag1=1
            
    if flag1==1:
        messagebox.showinfo('ERROR','Try another username this one already exists')
        window1.destroy()
    else:   
        file1.write(usr.get()+"\n")
        file1.close()
            
    paswrd1=tkinter.StringVar()
    j=tkinter.StringVar()
    file2= open("password.txt","r+")
    password=file2.readlines()
    paswrd1=paswrd.get()
    for j in password:
        if j==(paswrd1+"\n"):
            flag2=1
    if flag2==1:
        messagebox.showinfo('ERROR','Try another password this one already exists')
        window1.destroy()
    else:
        file2.write(paswrd.get()+"\n")
        messagebox.showinfo('SUCCESSFULLY SUBMITTED','Remember username and password')  
        file2.close()
    window1.destroy()
    flag1=0
    flag2=0
    
   
def clicked_on_newuser():
    global usr,paswrd,usr1,paswrd1,window1
    window1=tkinter.Tk()
    window1.geometry('1000x1000')
    window1.title("NEW USER CREDENTIALS")
    l1=tkinter.Label(window1,fg='orange',text="NEW USER CREDENTIALS\n\n\n",font=("Calibri Bold",20))
    l1.grid(column=1,row=0)
    cred=tkinter.Label(window1,text="\t\t\t\t\tNAME\n")
    cred.grid(column=0,row=1)
    name=tkinter.Entry(window1,width=20)
    name.grid(column=1,row=1)
    cred1=tkinter.Label(window1,text="\t\t\t\t\tD.O.B\n")
    cred1.grid(column=0,row=3)
    dob=tkinter.Entry(window1,width=20)
    dob.grid(column=1,row=3)
    cred2=tkinter.Label(window1,text="\t\t\t\t\tAADHAR NUMBER\n")
    cred2.grid(column=0,row=5)
    adno=tkinter.Entry(window1,width=20)
    adno.grid(column=1,row=5)
    cred3=tkinter.Label(window1,text="\t\t\t\t\tCONTACT NUMBER\n")
    cred3.grid(column=0,row=7)
    cono=tkinter.Entry(window1,width=20)
    cono.grid(column=1,row=7)
    cred4=tkinter.Label(window1,text="\t\t\t\t\tUSERNAME\n")
    cred4.grid(column=0,row=9)
    usr=tkinter.Entry(window1,width=20)
    usr.grid(column=1,row=9)
    cred5=tkinter.Label(window1,text="\t\t\t\t\tPASSWORD\n")
    cred5.grid(column=0,row=11)
    paswrd=tkinter.Entry(window1,width=20)
    paswrd.grid(column=1,row=11)
    cred6=tkinter.Label(window1,text="\t\t\t\t\tGENDER\n")
    cred6.grid(column=0,row=13)
    rd1=tkinter.Radiobutton(window1,text=" MALE ",value=1)
    rd1.grid(column=1,row=13)
    rd2=tkinter.Radiobutton(window1,text=" FEMALE ",value=2)
    rd2.grid(column=2,row=13)
    rd3=tkinter.Radiobutton(window1,text=" OTHERS ",value=3)
    rd3.grid(column=3,row=13)
    sub_button=tkinter.Button(window1,text="  SUBMIT  ",bg='blue',fg='white',command=newuser_cred_submit)
    sub_button.grid(column=1,row=15)

#############################################################################################################################

def login_page_for_issue():
    global login_usr,login_paswrd,window2_1
    window2_1=tkinter.Tk()
    window2_1.geometry('600x200')
    window2_1.title("LOGIN DETAILS")
    l2_1=tkinter.Label(window2_1,fg='red',text='Please login to your account\n\n',font=("Calibri Bold",15))
    l2_1.grid(column=0,row=1)
    login_cred1=tkinter.Label(window2_1,text="\t\t\t\t\tUSERNAME\n")
    login_cred1.grid(column=0,row=3)
    login_usr=tkinter.Entry(window2_1,width=15)
    login_usr.grid(column=1,row=3)    
    login_cred2=tkinter.Label(window2_1,text="\t\t\t\t\tPASSWORD\n")
    login_cred2.grid(column=0,row=5)
    login_paswrd=tkinter.Entry(window2_1,width=15)
    login_paswrd.grid(column=1,row=5)
    bt2_1=tkinter.Button(window2_1,text="LOGIN\t",height = 1, width = 10,bg="blue",fg="white",command=check_for_login_credentils)
    bt2_1.grid(column=1,row=7)

    
def check_for_login_credentils():
    global usr2,paswrd2
    flag1=0
    flag2=0
    usr2=tkinter.StringVar()
    paswrd2=tkinter.StringVar()
    file1= open("username.txt","r+")
    username=file1.readlines()
    usr2=login_usr.get()
    file2= open("password.txt","r+")
    password=file2.readlines()
    paswrd2=login_paswrd.get()
    for i in username:
        if i==(usr2+"\n"):
            flag1=1
    
    for j in password:
        if j==(paswrd2+"\n"):
            flag2=1
    
    if flag1==1 and flag2==1:
        clicked_on_bookissue()
        file1.close()
        file2.close()
        window2_1.destroy()
    elif flag1==1 and flag2!=1:   
        messagebox.showinfo('ERROR','Please input your valid PASSWORD.')
        window2_1.destroy()
    elif flag1!=1 and flag2==1:
        messagebox.showinfo('ERROR','Please input your valid USERNAME.')
        window2_1.destroy()
    elif flag1==0 and flag2==0:
        messagebox.showinfo('ERROR','Please input your valid USERNAME and PASSWORD.')
        window2_1.destroy()
    else:
        flag1=flag2=0
#############################################################################################################################
    
def login_page_for_return():
    global login_usr,login_paswrd,window2_1
    window2_1=tkinter.Tk()
    window2_1.geometry('600x200')
    window2_1.title("LOGIN DETAILS")
    l2_1=tkinter.Label(window2_1,fg='red',text='Please login to your account\n\n',font=("Calibri Bold",15))
    l2_1.grid(column=0,row=1)
    login_cred1=tkinter.Label(window2_1,text="\t\t\t\t\tUSERNAME\n")
    login_cred1.grid(column=0,row=3)
    login_usr=tkinter.Entry(window2_1,width=15)
    login_usr.grid(column=1,row=3)    
    login_cred2=tkinter.Label(window2_1,text="\t\t\t\t\tPASSWORD\n")
    login_cred2.grid(column=0,row=5)
    login_paswrd=tkinter.Entry(window2_1,width=15)
    login_paswrd.grid(column=1,row=5)
    bt2_1=tkinter.Button(window2_1,text="LOGIN\t",height = 1, width = 10,bg="blue",fg="white",command=check_for_login_credentils2)
    bt2_1.grid(column=1,row=7)

   
def check_for_login_credentils2():
    global usr2,paswrd2
    flag1=0
    flag2=0
    usr2=tkinter.StringVar()
    paswrd2=tkinter.StringVar()
    file1= open("username.txt","r+")
    username=file1.readlines()
    usr2=login_usr.get()
    file2= open("password.txt","r+")
    password=file2.readlines()
    paswrd2=login_paswrd.get()
    for i in username:
        if i==(usr2+"\n"):
            flag1=1
    
    for j in password:
        if j==(paswrd2+"\n"):
            flag2=1
    
    if flag1==1 and flag2==1:
        clicked_on_bookreturn()
        file1.close()
        file2.close()
        window2_1.destroy()
    elif flag1==1 and flag2!=1:   
        messagebox.showinfo('ERROR','Please input your valid PASSWORD.')
        window2_1.destroy()
    elif flag1!=1 and flag2==1:
        messagebox.showinfo('ERROR','Please input your valid USERNAME.')
        window2_1.destroy()
    elif flag1==0 and flag2==0:
        messagebox.showinfo('ERROR','Please input your valid USERNAME and PASSWORD.')
        window2_1.destroy()
    else:
        flag1=flag2=0


#############################################################################################################################

def clicked_on_bookissue_issuebutton():
    
    i=tkinter.StringVar()
    em_flag=0
    file1=open("issue details.txt","r+")
    username=file1.readlines()
    for i in username:
        em_flag=1
        
    file1.write("\n___________"+doi.get()+"___________\n\n")
    file1.write("Name :"+name.get()+"\n")
    file1.write("Book name :"+name_b.get()+"\n")
    file1.write("Author name :"+name_a.get()+"\n")
    file1.write("D.O.B :"+dob.get()+"\n")
    file1.write("Card number :"+card.get()+"\n")
    file1.write("User id :"+user.get()+"\n")
    file1.write("Password :"+password.get()+"\n")
    file1.write("________________________________\n")
    file1.close()
       
        
    messagebox.showinfo('SUCCESS','BOOK ISSUED SUCCESSFULLY')


def clicked_on_bookissue():

    global name,name_b,name_a,dob,doi,card,user,password,window2
    window2=tkinter.Tk()
    window2.geometry('1000x1000')
    window2.title("BOOK ISSUE")
    l2=tkinter.Label(window2,fg='green',text='THIS IS THE BOOK ISSUEING COUNTER\n\n\n',font=("Calibri Bold",20))
    l2.grid(column=1,row=0)
    bt2_1=tkinter.Button(window2,text='BOOKS AVAILABLE',height=1,width=15,fg='green',bg='white',command=clicked_on_available_books)
    bt2_1.grid(column=1,row=1)
    cred=tkinter.Label(window2,text="\t\t\t\t\tENTER YOUR NAME\n")
    cred.grid(column=0,row=3)
    name=tkinter.Entry(window2,width=20)
    name.grid(column=1,row=3)
    cred=tkinter.Label(window2,text="\t\t\t\t\tNAME OF THE BOOK\n")
    cred.grid(column=0,row=5)
    name_b=tkinter.Entry(window2,width=20)
    name_b.grid(column=1,row=5)
    cred=tkinter.Label(window2,text="\t\t\t\t\tNAME OF THE AUTHOR\n")
    cred.grid(column=0,row=7)
    name_a=tkinter.Entry(window2,width=20)
    name_a.grid(column=1,row=7)
    cred1=tkinter.Label(window2,text="\t\t\t\t\tD.O.B\n")
    cred1.grid(column=0,row=9)
    dob=tkinter.Entry(window2,width=20)
    dob.grid(column=1,row=9)
    cred2=tkinter.Label(window2,text="\t\t\t\t\tDATE OF ISSUE\n")
    cred2.grid(column=0,row=11)
    doi=tkinter.Entry(window2,width=20)
    doi.grid(column=1,row=11)
    cred3=tkinter.Label(window2,text="\t\t\t\t\tCARD NUMBER\n")
    cred3.grid(column=0,row=13)
    card=tkinter.Entry(window2,width=20)
    card.grid(column=1,row=13)
    cred4=tkinter.Label(window2,text="\t\t\t\t\tUSERNAME\n")
    cred4.grid(column=0,row=15)
    user=tkinter.Entry(window2,width=20)
    user.grid(column=1,row=15)
    cred5=tkinter.Label(window2,text="\t\t\t\t\tPASSWORD\n")
    cred5.grid(column=0,row=17)
    password=tkinter.Entry(window2,width=20)
    password.grid(column=1,row=17)
    bt2_2=tkinter.Button(window2,text='ISSUE',height=1,width=15,fg='blue',command=clicked_on_bookissue_issuebutton)

    bt2_2.grid(column=1,row=23)

##############################################################################################################################
    
def clicked_on_bookreturn_return_button():
    
    i=tkinter.StringVar()
    em_flag=0
    file1=open("return details.txt","r+")
    username=file1.readlines()
    for i in username:
        em_flag=1
        
    file1.write("\n___________"+dorr.get()+"___________\n\n")
    file1.write("Name :"+namer.get()+"\n")
    file1.write("Book name :"+name_br.get()+"\n")
    file1.write("Author name :"+name_ar.get()+"\n")
    file1.write("D.O.B :"+dobr.get()+"\n")
    file1.write("Card number :"+cardr.get()+"\n")
    file1.write("User id :"+userr.get()+"\n")
    file1.write("Password :"+passwordr.get()+"\n")
    file1.write("________________________________\n")
    file1.close()
    messagebox.showinfo('SUCCESS','BOOK RETURNED SUCCESSFULLY')
    
def clicked_on_bookreturn():
    global namer,name_br,name_ar,dobr,dorr,cardr,userr,passwordr,window3
    window3=tkinter.Tk()
    window3.geometry('1000x1000')
    window3.title("BOOK RETURN")
    l3=tkinter.Label(window3,fg='blue',text='THIS IS THE BOOK RETURNING COUNTER\n\n\n',font=("Calibri Bold",20))
    l3.grid(column=1,row=0)
    cred=tkinter.Label(window3,text="\t\t\t\t\tENTER YOUR NAME\n")
    cred.grid(column=0,row=3)
    namer=tkinter.Entry(window3,width=20)
    namer.grid(column=1,row=3)
    cred=tkinter.Label(window3,text="\t\t\t\t\tNAME OF THE BOOK\n")
    cred.grid(column=0,row=5)
    name_br=tkinter.Entry(window3,width=20)
    name_br.grid(column=1,row=5)
    cred=tkinter.Label(window3,text="\t\t\t\t\tNAME OF THE AUTHOR\n")
    cred.grid(column=0,row=7)
    name_ar=tkinter.Entry(window3,width=20)
    name_ar.grid(column=1,row=7)
    cred1=tkinter.Label(window3,text="\t\t\t\t\tD.O.B\n")
    cred1.grid(column=0,row=9)
    dobr=tkinter.Entry(window3,width=20)
    dobr.grid(column=1,row=9)
    cred2=tkinter.Label(window3,text="\t\t\t\t\tDATE OF RETURN\n")
    cred2.grid(column=0,row=11)
    dorr=tkinter.Entry(window3,width=20)
    dorr.grid(column=1,row=11)
    cred3=tkinter.Label(window3,text="\t\t\t\t\tCARD NUMBER\n")
    cred3.grid(column=0,row=13)
    cardr=tkinter.Entry(window3,width=20)
    cardr.grid(column=1,row=13)
    cred4=tkinter.Label(window3,text="\t\t\t\t\tUSERNAME\n")
    cred4.grid(column=0,row=15)
    userr=tkinter.Entry(window3,width=20)
    userr.grid(column=1,row=15)
    cred5=tkinter.Label(window3,text="\t\t\t\t\tPASSWORD\n")
    cred5.grid(column=0,row=17)
    passwordr=tkinter.Entry(window3,width=20)
    passwordr.grid(column=1,row=17)
    sub_bt=tkinter.Button(window3,text="RETURN\t",height = 1, width = 10,bg="blue",fg="white",command=clicked_on_bookreturn_return_button)
    sub_bt.grid(column=1,row=21)
    
#############################################################################################################################
    
def submit_book_details():
    name1=tkinter.StringVar()
    i=tkinter.StringVar()
    flag1=0
    flag2=0
    file2=open("books.txt","r+")
    books=file2.readlines()
    name1=nameb.get()
    for i in books:
        if i==("NAME OF THE BOOK:-  "+name1+"\n"):
            flag1=1       
    name_aut1=tkinter.StringVar()
    j=tkinter.StringVar()
    file2= open("books.txt","r+")
    books=file2.readlines()
    name_aut1=name_aut.get()
    for j in books:
        if j==("NAME OF THE AUTHOR:-  "+name_aut1+"\n"):
            flag2=1

    file2= open("books.txt","r+")
    books=file2.readlines()
    if flag1==1 and flag2==1:
        file2.write("NUMBER OF BOOKS AVAILABLE:-  "+nob.get()+"\n")
        messagebox.showinfo('ERROR',' This book already exists')
        
        window4_1.destroy()
        
    else:
        file2.write("NAME OF THE BOOK:-  "+nameb.get()+"\n")
        file2.write("NAME OF THE AUTHOR:-  "+name_aut.get()+"\n")
        file2.write("NUMBER OF BOOKS AVAILABLE:-  "+nob.get()+"\n")
        file2.write("_______________________________\n")
        messagebox.showinfo('SUCCESSFULLY SUBMITTED','SUCCESSFULLY ADDED THE BOOK')  
        
        file2.close()
    window4_1.destroy()
    flag1=0
    flag2=0
   

def clicked_on_add_books():
    global nameb,name_aut,nob,window4_1
    window4_1=tkinter.Tk()
    window4_1.geometry('500x280')
    window4_1.title("ADD BOOKS")
    l4_1=tkinter.Label(window4_1,fg='pink',text='ADD BOOKS HERE\n',font=("Calibri Bold",20))
    l4_1.grid(column=1,row=0)
    cred=tkinter.Label(window4_1,text="NAME OF THE BOOK\n")
    cred.grid(column=0,row=1)
    nameb=tkinter.Entry(window4_1,width=20)
    nameb.grid(column=1,row=1)
    cred=tkinter.Label(window4_1,text="NAME OF THE AUTHOR\n")
    cred.grid(column=0,row=3)
    name_aut=tkinter.Entry(window4_1,width=20)
    name_aut.grid(column=1,row=3)
    cred=tkinter.Label(window4_1,text="TOTAL NO.OF BOOKS AVAILABLE\n")
    cred.grid(column=0,row=5)
    nob=tkinter.Entry(window4_1,width=20)
    nob.grid(column=1,row=5)
    sub_bt=tkinter.Button(window4_1,text="SUBMIT\t",height = 1, width = 10,bg="yellow",fg="orange",command=submit_book_details)
    sub_bt.grid(column=1,row=7)

#############################################################################################################################


def remove_book_details():
    count=0
    file1=open("books.txt","r+")
    lines=file1.readlines()
    for i in lines:
        count+=1
    for i in range(count-1):
        if lines[i]==("NAME OF THE BOOK:-  "+named.get()+"\n"):
            del lines[i]
            messagebox.showinfo('DELETE','BOOK DELETED SUCCESSFULLY')
            #window4_2.destroy()
        elif lines[i]==("NAME OF THE AUTHOR:-  "+named_auth.get()+"\n"):
            del lines[i]
            messagebox.showinfo('DELETE','AUTHOR NAME DELETED SUCCESSFULLY')
        else:
            messagebox.showinfo('DELETE','NO SUCH BOOKS AVAILABLE TO DELETE')
            
      
    
def clicked_on_remove_books():
    global named,named_auth,window4_2
    window4_2=tkinter.Tk()
    window4_2.geometry('400x200')
    window4_2.title("REMOVE BOOK")
    l4_1=tkinter.Label(window4_2,fg='pink',text='REMOVE BOOKS \n',font=("Calibri Bold",20))
    l4_1.grid(column=1,row=0)
    cred=tkinter.Label(window4_2,text="NAME OF THE BOOK\n")
    cred.grid(column=0,row=1)
    named=tkinter.Entry(window4_2,width=20)
    named.grid(column=1,row=1)
    cred=tkinter.Label(window4_2,text="NAME OF THE AUTHOR\n")
    cred.grid(column=0,row=3)
    named_auth=tkinter.Entry(window4_2,width=20)
    named_auth.grid(column=1,row=3)
    sub_bt=tkinter.Button(window4_2,text="REMOVE\t",height = 1, width = 10,bg="yellow",fg="orange",command=remove_book_details)
    sub_bt.grid(column=1,row=5)
    
def clicked_on_available_books():
    file1=open("books.txt","r+")
    books=file1.readlines()
    flag=1
    for i in books:
        if flag%2!=0:
            print(i,end='\t')
        else:
            print(i)
        flag+=1    

def clicked_on_quit_window4():
    window4.destroy()
    
#############################################################################################################################

def check_librarians_login_details():
    global usr_lib,paswrd_lib
    flag1=0
    flag2=0
    usr_lib=tkinter.StringVar()
    paswrd_lib=tkinter.StringVar()
    file1= open("librarians cred.txt","r+")
    username=file1.readlines()
    usr_lib=login_librarian_usr.get()
    file2= open("librarians cred.txt","r+")
    password=file2.readlines()
    paswrd_lib=login_librarian_paswrd.get()
    for i in username:
        if i==(usr_lib+"\n"):
            flag1=1
    
    for j in password:
        if j==(paswrd_lib+"\n"):
            flag2=1
    
    if flag1==1 and flag2==1:
        clicked_on_librariansmenu()
        file1.close()
        file2.close()
        window4_3.destroy()
    elif flag1==1 and flag2!=1:   
        messagebox.showinfo('ERROR','Please input your valid PASSWORD.')
        window4_3.destroy()
    elif flag1!=1 and flag2==1:
        messagebox.showinfo('ERROR','Please input your valid USERNAME.')
        window4_3.destroy()
    elif flag1==0 and flag2==0:
        messagebox.showinfo('ERROR','Please input your valid USERNAME and PASSWORD.')
        window4_3.destroy()
    else:
        flag1=flag2=0
    
def librarians_login_details():
    global login_librarian_usr,login_librarian_paswrd,window4_3
    window4_3=tkinter.Tk()
    window4_3.geometry('600x200')
    window4_3.title("LOGIN DETAILS OF LIBRARIAN")
    l4_3=tkinter.Label(window4_3,fg='red',text="Please login to LIBRARIAN'S account\n\n",font=("Calibri Bold",15))
    l4_3.grid(column=1,row=1)
    login_cred1=tkinter.Label(window4_3,text="\t\tUSERNAME\n")
    login_cred1.grid(column=0,row=3)
    login_librarian_usr=tkinter.Entry(window4_3,width=15)
    login_librarian_usr.grid(column=1,row=3)    
    login_cred2=tkinter.Label(window4_3,text="\t\tPASSWORD\n")
    login_cred2.grid(column=0,row=5)
    login_librarian_paswrd=tkinter.Entry(window4_3,width=15)
    login_librarian_paswrd.grid(column=1,row=5)
    bt4_3=tkinter.Button(window4_3,text="LOGIN\t",height = 1, width = 10,bg="blue",fg="white",command=check_librarians_login_details)
    bt4_3.grid(column=1,row=7)
    
#############################################################################################################################

def check_librarians_credentials_change():
    usr1=tkinter.StringVar()
    i=tkinter.StringVar()
    flag1=0
    flag2=0
    file1=open("librarians cred.txt","r+")
    username=file1.readlines()
    usr1=login_librarian_usr_chng.get()
    for i in username:
        if i==(usr1+"\n"):
            flag1=1
            
    if flag1==1:
        messagebox.showinfo('ERROR','Try another username this one already exists')
        window1.destroy()
    else:   
        file1.write(login_librarian_usr_chng.get()+"\n")
        file1.close()
            
    paswrd1=tkinter.StringVar()
    j=tkinter.StringVar()
    file2= open("librarians cred.txt","r+")
    password=file2.readlines()
    paswrd1=login_librarian_paswrd_chng.get()
    for j in password:
        if j==(paswrd1+"\n"):
            flag2=1
    if flag2==1:
        messagebox.showinfo('ERROR','Try another password this one already exists')
        window1.destroy()
    else:
        file2.write(login_librarian_paswrd_chng.get()+"\n")
        messagebox.showinfo('SUCCESSFULLY SUBMITTED','Remember username and password')  
        file2.close()
    window1.destroy()
    flag1=0
    flag2=0

def librarians_credentials_change():
    global login_librarian_usr_chng,login_librarian_paswrd_chng,window4_3
    window4_4=tkinter.Tk()
    window4_4.geometry('600x200')
    window4_4.title("CHANGE LOGIN DETAILS OF LIBRARIAN")
    l4_4=tkinter.Label(window4_4,fg='red',text='Change login details here\n\n',font=("Calibri Bold",15))
    l4_4.grid(column=0,row=1)
    login_cred1=tkinter.Label(window4_4,text="\t\t\tEnter your new USERNAME\n")
    login_cred1.grid(column=0,row=3)
    login_librarian_usr_chng=tkinter.Entry(window4_4,width=15)
    login_librarian_usr_chng.grid(column=1,row=3)    
    login_cred2=tkinter.Label(window4_4,text="\t\t\tEnter your new PASSWORD\n")
    login_cred2.grid(column=0,row=5)
    login_librarian_paswrd_chng=tkinter.Entry(window4_4,width=15)
    login_librarian_paswrd_chng.grid(column=1,row=5)
    bt4_3=tkinter.Button(window4_4,text="CHANGE\t",height = 1, width = 10,bg="blue",fg="white",command=check_librarians_credentials_change)
    bt4_3.grid(column=1,row=7)

#############################################################################################################################
    
def clicked_on_librariansmenu():
    global window4,bg1
    window4=tkinter.Tk()
    window4.geometry('1000x1000')
    window4.title("LIBRARIANS MENU")
    l4=tkinter.Label(window4,fg='violet',text='\tTHIS IS THE LIBRARIANS COUNTER\n\n\n\n',font=("Calibri Bold",20)).pack()
    bt4_1=tkinter.Button(window4,text="\tADD BOOKS\t",height = 3, width = 30,bg="yellow",fg="orange",command=clicked_on_add_books).pack()
    bt4_2=tkinter.Button(window4,text="REMOVE BOOKS\t",height = 3, width = 30,bg="orange",fg="yellow",command=clicked_on_remove_books).pack()
    bt4_3=tkinter.Button(window4,text="\tBOOKS AVAILABLE\t",height = 3, width = 30,bg="yellow",fg="orange",command=clicked_on_available_books).pack()
    bt4_4=tkinter.Button(window4,text="\tCHANGE LOGIN CREDENTIALS\t",height = 3, width = 30,bg="orange",fg="yellow",command=librarians_credentials_change).pack()
    bt4_5=tkinter.Button(window4,text="\tQUIT\t",height = 3, width = 30,bg="yellow",fg="orange",command=clicked_on_quit_window4).pack()
    
#############################################################################################################################
   
def clicked_on_membership():
    window5=tkinter.Tk()
    window5.geometry('1000x1000')
    window5.title("MEMBERSHIPS")
    l5=tkinter.Label(window5,fg='yellow',text='THIS IS THE MEMBERSHIP COUNTER\n\n\n',font=("Calibri Bold",20))
    l5.grid(column=1,row=0)
    


def clicked_on_quit_window():
    window.destroy()

##############################################################################################################################
    
bt1=tkinter.Button(window,text="\tNEW USER\t",height = 2, width = 30,bg="black",fg="white",command=clicked_on_newuser)
button1_canvas = canvas1.create_window( 520, 200,anchor = "center",window = bt1)
bt2=tkinter.Button(window,text="\tBOOK ISSUE\t",height = 2, width = 30,bg="white",fg="black",command=login_page_for_issue)
button2_canvas = canvas1.create_window( 520, 250,anchor = "center",window = bt2)
bt3=tkinter.Button(window,text="\tBOOK RETURN\t",height = 2, width = 30,bg="black",fg="white",command=login_page_for_return)
button3_canvas = canvas1.create_window( 520, 300,anchor = "center",window = bt3)
bt4=tkinter.Button(window,text="\tLIBRARIAN'S MENU\t",height = 2, width = 30,bg="white",fg="black",command=librarians_login_details)
button4_canvas = canvas1.create_window( 520, 350,anchor = "center",window = bt4)
bt5=tkinter.Button(window,text="\tMEMBERSHIPS\t",height = 2, width = 30,bg="black",fg="white",command=clicked_on_membership)
button5_canvas = canvas1.create_window( 520, 400,anchor = "center",window = bt5)
bt6=tkinter.Button(window,text="\tDAILY NEWSPAPER\t",height = 2, width = 30,bg="white",fg="black")
button6_canvas = canvas1.create_window( 520, 450,anchor = "center",window = bt6)
bt7=tkinter.Button(window,text="\tQUIT\t",height = 2, width = 30,bg="black",fg="white",command=clicked_on_quit_window)
button7_canvas = canvas1.create_window( 520, 500,anchor = "center",window = bt7)
window.mainloop()














