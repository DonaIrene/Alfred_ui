import tkinter as tk
from tkinter.constants import END
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from tkinter import ttk, scrolledtext
import sys
import time



class TkinterGuiExample(tk.Tk):
         
        def __init__(self,*args, **kwargs):
                

            bot = ChatBot(
                'alfred',
                storage_adapter ='chatterbot.storage.SQLStorageAdapter',
                logic_adapters = [{
                'import_path': 'chatterbot.logic.BestMatch',
                'defeault_response': "I'm sorry, but I do not understand.",
                'maximum_similarity_threshold': 0.90
            }],
            database_uri = 'sqlite:///database.sqlite3'
            )

            treiner = ListTrainer(bot)

            treiner.train = ([
            'Oi',
            'Tudo bem?',
            'Sim e com você?',
            'Ainda Bem, é bom ouvir isso!'
        ])


        def UI_app(self):
            self.respond = ttk.Button(self, Text = "Get Response", command= self.get_response)
            self.respond.grid(colum=0,row=0, sticky='nesw',padx=3,pady=3)

            self.usr_input = ttk.Entry (self, state=' normal ')
            self.usr_input.grid(column=1, row=0, sticky='nesw', padx=3, pady=3)

            self.conversation_lbl = ttk.Label(self, anchor=gui_ui_example, text='Conversation: ')
            self.conversation_lbl.grid(column=0, row=1, sticky='nesw',padx=3, pady=3)

            self.conversation = scrolledtext.ScrolledText(self, state = 'disabled')
            self.conversation.grid(column=0, row=2, columnspan=2, sticky='nesw', padx=3,pady=3)
            

        def get_response(self):
                 
                usr_input = self.usr_input.get()
                self.usr_input.delete(0, tk.END)

                response = self.bot.get_response(usr_input)
                self.conversation.insert(
                    tk.END,"Self: " + "\n" + "Bot: " + str(response.text) + '\n'
            )
                self.conversation['state'] = 'enable'
                time.sleep (0.9)
                


gui_ui_example = TkinterGuiExample()
print(sys.setrecursionlimit(150))
gui_ui_example.tk.mainloop()