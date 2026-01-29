from customtkinter import *
from socket import *
from MainWindowClass import MainWindow

class AuthWindow(CTk):
    def __init__(self):
        super().__init__()
        self.title("Authentication")
        self.geometry("400x300")
        self.username = None

        self.label = CTkLabel(self, text="Please log in")
        self.label.pack(pady=20)


        self.username_entry = CTkEntry(self, placeholder_text="nickname")
        self.username_entry.pack(pady=10)

        self.ip_entry = CTkEntry(self, placeholder_text="ip")
        self.ip_entry.pack(pady=10)

        self.port_entry = CTkEntry(self, placeholder_text="port")
        self.port_entry.pack(pady=10)

        self.login_button = CTkButton(self, text="connect", command=self.authenticate)
        self.login_button.pack(pady=20)

    def authenticate(self):
        self.username = self.username_entry.get()
        try:
            self.sock = socket(AF_INET, SOCK_STREAM)
            self.sock.connect((self.ip_entry.get(), int(self.port_entry.get())))
            hello = f"TEXT@{self.username}@[SYSTEM] {self.username} has connected to the server."
            self.sock.send(hello.encode('utf-8'))
            self.destroy()
            win = MainWindow(self.sock, self.username)
            win.mainloop()
        except Exception as e:
            print(f"Connection failed: {e}")

