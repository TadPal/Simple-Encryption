from tkinter import *

class EncoderDecoderView:
    def __init__(self, logic):
        # Create a Tkinter Tk object and set the size and title of the window
        self.top = Toplevel()
        self.top.geometry("500x300")
        self.top.resizable(0,0)
        self.top.title(logic.name)
        self.logic = logic # Assign the logic attribute

        # Place a label with the text "Encoder and Decoder" at the top of the window
        Label(self.top, text="Encoder and Decoder", font = "arial 20 bold").pack()

        # Create StringVar objects for storing the message text, private key, and resulting encoded/decoded text
        self.text_var = StringVar()
        self.private_key_var = StringVar()
        self.result_var = StringVar()

        # Create labels for the message text, private key, and resulting encoded/decoded text and place them on the window
        Label(self.top, font="arial 12 bold", text="MESSAGE").place(x=60, y=60)
        Label(self.top, font="arial 12 bold", text="KEY").place(x=60, y=90)
        Label(self.top, font="arial 12 bold", text="RESULT").place(x=60, y=120)

        # Create entry fields for the message text, private key, and resulting encoded/decoded text and place them on the window
        # Set the textvariable attribute of the entry fields to the corresponding StringVar object
        Entry(self.top, font="arial 10", textvariable=self.text_var, bg = "ghost white", width=30).place(x=190, y=60)
        Entry(self.top, font="arial 10", textvariable=self.private_key_var, bg = "ghost white", width=30).place(x=190, y=90)
        Entry(self.top, font="arial 10 bold", textvariable=self.result_var, bg = "ghost white", width=30).place(x=190, y=120)

        # Create buttons for encoding and decoding and place them on the window
        # Set the command attribute of the buttons to the encode and decode methods respectively
        Button(self.top, font="arial 10 bold", text = "ENCODE", padx=2, bg="LimeGreen", width=8, height=2, command=self.encode).place(x=150, y=190)
        Button(self.top, font="arial 10 bold", text = "DECODE", padx=2, bg="OrangeRed", width=8, height=2, command=self.decode).place(x=270, y=190)

        self.top.mainloop()

    
    def encode(self):
        # Get the message text and private key from the text_var and private_key_var respectively
        self.logic.text = self.text_var.get()
        self.logic.private_key = self.private_key_var.get()
        # Call the encode method of the logic class
        self.logic.encode()
        # Update the result_var with the value of the result attribute of the logic class
        self.result_var.set(self.logic.result)

    def decode(self):
        # Get the message text and private key from the text_var and private_key_var respectively
        self.logic.text = self.text_var.get()
        self.logic.private_key = self.private_key_var.get()
        # Call the decode method of the logic class
        self.logic.decode()
        # Update the result_var with the value of the result attribute of the logic class
        self.result_var.set(self.logic.result)

        
