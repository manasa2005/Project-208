import socket
import tkinter as tk
from tkinter import *
from tkinter import ttk

SERVER = None
PORT = 8050
IP_ADDRESS = '127.0.0.1'
BUFFER_SIZE = 4096

def setup():
    global SERVER, PORT, IP_ADDRESS
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((SERVER, PORT))
    print(f"Connected to server {SERVER}:{PORT}")

def musicWindow():
    selectlabel = Label(window, text = "Select song", bg="LightBlueSky", front=("Calibri", 8))
    selectlabel.place(x=2, y=1)

    scrollbar1 = Scrollbar(listbox)
    scrollbar1.place(relheight = 1, relx = 1)
    scrollbar1.config(command = listbox.yview)

def main():
    setup()
    musicWindow()

if __name__ == "__main__":
    main()
