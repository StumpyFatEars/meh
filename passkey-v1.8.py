
import string
import random
import tkinter as tk
import pyperclip


def generate_passwords():
	try:
		password_length = int(length_entry.get())
		if password_length <= 0:
			raise ValueError
	except ValueError:
		tk.messagebox.showerror('Error',
								'Please enter a positive integer for password length.'
								)
		return

	try:
		num_passwords = int(num_passwords_entry.get())
		if num_passwords <= 0:
			raise ValueError
	except ValueError:
		tk.messagebox.showerror('Error',
								'Please enter a positive integer for number of passwords.'
								)
		return

	include_uppercase = uppercase_var.get()
	include_numbers = numbers_var.get()
	include_special = special_var.get()

	characters = string.ascii_lowercase
	if include_uppercase:
		characters += string.ascii_uppercase
	if include_numbers:
		characters += string.digits
	if include_special:
		characters += string.punctuation

	passwords = []
	for i in range(num_passwords):
		password = ''.join(random.choice(characters) for i in
						   range(password_length))
		passwords.append(password)

	password_display.config(state=tk.NORMAL)
	password_display.delete('1.0', tk.END)
	for password in passwords:
		password_display.insert(tk.END, password + '\n')
		copy_button = tk.Button(password_display,
								text='Copy to Clipboard',
								command=lambda password=password: \
								pyperclip.copy(password))
		password_display.window_create(tk.END, window=copy_button)
		save_button = tk.Button(password_display, text='Save Password',
								command=lambda password=password: \
								save_password(password))
		password_display.window_create(tk.END, window=save_button)
		password_display.insert(tk.END, '''

''')
	password_display.config(state=tk.DISABLED)


def save_password(password):
	with open('passwords.txt', 'a') as f:
		f.write(password + '\n')


def load_passwords():
	with open('passwords.txt', 'r') as f:
		passwords = f.readlines()
		password_display.config(state=tk.NORMAL)
		password_display.delete('1.0', tk.END)
		for password in passwords:
			password_display.insert(tk.END, password.strip() + '\n')
		password_display.config(state=tk.DISABLED)


root = tk.Tk()
root.title('PassKey™')
root.iconbitmap('favicon.ico'
				)

length_label = tk.Label(root, text='Password Length:')
length_label.pack()

length_entry = tk.Entry(root)
length_entry.pack()

num_passwords_label = tk.Label(root, text='Number of Passwords:')
num_passwords_label.pack()

num_passwords_entry = tk.Entry(root)
num_passwords_entry.pack()

uppercase_var = tk.BooleanVar()
uppercase_check = tk.Checkbutton(root, text='Include Uppercase Letters'
								 , variable=uppercase_var)
uppercase_check.pack()

numbers_var = tk.BooleanVar()
numbers_check = tk.Checkbutton(root, text='Include Numbers',
							   variable=numbers_var)
numbers_check.pack()

special_var = tk.BooleanVar()
special_check = tk.Checkbutton(root, text='Include Special Characters',
							   variable=special_var)
special_check.pack()

generate_button = tk.Button(root, text='Generate Passwords',
							command=generate_passwords)
generate_button.pack()

load_button = tk.Button(root, text='Load Passwords',
						command=load_passwords)
load_button.pack()

password_display = tk.Text(root, height=10, state=tk.DISABLED)
password_display.pack()

root.mainloop()
