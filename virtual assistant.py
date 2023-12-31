from tkinter import *
from gtts import gTTS
import speech_recognition as sr
import os
import re
import webbrowser
import smtplib
import requests
import pyttsx3
import datetime
import time


def mainprogram():
    
    def talkToMe(audio):
        print(audio)
        engine = pyttsx3.init()
        engine.say(audio)
        engine.runAndWait()

    def myCommand():
        r = sr.Recognizer()

        with sr.Microphone() as source:
            print('Ready...')
            r.pause_threshold = 1
            r.adjust_for_ambient_noise(source, duration=1)
            audio = r.listen(source)

        try:
            command = r.recognize_google(audio).lower()
            talkToMe('You said: ' + command + '\n')

        except sr.UnknownValueError:
            talkToMe('Your last command couldn\'t be heard')
            command = myCommand();

        return command


    def assistant(command):
        if 'open youtube' in command:
            reg_ex = re.search('open youtube (.*)', command)
            url = 'https://www.youtube.com/'
            if reg_ex:
                utube = reg_ex.group(1)
                url = url + 'r/' + utube
            talkToMe("Opening YouTube")
            webbrowser.open(url)
            print('Done!')

        elif 'open facebook' in command:
            reg_ex = re.search('open facebook (.+)', command)
            url = 'https://www.facebook.com/'
            if reg_ex:
                fb = reg_ex.group(1)
                url = url + 'r/' + fb
            talkToMe("Opening Facebook")
            webbrowser.open(url)
            print('Done!')

        elif 'what are you doing' in command:
            talkToMe('I am trying to use my inner powers to remain stable for long in order to increase my potential energy. I already lost some, in form of kinetic energy while explaining you. So stay away!')

        elif 'play hangman' in command:
            talkToMe("Okay let's play Hangman")
            hangman()

        elif 'boring' in command:
            talkToMe('Sorry, I\'m boring. I wasn\'t born this way. My school made me boring. Do you wanna play a game?')

        elif 'date' in command:
            talkToMe('Current Time and Date is: ')
            now = datetime.datetime.now()
            talkToMe(now.strftime("%Y-%m-%d %H:%M:%S"))

        elif 'Hello' in command:
            
            talkToMe('Hi! What should I call you?')
            myCommand()
            
            talkToMe('Nice name. I like it. It is nice to meet you! How old are you?')
            myCommand()
            
            talkToMe('wow! I\'m younger than you. When is your birthday?')
            myCommand()
            
            talkToMe('Awesome!!! I was born in the same month!')
            
            talkToMe('Okay. So what do you want me to do next?')
            
        elif 'joke' in command:
            res = requests.get(
                    'https://icanhazdadjoke.com/',
                    headers={"Accept":"application/json"}    
                    )
            if res.status_code == requests.codes.ok:
                talkToMe(str(res.json()['joke']))
            else:
                talkToMe('oops!I ran out of jokes')

        elif 'email' in command:
            
            talkToMe('Who is the recipient?')
            recipient = myCommand()

            if 'Sibani' in recipient:
                
                talkToMe('What should I say?')
                
                content = myCommand()
                mail = smtplib.SMTP('smtp.gmail.com', 587)
                mail.ehlo()
                mail.starttls()
                mail.login('username', 'password')
                mail.sendmail('Sibani Majhi', '160301120143@cutm.ac.in', content)
                mail.close()
                
                talkToMe('Email sent.')

            else:
                talkToMe('I don\'t know what you mean!')
                assistant(myCommand())
        else:
            talkToMe('Sorry! I can\'t do it. Tell me something else.')
            assistant(myCommand())
            sys.exit()

    def hangman():
        print ("Hello, Time to play hangman!")
        print ( " ")
        time.sleep(1)

        print( "Start guessing...")
        time.sleep(0.5)
        word = "secret"
        guesses = ''
        turns = 10
        while turns > 0:         
            failed = 0                
            for char in word:      
                if char in guesses:    
                    print (char)    

                else:
                    print( "_",   )  
                    failed += 1    
            if failed == 0:        
                print ("You won"  )
                break              
            guess = input("guess a character:") 
            guesses += guess                    
            if guess not in word:  
                turns -= 1  
                print ("Wrong")    
                print ("You have", + turns, 'more guesses' )
                if turns == 0:
                    print ("You Lose")



    talkToMe('Hello there!')

    while True:
        assistant(myCommand())
 
