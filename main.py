import base64
import io
import threading
from socket import socket, AF_INET, SOCK_STREAM


from customtkinter import *
from tkinter import filedialog
from PIL import Image
from AuthWindowClass import AuthWindow
from MainWindowClass import MainWindow


if __name__ == "__main__":
    AuthWindow().mainloop()