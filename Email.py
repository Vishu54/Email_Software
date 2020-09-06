from tkinter import *
from tkinter import scrolledtext
from tkinter import messagebox
import smtplib

smtp_obj=smtplib.SMTP('smtp.gmail.com',587)
smtp_obj.ehlo()
smtp_obj.starttls()

##################################################################################################################################
                                                    #connection
def connect():
    succes_login=smtp_obj.login(email.get(),passwd.get())
    if 235 in succes_login:
        print("sucess")
        send()
    else:
        messagebox.showwarning("Alert!!","Wrong Email/Password\nTry Again!!")
             
signup=Tk()
signup.title('LOGIN')
signup['bg']='#ED525A'
signup.geometry('500x370')

sub=Label(signup,text="",bg='#ED525A')
sub.pack()

labl=Label(signup,text='MAILING SYSTEM',bg='#ED525A',font=('Kite One',25,'bold'))
labl.config(anchor=CENTER)
labl.pack()

labl2=Label(signup,text='SIGNIN',bg='#ED525A',font=('Kite One',20,'bold'))
labl2.pack()

mail=Label(signup,text="Email: ",font=('Kite One',13,'bold'),bg='#ED525A')
mail.pack()

email = Entry(signup,width=30,font=('Kite One',13,'bold'))
email.pack()

pss=Label(signup,text="Password: ",bg='#ED525A',font=('Kite One',13,'bold'))
pss.pack()

passwd = Entry(signup,width=30,show = '*',font=('Kite One',13,'bold'))
passwd.pack()

space=Label(signup,text="",bg='#ED525A',font=('Kite One',13,'bold'))
space.pack()

btn=Button(signup,text="LOGIN",bg='#e84850',font=('Kite One',13,'bold'),command=connect)
btn.pack()

space=Label(signup,text="",bg='#ED525A')
space.pack()

eml=email.get()
pas=passwd.get()

##############################################################################################################################################
                                                        #EMAIL
def send():
    root=Tk()
    root.configure(bg='#ED525A')
    def send_mail():
        f=eml
        t=to_email.get()
        s=subject.get()
        m=message.get()
        msg="SUBJECT: "+s+"\n"+m
        dic=smtp_obj.sendmail(f,t,msg)
        print(dic)
        if dic == {}:
            messagebox.showinfo("Alert!!", "Mail Sent!!")

    root.title("Mail")
    root.geometry('500x370')
    signup.destroy()

    intro=Label(root,text="SEND MAIL",bg='#ED525A',font=('Kite One',20,'bold'))
    intro.pack()

    space=Label(root,text="",bg='#ED525A')
    space.pack()

    to=Label(root,text="TO: ",bg='#ED525A',font=('Kite One',13,'bold'))
    to.pack()
    
    to_email = Entry(root,width = 40,)
    to_email.pack()

    space=Label(root,text="",bg='#ED525A')
    space.pack()

    sub=Label(root,text="SUBJECT: ",bg='#ED525A',font=('Kite One',13,'bold'))
    sub.pack()

    subject = Entry(root,width = 40)
    subject.pack()
    
    space=Label(root,text="",bg='#ED525A')
    space.pack()
    
    sub=Label(root,text="MESSAGE",bg='#ED525A',font=('Kite One',13,'bold'))
    sub.pack()

    message = Entry(root,width=50)
    message.pack()

    sub=Label(root,text="",bg='#ED525A')
    sub.pack()
    snd=Button(root,text='SEND',bg='#e84850',command=send_mail)
    snd.pack()

##########################################################################################################################################
                                                        #DRIVER    
signup.mainloop()
smtp_obj.close()
