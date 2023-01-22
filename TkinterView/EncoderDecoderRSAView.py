from tkinter import *

class EncoderDecoderView:
    def __init__(self, logic):
        self.top = Toplevel()
        self.top.geometry("500x300")
        self.top.resizable(0,0)
        self.top.title(logic.name)
        self.logic = logic

        Label(self.top, text="Encoder and Decoder", font = "arial 20 bold").pack()

        self.keys_status_label = Label(self.top, font="arial 12 bold", text="Load Keys", fg="OrangeRed")
        self.keys_status_label.place(x=60, y=150)

        Label(self.top, font="arial 12 bold", text="MESSAGE").place(x=60, y=60)
        self.text_var = StringVar()
        Entry(self.top, font="arial 10", textvariable=self.text_var, bg = "ghost white", width=30).place(x=190, y=60)

        Label(self.top, font="arial 12 bold", text="KEY FILENAME").place(x=60, y=90)
        self.private_key_var = StringVar()
        Entry(self.top, font="arial 10", textvariable=self.private_key_var, bg = "ghost white", width=30).place(x=190, y=90)

        Label(self.top, font="arial 12 bold", text="RESULT").place(x=60,y=120)
        self.result_var = StringVar()
        Entry(self.top, font="arial 10 bold", textvariable=self.result_var, bg = "ghost white",width=30).place(x=190, y=120)
        
        Button(self.top, font="arial 10 bold", text = "LOAD KEYS", padx=2, bg="OrangeRed", width=8, height=2, command=self.load_keys).place(x=150, y=190)
        Button(self.top, font="arial 10 bold", text = "SAVE KEYS", padx=2, bg="LimeGreen", width=8, height=2, command=self.save_keys).place(x=50, y=190)
        Button(self.top, font="arial 10 bold", text = "ENCODE", padx=2, bg="LimeGreen", width=8, height=2, command=self.encode).place(x=250, y=190)
        Button(self.top, font="arial 10 bold", text = "DECODE", padx=2, bg="OrangeRed", width=8, height=2, command=self.decode).place(x=350, y=190)

        self.top.mainloop()

    def load_keys(self):
        priv_file = self.private_key_var.get() + '.pem'
        pub_file = self.private_key_var.get() + '_pub.pem'
        try:
            self.logic.load_keys(priv_file, pub_file)
            self.keys_status_label.config(text="Keys Loaded", fg="LimeGreen")
        except Exception as e:
            self.keys_status_label.config(text="Error Loading Keys", fg="OrangeRed")

    def save_keys(self):
        priv_file = self.private_key_var.get() + '.pem'
        pub_file = self.private_key_var.get() + '_pub.pem'
        self.logic.save_keys(priv_file, pub_file)

    def encode(self):
        self.logic.text = self.text_var.get()
        self.logic.encode()
        self.result_var.set(self.logic.result.hex())

    def decode(self):
        self.logic.text = bytearray.fromhex(self.text_var.get())
        self.logic.decode()
        self.result_var.set(self.logic.result)

