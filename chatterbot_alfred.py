from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import tkinter as tk
import sys

try:
    import ttk as ttk
    import ScrolledText
except ImportError:
    import tkinter.ttk as ttk
    import tkinter.scrolledtext as ScrolledText
import time

class TkinterGuiExample(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk().__init__()
        tk.Tk('720x720')
        self.grid()


        self.chatbot = ChatBot(
            "Alfred",
            storage_adapter = "chatterbot.storage.SQLStorageAdapter",
            logic_adapter =[
                {
                'import_patch': "chatterbot.logic.BestMatch"
                }
            ],
            database_Url = "sqlite:///database.sqlite3"
            )

        trainer = ListTrainer(self.chatbot)

        trainer.train([
            'Olá',
            'Tudo bem?',
            'Sim e com você?',

        ])


        self.initialize()

    def initialize(self):

        tk.Tk('720x720')
        self.grid()

        self.respond = ttk.Button (self, Text = "Get Response", command = self.get_response)
        self.respond.grip(colum=0, row=0, sticky='nesw', padx=3, pady=3)

        self.usr_input = ttk.Entry(self, state='normal')
        self.usr_input.grid (column=1, row=0, sticky='nesw', padx=3, pady=3)

        self.conversation_lbl = ttk.Label(self, anchor=tk.E, text='Conversation: ')
        self.conversation_lbl.grid(column=0, row=1, sticky='nesw', padx=3, pady=3)

        self.conversation = ScrolledText.ScrolledText(self, state= 'disabled')
        self.conversation.grid(column=0,row=2, columnspan=2, sticky='nesw', padx=3, pady=3)


    def get_response(self):

        user_input = self.usr_input.get()
        self.usr_input.delete(0, tk.END)

        response = self.chatbot.get_response(user_input)
        self.conversation.insert(
            tk.END, "Human: " + "\n" + "ChatBot: " + str(response.text) + "\n"
        )
        self.conversation['state']='disabled'
        time.sleep(0.5)


gui_example = TkinterGuiExample()
print(sys.setecursionlimit(150))
gui_example.mainloop()

