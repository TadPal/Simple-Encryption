from tkinter import *

class EncoderDecoderView:
    def __init__(self, logic):
        self.root = Tk()
        self.root.geometry("500x300")
        self.root.resizable(0,0)
        self.root.title("Message Encoder and Decoder")
        self.logic = logic

        Label(self.root, text="Encoder and Decoder", font = "arial 20 bold").pack()

        self.text_var = StringVar()
        self.private_key_var = StringVar()
        self.result_var = StringVar()

        Label(self.root, font="arial 12 bold", text="MESSAGE").place(x=60, y=60)
        Entry(self.root, font="arial 10", textvariable=self.text_var, bg = "ghost white", width=30).place(x=190, y=60)

        Label(self.root, font="arial 12 bold", text="KEY FILENAME").place(x=60, y=90)
        Entry(self.root, font="arial 10", textvariable=self.private_key_var, bg = "ghost white", width=30).place(x=190, y=90)

        Label(self.root, font="arial 12 bold", text="RESULT").place(x=60,y=120)
        Entry(self.root, font="arial 10 bold", textvariable=self.result_var, bg = "ghost white", width=30).place(x=190, y=120)

        Button(self.root, font="arial 10 bold", text = "LOAD KEYS", padx=2, bg="OrangeRed", width=8, height=2, command=self.load_keys).place(x=150, y=190)
        Button(self.root, font="arial 10 bold", text = "SAVE KEYS", padx=2, bg="LimeGreen", width=8, height=2, command=self.save_keys).place(x=50, y=190)
        Button(self.root, font="arial 10 bold", text = "ENCODE", padx=2, bg="LimeGreen", width=8, height=2, command=self.encode).place(x=250, y=190)
        Button(self.root, font="arial 10 bold", text = "DECODE", padx=2, bg="OrangeRed", width=8, height=2, command=self.decode).place(x=350, y=190)
        
        self.root.mainloop()

    def load_keys(self):
        priv_file = self.private_key_var.get() + '.priv'
        pub_file = self.private_key_var.get() + '.pub'
        self.logic.load_keys(priv_file, pub_file)

    def save_keys(self):
        priv_file = self.private_key_var.get() + '.priv'
        pub_file = self.private_key_var.get() + '.pub'
        self.logic.save_keys(priv_file, pub_file)

    def encode(self):
        self.logic.text = self.text_var.get()
        self.logic.encode()
        self.result_var.set(self.logic.result)

    def decode(self):
        self.logic.text = self.text_var.get().encode()
        self.logic.decode()
        self.result_var.set(self.logic.result)


