
import tkinter as tk
from tkinter.constants import N
from tkinter.scrolledtext import ScrolledText
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer, Trainer
from tkinter import Button, ttk
import tkinter.scrolledtext as ScrolledText




class Alfred_Bot(tk.Frame):
    
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.app_interface()
    
    
    def chatbot_mem(self):
        chatbot = ChatBot(
            'Baby Alfred',
        storage_adapter = 'chatterbot.storage.SQLStorageAdapter',
        logic_adapter = [
            {
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
        while True:
            try:
                bot_input = chatbot.get_response(input())
                

            except(KeyboardInterrupt, EOFError, SystemExit):
                break
        

    def app_interface(self):
        self.app_gui_conversation = ttk.Label (self, text='Conversa')
        self.app_gui_conversation.pack(side='top')

        self.app_gui_button = ttk.Button(self, text='Confirm' ,command= self.chatbot_mem)
        self.app_gui_button.pack( anchor='nw')
        
        self.app_gui_conversation_scr = ScrolledText.ScrolledText (self, state= 'disabled')
        self.app_gui_conversation.pack()

        self.app_gui_entry = ttk.Entry(self, state='normal')
        self.app_gui_entry.pack(anchor= 's')

    
    



root = tk.Tk('720x720')
app = Alfred_Bot(master=root)
app.mainloop()