def register():
    global register_screen
    register_screen = Toplevel(main_screen)
    register_screen.title("Register")
    register_screen.geometry("300x250")
 
    global username
    global password
    global username_entry
    global password_entry
    username = StringVar()
    password = StringVar()
 
    Label(register_screen, text="Please enter details below", bg="blue").pack()
    Label(register_screen, text="").pack()
    username_lable = Label(register_screen, text="Username * ").pack()
    username_entry = Entry(register_screen, textvariable=username).pack()
    password_lable = Label(register_screen, text="Password * ").pack()
    password_entry = Entry(register_screen, textvariable=password, show='*').pack()
    Label(register_screen, text="").pack()
    Button(register_screen, text="Register", width=10, height=1, bg="blue", command = register_user).pack()
 
def login():
    
    global login_screen
    login_screen = Toplevel(main_screen)
    login_screen.title("Login")
    login_screen.geometry("300x250")
    Label(login_screen, text="Please enter de tails below to login",bg="blue").pack()
    Label(login_screen, text="").pack()
 
    global username_verify
    global password_verify
 
    username_verify = StringVar()
    password_verify = StringVar()
 
    global username_login_entry
    global password_login_entry
 
    Label(login_screen, text="Username * ").pack()
    username_login_entry = Entry(login_screen, textvariable=username_verify)
    username_login_entry.pack()
    Label(login_screen, text="").pack()
    Label(login_screen, text="Password * ").pack()
    password_login_entry = Entry(login_screen, textvariable=password_verify, show= '*')
    password_login_entry.pack()
    Label(login_screen, text="").pack()
    Button(login_screen, text="Login", width=10, height=1, command = login_verify).pack()
 
def register_user():
 
    username_info = username.get()
    password_info = password.get()
 
    file = open(username_info, "w") 
    file.write(username_info + "\n")
    file.write(password_info)
    file.close()
    
    Label(register_screen, text="Registration Success", fg="green", font=("calibri", 11)).pack()
    username_entry.delete(0, END)
    password_entry.delete(0, END)    
 
def login_verify():
    
    username1 = username_verify.get()
    password1 = password_verify.get()
    username_login_entry.delete(0, END)
    password_login_entry.delete(0, END)
 
    list_of_files = os.listdir()
    if username1 in list_of_files:
        file1 = open(username1, "r")
        verify = file1.read()
        if password1 in verify:
            login_sucess()
 
        else:
            password_not_recognised()
 
    else:
        user_not_found()
 
def login_sucess():
    
    global login_success_screen
    login_success_screen = Toplevel(login_screen)
    login_success_screen.title("Success")
    login_success_screen.geometry("150x100")
    Label(login_success_screen, text="Login Success").pack()
    Button(login_success_screen, text="OK", command=delete_login_success).pack()
    mainprogram()
 
def password_not_recognised():
    
    global password_not_recog_screen
    password_not_recog_screen = Toplevel(login_screen)
    password_not_recog_screen.title("Success")
    password_not_recog_screen.geometry("150x100")
    Label(password_not_recog_screen, text="Invalid Password ").pack()
    Button(password_not_recog_screen, text="OK", command=delete_password_not_recognised).pack()
 
def user_not_found():
    
    global user_not_found_screen
    user_not_found_screen = Toplevel(login_screen)
    user_not_found_screen.title("Success")
    user_not_found_screen.geometry("150x100")
    Label(user_not_found_screen, text="User Not Found").pack()
    Button(user_not_found_screen, text="OK", command=delete_user_not_found_screen).pack()
    
def delete_login_success():
    login_success_screen.destroy()
 
 
def delete_password_not_recognised():
    password_not_recog_screen.destroy()
 
def delete_user_not_found_screen():
    user_not_found_screen.destroy()
 
def main_account_screen():
    
    global main_screen
    
    main_screen = Tk()     
    main_screen.geometry("600x250")
    main_screen.title("Virtual Assistant")
    Label(text="Select Your Choice", bg="sky blue", width="300", height="2", font=("Calibri", 13)).pack()
    Label(text="").pack()
    Button(text="Login", height="2", width="30", command = login).pack()
    Label(text="").pack()
    Button(text="Register", height="2", width="30", command=register).pack()
    
    main_screen.mainloop()
 
 
main_account_screen()
