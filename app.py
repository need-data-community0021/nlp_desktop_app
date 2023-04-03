from tkinter import *
from mydb import database
from tkinter import messagebox
from myapi import API
class Nlp:
    def __init__(self):
        # create db object
        self.dbo=database()
        self.apio=API()
        #this is log in code for our gui
        #create the object of the class
        self.root=Tk()

        # write the title of app
        self.root.title("NLP App")
        #here we are set the icon of the app which is converted by the favicon website
        self.root.iconbitmap("C:/Users/Rohit/PycharmProjects/pythonProject3/resources/favicon.ico")

        #here we are set the size of the app when app is open
        self.root.geometry('350x600')

        #in this we are set the colour
        self.root.configure(bg="white")

        #here we are also create the login class object because we first show the login page
        self.login_gui()

# this is function is hold the gui
        self.root.mainloop()

# create a login method
    def login_gui(self):
        self.clear()
        # when we want to display any text in tkinter so we have class id label
        heading = Label(self.root,text="NLPApp",bg='#34495E',fg="white")
        heading.pack(pady=(20))
        heading.configure(font=('vardana',22,'bold'))

#this is Label to show the  basically enter email
        label1=Label(self.root,text="Enter Email")
        label1.pack(pady=(10))

# it is a blank box in which we are write the the email
        self.emal_input=Entry(self.root,bg="white",width=40)
#
        self.emal_input.pack(pady=(5),ipady=2)

# this is Label to show the  basically enter password
        label2 = Label(self.root, text="Enter Password")
        label2.pack(pady=(10,5))

# it is a blank box in which we are write the password
        self.password_input = Entry(self.root, bg="white", width=40,show="*")
        self.password_input.pack(pady=5,ipady=2)

# this is 'Login' botton with this we are log in to app
        login_btn=Button(self.root,text="Login",width=20,height=1,command=self.perform_login)
        login_btn.pack(pady=(40,10))

#this is a label which is show the text 'not a member ?'
        label3 = Label(self.root, text="Not a Member?",fg="red")
        label3.pack(pady=(20,5))
# this is 'Register botton' with this we are register in to app
        redirect_btn=Button(self.root,text="Register Now",command=self.register_gui)
        redirect_btn.pack(pady=(10,10))

    def register_gui(self): # this is a method to clear the gui which is call by redirect_botton in which "cammand" parameter
        self.clear()
# we are using "self.clear()" method to when a click on the register botton then this function is call the clear function
#clear all login gui which is basically present in the our current gui thst's why we write the "self.clear()" method
        heading=Label(self.root,text='NLPApp',bg="#34495E",fg="white")
        heading.pack(pady=(30,30))
        heading.configure(font=("vardana",24,'bold'))

#set the leabel of "Enter name"
        label0 = Label(self.root,text="Enter Name")
        label0.pack(pady=(10,10))
# create the "Name entry box in which we write the Name"
        self.name_input = Entry(self.root,width=40)
        self.name_input.pack(pady=(10),ipady=2)

#also create the label of "Enter Email"
        label1 = Label(self.root, text="Enter Email")
        label1.pack(pady=(10, 5))

# it is a blank box in which we are write the password
        self.email_input = Entry(self.root, bg="white", width=40)
        self.email_input.pack(pady=5, ipady=2)

        label2 = Label(self.root,text="Enter Password")
        label2.pack(pady=(10,10))

        self.password_input = Entry(self.root,width=40,show="*")
        self.password_input.pack(pady=(10),ipady=2)

# this is 'Login' botton with this we are log in to app
        register_btn = Button(self.root, text="Register", width=20, height=1,command=self.registration)
        register_btn.pack(pady=(40, 10))

# this is a label which is show the text 'not a member ?'
        label3 = Label(self.root, text="Allready a Member?", fg="red")
        label3.pack(pady=(20, 5))

# this is 'Register botton' with this we are register in to app
        redirect_btn = Button(self.root, text="Login  Now", command=self.login_gui)
        redirect_btn.pack(pady=(10, 10))

#this method is basisclly clear the gui that are present in our gui
    def clear(self):
# pack slaves is basically get or fetch all the gui componant from that are availabel or present in our gui
        for i in self.root.pack_slaves(): # this is slaves of the pack he take all the gui componant that are available in the gui
            i.destroy() # destroy function is basically remove all the  gui componant



