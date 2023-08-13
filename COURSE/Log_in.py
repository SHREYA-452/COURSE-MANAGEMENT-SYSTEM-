import tkinter as tk
import tkinter.messagebox
import hashlib
import json
import os


def main():
    root = tk.Tk()
    app = Window_1(root)
    root.mainloop()

class Window_1:
    def __init__(self, master):
        self.master = master
        self.master.title("Login Window")
        self.master.geometry('1350x750')
        self.master.config(bg='lightskyblue')
        self.Frame = tk.Frame(self.master, bg='lightskyblue')
        self.Frame.pack()

        self.Username = tk.StringVar()
        self.Password = tk.StringVar()

        self.Lbl_Title = tk.Label(self.Frame, text='Login Menu', font=('arial', 55, 'bold'), bg='lightskyblue',
                               fg='Black')
        self.Lbl_Title.grid(row=0, column=0, columnspan=3, pady=40)

        self.Login_Frame_1 = tk.LabelFrame(self.Frame, width=1350, height=600, relief='ridge', bg='lightskyblue', bd=15,
                                        font=('arial', 20, 'bold'))
        self.Login_Frame_1.grid(row=1, column=0)
        self.Login_Frame_2 = tk.LabelFrame(self.Frame, width=1000, height=600, relief='ridge', bg='lightskyblue', bd=15,
                                        font=('arial', 20, 'bold'))
        self.Login_Frame_2.grid(row=2, column=0)

        self.Label_Username = tk.Label(self.Login_Frame_1, text='Username', font=('arial', 20, 'bold'),
                                    bg='lightskyblue', bd=20)
        self.Label_Username.grid(row=0, column=0)
        self.text_Username = tk.Entry(self.Login_Frame_1, font=('arial', 20, 'bold'), textvariable=self.Username)
        self.text_Username.grid(row=0, column=1, padx=50)

        self.Label_Password = tk.Label(self.Login_Frame_1, text='Password', font=('arial', 20, 'bold'),
                                    bg='lightskyblue', bd=20)
        self.Label_Password.grid(row=1, column=0)
        self.text_Password = tk.Entry(self.Login_Frame_1, font=('arial', 20, 'bold'), show='*', textvariable=self.Password)
        self.text_Password.grid(row=1, column=1)

        self.btnLogin = tk.Button(self.Login_Frame_2, text='Login', width=10, font=('airia', 15, 'bold'),
                               command=self.Login)
        self.btnLogin.grid(row=3, column=0, padx=8, pady=20)

        self.btnRegister = tk.Button(self.Login_Frame_2, text='Register', width=10, font=('airia', 15, 'bold'),
                                  command=self.Register)
        self.btnRegister.grid(row=3, column=1, padx=8, pady=20)

        self.btnExit = tk.Button(self.Login_Frame_2, text='Exit', width=10, font=('airia', 15, 'bold'), command=self.Exit)
        self.btnExit.grid(row=3, column=2, padx=8, pady=20)

        # Load usernames and passwords from a file
        self.Passwords = self.load_passwords()

    def load_passwords(self):
        try:
          with open("passwords.json", "r") as file:
            try:
                return json.load(file)
            except json.JSONDecodeError:
                # Handle empty or invalid JSON file
                return {}
        except FileNotFoundError:
         return {}


    def save_passwords(self):
        with open("passwords.json", "w") as file:
            json.dump(self.Passwords, file)

    def Login(self):
        u = self.Username.get()
        p = self.Password.get()

        hashed_password = hashlib.md5(p.encode()).hexdigest()

        if u in self.Passwords and self.Passwords[u] == hashed_password:
            self._menu_()
        else:
            tk.messagebox.askyesno("Login", "Error: Wrong Password")
            self.Username.set("")
            self.Password.set("")

    def Register(self):
        u = self.Username.get()
        p = self.Password.get()

        if u == "" or p == "":
            tk.messagebox.askyesno("Registration", "Error: Please enter a username and password")
            return

        if u in self.Passwords:
            tk.messagebox.askyesno("Registration", "Error: Username already exists")
            return

        hashed_password = hashlib.md5(p.encode()).hexdigest()
        self.Passwords[u] = hashed_password

        tk.messagebox.askyesno("Registration", "Registration successful! You can now log in.")

        self.save_passwords()
        self.Username.set("")
        self.Password.set("")

    def Exit(self):
        self.Exit = tk.messagebox.askokcancel("Login System", "Confirm if you want to Exit")
        if self.Exit > 0:
            self.master.destroy()
            return

    def _menu_(self):
        filename = 'reg.py'
        
        os.startfile(filename)

if __name__ == '__main__':
    main()
