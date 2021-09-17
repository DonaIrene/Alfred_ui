from os import stat
import tkinter as tk
from tkinter.constants import N
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from tkinter import Button, ttk
import time





class Alfred_Bot(tk.Frame):
    
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.app_interface()
    
    
    def chatbot_mem():
        chatbot = ChatBot(
            'Baby Alfred',
        storage_adapter = 'chatterbot.storage.SQLStorage.Adapter',
        logic_adapter = [{
            "chatterbot.logic.BestMatch"

        }
        ],
        database_url = "sqlite:///database.sqlite3"
)
        trainer = ListTrainer(chatbot)

        trainer.train([
            'ola',
            'Tudo bem?',

    ])

    
    
    def app_interface(self):
        self.app_gui_conversation = ttk.Label (self, text='Conversa')
        self.app_gui_conversation.pack(side='top')

        self.app_gui_button = ttk.Button(self, text='Confirm' ,command=self.get_response)
        self.app_gui_button.pack( anchor='nw')
        
        self.app_gui_input = ttk.Entry(self, state='normal')
        self.app_gui_input.pack(anchor='nw')


    def get_response(self):

        app_gui_input = self.app_gui_input.get()
        self.app_gui_input.delete(0, tk.END)

        response = self.chatbot.get_response(app_gui_input)
        self.app_gui_conversation.insert(str (response)
        )
        self.app_gui_conversation['state']='disabled'
        time.sleep(0.1)
    
    
        

root = tk.Tk()
app = Alfred_Bot(master=root)
app.mainloop()

