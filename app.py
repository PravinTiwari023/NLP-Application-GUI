from tkinter import *
from tkinter import messagebox
from mydb import Database
from myapi import API

class NLPApp:
    # Constructor
    def __init__(self):
        self.dbo = Database()
        self.api = API()
        # Login ka GUI Load karna
        self.root = Tk()
        self.root.title('NLP Application')
        self.root.iconbitmap('Resources/favicon.ico')
        self.root.geometry('500x700')

        self.Homepage_GUI()

        self.root.mainloop()

    # Homepage GUI Function
    def Homepage_GUI(self):
        self.Clear_GUI()

        self.root.configure(bg='#CEF6F5')
        welcome_label = Label(self.root, text="Welcome to the NLP Application!", font=("times", 18, 'bold'), bg='#CEF6F5', fg='#0B615E')
        welcome_label.pack(pady=20)

        # Login Button
        login_button = Button(self.root, text='Login', font=('times', 15, 'bold'), bg='#00FFFF', fg='#000000', command=self.Login_GUI)
        login_button.pack(pady=(20,20))

        # Register Button
        register_button = Button(self.root, text='Register', font=('times', 15, 'bold'), bg='#2EFE9A', fg='#000000', command=self.Register_GUI)
        register_button.pack(pady=(20,20))

    # Login GUI Function
    def Login_GUI(self):
        self.Clear_GUI()

        self.root.configure(bg='#D8D8D8')
        heading = Label(self.root, text='NLP Application', font=('times', 20, 'bold'), bg='#D8D8D8', fg='#0B615E')
        heading.pack(pady=(20,20))

        lable1 = Label(self.root, text='Email', font=('times', 14, 'bold'), bg='#D8D8D8', fg='#0B615E')
        lable1.pack(pady=(10, 10))

        self.email_input = Entry(self.root, width=35, font=('times', 12, 'bold'), bg='#FAFAFA', fg='#000000')
        self.email_input.pack(pady=(10, 10), ipady=4)

        lable2 = Label(self.root, text='Password', font=('times', 14, 'bold'), bg='#D8D8D8', fg='#0B615E')
        lable2.pack(pady=(10, 10))

        self.password_input = Entry(self.root, show='*', width=35, font=('times', 12, 'bold'), bg='#FAFAFA', fg='#000000')
        self.password_input.pack(pady=(10, 10), ipady=4)

        Button(self.root, text='Login', width=8, height=1 , font=('times', 14, 'bold'), bg='#00FFFF', fg='#000000', command=self.perform_login).pack(pady=(20,20))

        lable2 = Label(self.root, text='Not a member?', font=('times', 14, 'bold'), bg='#D8D8D8', fg='#0B615E')
        lable2.pack(pady=(20, 10))

        Button(self.root, text='Register Now', font=('times', 14, 'bold'), bg='#2EFE9A', fg='#000000', command=self.Register_GUI).pack(pady=(10,10))
        pass

    def Register_GUI(self):
        self.Clear_GUI()

        self.root.configure(bg='#F8E0F7')
        heading = Label(self.root, text='NLP Application', font=('times', 20, 'bold'), bg='#F8E0F7', fg='#610B38')
        heading.pack(pady=(20,20))

        lable0 = Label(self.root, text='Name', font=('times', 14, 'bold'), bg='#F8E0F7', fg='#610B38')
        lable0.pack(pady=(10, 10))

        self.name_input = Entry(self.root, width=35, font=('times', 12, 'bold'), bg='#FAFAFA', fg='#000000')
        self.name_input.pack(pady=(10, 10), ipady=4)

        lable1 = Label(self.root, text='Email', font=('times', 14, 'bold'), bg='#F8E0F7', fg='#610B38')
        lable1.pack(pady=(10, 10))

        self.email_input = Entry(self.root, width=35, font=('times', 12, 'bold'), bg='#FAFAFA', fg='#000000')
        self.email_input.pack(pady=(10, 10), ipady=4)

        lable2 = Label(self.root, text='Password', font=('times', 14, 'bold'), bg='#F8E0F7', fg='#610B38')
        lable2.pack(pady=(10, 10))

        self.password_input = Entry(self.root, show='*', width=35, font=('times', 12, 'bold'), bg='#FAFAFA', fg='#000000')
        self.password_input.pack(pady=(10, 10), ipady=4)

        Button(self.root, text='Register', width=8, height=1, font=('times', 14, 'bold'), bg='#2EFE9A', fg='#000000', command=self.Perform_registration).pack(pady=(20, 20))

        lable2 = Label(self.root, text='Already a member?', font=('times', 14, 'bold'), bg='#F8E0F7', fg='#610B38')
        lable2.pack(pady=(20, 10))

        Button(self.root, text='Login Now', font=('times', 14, 'bold'), bg='#00FFFF', fg='#000000', command=self.Login_GUI).pack(pady=(10, 10))
        pass

    # Home Gui for operetion
    def Home_GUI(self):
        self.Clear_GUI()

        self.root.configure(bg='#D8F6CE')
        label1 = Label(self.root, text='NLP Application', font=('times', 20, 'bold'), bg='#D8F6CE', fg='#0B615E')
        label1.pack(pady=(20,20))

        Button(self.root, text='Sentiment Analysis', width=20, height= 3, font=('times', 14, 'bold'), bg='#0B615E', fg='#CEF6F5', command= self.Sentiment_GUI).pack(pady=(20, 20))
        Button(self.root, text='Named Entity Recognition', width=20, height= 3, font=('times', 14, 'bold'), bg='#0B615E', fg='#CEF6F5', command= self.NER_GUI).pack(pady=(20, 20))
        Button(self.root, text='Abuse Detection', width=20, height= 3, font=('times', 14, 'bold'), bg='#0B615E', fg='#CEF6F5', command=self.Abuse_GUI).pack(pady=(20, 20))

        Button(self.root, text='Logout', font=('times', 14, 'bold'), bg='#FF0000', fg='#000000', command=self.Homepage_GUI).pack(pady=(20, 20))

    # Sentiment GUI Function
    def Sentiment_GUI(self):
        self.Clear_GUI()

        self.root.configure(bg='#D8F6CE')
        label1 = Label(self.root, text='NLP Application', font=('times', 20, 'bold'), bg='#D8F6CE', fg='#0B615E')
        label1.pack(pady=(20, 10))

        label2 = Label(self.root, text='Sentiment Analysis', font=('times', 18), bg='#D8F6CE', fg='#0B615E')
        label2.pack(pady=(10, 20))

        label3 = Label(self.root, text='Enter the text to be analyzed', font=('times', 14, 'bold'), bg='#D8F6CE', fg='#0B615E')
        self.text_input = Text(self.root, width=60, height=5, font=('times', 12, 'bold'), bg='#FAFAFA', fg='#000000')
        self.text_input.pack(pady=(10, 10), ipady=4)

        Button(self.root, text='Analyze Sentiment', font=('times', 14, 'bold'), bg='#A9A9F5', fg='#CEF6F5', command=self.perform_sentiment).pack(pady=(10, 10))

        self.result = Label(self.root, text='', font=('verdana', 14, 'bold'), bg='#D8F6CE', fg='#01DF01')
        self.result.pack(pady=(10, 10))

        Button(self.root, text='Back', font=('times', 14, 'bold'), bg='#FFFF00', fg='#000000', command=self.Home_GUI).pack(pady=(10, 10))

    def NER_GUI(self):
        self.Clear_GUI()

        self.root.configure(bg='#D8F6CE')
        label1 = Label(self.root, text='NLP Application', font=('times', 20, 'bold'), bg='#D8F6CE', fg='#0B615E')
        label1.pack(pady=(20, 10))

        label2 = Label(self.root, text='Named Entity Recognition', font=('times', 18), bg='#D8F6CE', fg='#0B615E')
        label2.pack(pady=(10, 20))

        label3 = Label(self.root, text='Enter the text to be analyzed', font=('times', 14, 'bold'), bg='#D8F6CE', fg='#0B615E')
        label3.pack(pady=(10, 10))

        self.text_input = Text(self.root, width=60, height=5, font=('times', 12, 'bold'), bg='#FAFAFA', fg='#000000')
        self.text_input.pack(pady=(10, 10), ipady=4)

        Button(self.root, text='Analyze Named Entities', font=('times', 14, 'bold'), bg='#A9A9F5', fg='#CEF6F5', command=self.perform_NER).pack(pady=(10, 10))

        self.result = Label(self.root, text='', font=('verdana', 14, 'bold'), bg='#D8F6CE', fg='#01DF01')
        self.result.pack(pady=(10, 10))

        Button(self.root, text='Back', font=('times', 14, 'bold'), bg='#FFFF00', fg='#000000', command=self.Home_GUI).pack(pady=(10, 10))

    def Abuse_GUI(self):
        self.Clear_GUI()

        self.root.configure(bg='#D8F6CE')
        label1 = Label(self.root, text='NLP Application', font=('times', 20, 'bold'), bg='#D8F6CE', fg='#0B615E')
        label1.pack(pady=(20, 10))

        label2 = Label(self.root, text='Abuse Detection', font=('times', 18), bg='#D8F6CE', fg='#0B615E')
        label2.pack(pady=(10, 20))

        label3 = Label(self.root, text='Enter the text to be analyzed', font=('times', 14, 'bold'), bg='#D8F6CE', fg='#0B615E')
        label3.pack(pady=(10, 10))

        self.text_input = Text(self.root, width=60, height=5, font=('times', 12, 'bold'), bg='#FAFAFA', fg='#000000')
        self.text_input.pack(pady=(10, 10), ipady=4)

        Button(self.root, text='Analyze Emotion', font=('times', 14, 'bold'), bg='#A9A9F5', fg='#CEF6F5', command=self.perform_abuse).pack(pady=(10, 10))

        self.result = Label(self.root, text='', font=('verdana', 14, 'bold'), bg='#D8F6CE', fg='#01DF01')
        self.result.pack(pady=(10, 10))

        Button(self.root, text='Back', font=('times', 14, 'bold'), bg='#FFFF00', fg='#000000', command=self.Home_GUI).pack(pady=(10, 10))

    # Clear GUI Function
    def Clear_GUI(self):
        for i in self.root.pack_slaves():
            i.destroy()

    # Performing Registration process
    def Perform_registration(self):
        # Fetching the data
        name = self.name_input.get()
        email = self.email_input.get()
        password = self.password_input.get()

        response = self.dbo.add_data(name, email, password)

        if response:
            messagebox.showinfo('Success', 'Registration Successfull. You can login now')
            self.Login_GUI()
        else:
            messagebox.showerror('Error', 'Email already exists. Please try another email')
            self.Login_GUI()

    # Performing Login process
    def perform_login(self):
        # Fetching the data
        email = self.email_input.get()
        password = self.password_input.get()

        response = self.dbo.login_data(email, password)

        if response == 1:
            messagebox.showinfo('Success', 'Login Successfull')
            self.Home_GUI()
        elif response == 2:
            messagebox.showerror('Error', 'Incorrect Password')
            self.Login_GUI()
        else:
            messagebox.showerror('Error', 'Email is not registered yet. Please Register first')
            self.Register_GUI()

    # Performing Sentiment
    def perform_sentiment(self):
        text = self.text_input.get(1.0, END)
        response = self.api.sentiment_analysis(text)

        txt = ''
        for i in response:
            txt = txt + i + " -> " + str(response[i]) + '\n'

        self.result['text'] = txt

    def perform_NER(self):
        text = self.text_input.get(1.0, END)
        response = self.api.NER_analysis(text)

        txt = ''
        for i in response:
            for j in i:
                txt = txt + j + " -> " + str(i[j]) + '\n'
            txt = txt + '\n'

        self.result['text'] = txt

    def perform_abuse(self):
        text = self.text_input.get(1.0, END)
        response = self.api.Abuse_analysis(text)

        txt = ''
        for i in response:
            txt = txt + i + " -> " + str(response[i]) + '\n'

        self.result['text'] = txt



nlp = NLPApp()