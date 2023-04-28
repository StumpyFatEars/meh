#import modules
 
from tkinter import *
import os
import time
 
def close():
	   #win.withdraw()
   win.withdraw()
 
# Designing window for registration
 
def delete_register_screen():
		register_screen.withdraw()
	
def delete_main_screen():
	main_screen.withdraw()
 
 
def register():
	global register_screen
	register_screen = Toplevel(main_screen)
	register_screen.title("PassKey™	|   Register")
	register_screen.iconbitmap('favicon.ico')
	register_screen.geometry("400x300")
 
	global username
	global password
	global username_entry
	global password_entry
	username = StringVar()
	password = StringVar()
 
	Label(register_screen, text="Please enter details below", bg="white").pack()
	Label(register_screen, text="").pack()
	username_lable = Label(register_screen, text="Username * ")
	username_lable.pack()
	username_entry = Entry(register_screen, textvariable=username)
	username_entry.pack()
	password_lable = Label(register_screen, text="Password * ")
	password_lable.pack()
	password_entry = Entry(register_screen, textvariable=password, show='*')
	password_entry.pack()
	Label(register_screen, text="").pack()
	Button(register_screen, text="Register", width=10, height=1, bg="white", command = register_user).pack()
 
 
# Designing window for login 
 
def login():
	global login_screen
	login_screen = Toplevel(main_screen)
	login_screen.title("PassKey™	|   Login")
	login_screen.iconbitmap('favicon.ico')
	login_screen.geometry("400x300")
	Label(login_screen, text="Please enter details below to login").pack()
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
 
# Implementing event on register button
 
def register_user():
 
	username_info = username.get()
	password_info = password.get()
 
	file = open(username_info, "w")
	file.write(username_info + "\n")
	file.write(password_info)
	file.close()
 
	username_entry.delete(0, END)
	password_entry.delete(0, END)
 
	Label(register_screen, text="Registration Success", fg="green", font=("calibri", 11)).pack()
	time.sleep(2)
	quit()
	
	
	
# Implementing event on login button 
 
def login_verify():
	username1 = username_verify.get()
	password1 = password_verify.get()
	username_login_entry.delete(0, END)
	password_login_entry.delete(0, END)
 
	list_of_files = os.listdir()
	if username1 in list_of_files:
		file1 = open(username1, "r")
		verify = file1.read().splitlines()
		if password1 in verify:
			login_sucess()
 
		else:
			password_not_recognised()
 
	else:
		user_not_found()
 
# Designing popup for login success
 
def login_sucess():
	global login_success_screen
	login_success_screen = Toplevel(login_screen)
	login_success_screen.title("PassKey™	|   Success")
	login_success_screen.iconbitmap('favicon.ico')
	login_success_screen.geometry("300x200")
	Label(login_success_screen, text="Login Success").pack()
	Button(login_success_screen, text="OK", command=delete_login_success).pack()
 
# Designing popup for login invalid password
 
def password_not_recognised():
	global password_not_recog_screen
	password_not_recog_screen = Toplevel(login_screen)
	password_not_recog_screen.title("PassKey™	|   Success")
	password_not_recog_screen.geometry("300x200")
	Label(password_not_recog_screen, text="Invalid Password ").pack()
	Button(password_not_recog_screen, text="OK", command=delete_password_not_recognised).pack()
 
# Designing popup for user not found
 
def user_not_found():
	global user_not_found_screen
	user_not_found_screen = Toplevel(login_screen)
	user_not_found_screen.title("PassKey™	|   Success")
	user_not_found_screen.iconbitmap('favicon.ico')
	user_not_found_screen.geometry("300x200")
	Label(user_not_found_screen, text="User Not Found").pack()
	Button(user_not_found_screen, text="OK", command=delete_user_not_found_screen).pack()
 
# Deleting popups
 
def delete_login_success():
	login_success_screen.withdraw()
 
 
def delete_password_not_recognised():
	password_not_recog_screen.withdraw()
 
 
def delete_user_not_found_screen():
	user_not_found_screen.withdraw()
 

 
 
# Designing Main(first) window
 
def main_account_screen():
	global main_screen
	main_screen = Tk()
	main_screen.geometry("400x300")
	main_screen.title("PassKey™	|   Account Login")
	main_screen.iconbitmap('favicon.ico')
	Label(text="Welcome!", bg="white", width="400", height="2", font=("Calibri", 13)).pack()
	Label(text="This is your first time so please register!").pack()
	Label(text="").pack()
	Button(text="Register", height="2", width="30", command=register).pack()
 
	main_screen.mainloop()
 
 
main_account_screen()