# fetch the data from registration "gui" with get method and add this data into our db file
    def registration(self):
        name=self.name_input.get()
        email=self.email_input.get()
        password=self.password_input.get()
        responce=self.dbo.add_data(name,email,password)
        if responce==1:
            messagebox.showinfo('Success','Registration successful. You can log in now')
            self.login_gui()
        else:
            messagebox.showinfo("Error","Email already exists")

    def perform_login(self):
        email=self.emal_input.get()
        password=self.password_input.get()

        response=self.dbo.search(email,password)
        if response:
            messagebox.showinfo("Success",'Login successful')
        #if successful login than this function redirect to home gui where we perform sentimental analysis,NER and so on
            self.home_gui()
        else:
            messagebox.showinfo("Error","Incorrect  email/password")

    def home_gui(self):
        #purana wala gui clear hoga uske bad hom_gui ka ka uske bad gui banaya he wo line by line load hoga
        self.clear()
        heading=Label(self.root,text="NlPApp",bg="#34495E",fg="white")
        heading.pack(pady=(30,30))
        #"pack" is a geometry manager that arranges widgets in a parent widget.
        #pack() method provides a simple and effective way to organize widgets in a window.
        heading.configure(font=('vardana',24,'bold'))

        sentiment_btn=Button(self.root,text="Sentimental Analysis",width=30,height=4,command=self.sentiment_gui)
        sentiment_btn.pack(pady=(10,10))

        ner_btn=Button(self.root,text="Named Entity Recognition",width=30,height=4,command=self.name_entity_recognition_gui)
        ner_btn.pack(pady=(10,10))

        emotional_btn=Button(self.root,text="Emostional Prediction",width=30,height=4)
        emotional_btn.pack(pady=(10,10))

        logout_btn=Button(self.root,text="Logout",command=self.login_gui)
        logout_btn.pack(pady=(10,10))

    def sentiment_gui(self):
        self.clear()

        heading=Label(self.root,text="NlPApp",bg="#34495E",fg="white")
        heading.pack(pady=(30,10))
        heading.configure(font=('vardana',24,'bold'))

        heading=Label(self.root,text="Sentiment Analysis",bg="#34495E",fg="white")
        heading.pack(pady=(5,20))
        heading.configure(font=('vardana',20))

        label1=Label(self.root,text="Enter The Text",width=15)
        label1.pack(pady=(10,10))

        self.sentiment_input=Entry(self.root,bg="white",width=50)
        self.sentiment_input.pack(pady=(5),ipady=10)

        sentiment_btn = Button(self.root, text="Analyze Sentiment", command=self.do_sentiment_analisis)
        sentiment_btn.pack(pady=(10, 10))

        self.sentiment_result=Label(self.root,text="",width=15,bg="#34495E",fg="white")
        self.sentiment_result.pack(pady=(10,10))
        self.sentiment_result.configure(font=('vardana',16))

        goback_btn = Button(self.root, text="Go Back", command=self.home_gui,height="1",width=6)
        goback_btn.pack(pady=(10, 10))

    def do_sentiment_analisis(self):
        text=self.sentiment_input.get()
        result=self.apio.sentiment_analysis(text)
        print(result)
        txt=''
        for i in result["sentiment"]:
            txt=txt + i + " -> " + str(result["sentiment"][i]) + '\n'
        print(txt)

        self.sentiment_result["text"]=txt


    def name_entity_recognition_gui(self):
        self.clear()
        heading=Label(self.root,text="NLPApp",bg="#34495E",fg="white")
        heading.pack(pady=(30,30))
        heading.configure(font=('vardana',24,'bold'))

        heading=Label(self.root,text="Named Entity Recognition",bg="#34495E",fg="white")
        heading.pack(pady=(5,20))
        heading.configure(font=('vardana',20))

        label1=Label(self.root,text="Enter the text",width=15)
        label1.pack(pady=(10,10))

        self.ner_input=Entry(self.root,bg="white",width=52)
        self.ner_input.pack(pady=(5),ipady=10)

        ner_btn=Button(self.root,text="Analyze NER",command=self.do_ner)
        ner_btn.pack(pady=(10,10))

        self.ner_result=Label(self.root,text="",width=50,bg="#34495E",fg="white")
        self.ner_result.pack(pady=(10,10))
        self.ner_result.configure(font=('vardana',10))

        goback_btn=Button(self.root,text="Go Back",command=self.home_gui,height="1",width=6)
        goback_btn.pack(pady=(100,5))


    def do_ner(self):
        text=self.ner_input.get()
        response=self.apio.name_entity_recognition_api(text)
        print(response)
        result = []
        for entity in response['entities']:
            result.append({'name': entity['name'], 'category': entity['category']})
        txt= '\n'.join(str(d) for d in result)
        self.ner_result["text"]=txt



nlp=Nlp()
#34495E