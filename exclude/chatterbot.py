from chatterbot import ChatBot
import tkinter as tk

try:
    import ttk as ttk
    import ScrolledText
except ImportError:
    import tkinter.ttk as tk
    import tkinter.scrolledtext as ScrolledText
import time

class TkinterGuiExample(tk.Tk):

    def __init__(self, *args, **kwargs):

        tk.Tk.__init_(self,*args,**kwargs)

        self.chatbot = ChatBot(
            "Alfred",
            storage_adapter = "chatterbot.storage.SQLStorage.Adapter",
            logic_adapter =[
                "chatterbot.logic.BestMatch"
            ],
            database_Url = "sqlite:///database.sqlite3"
            )

        self.title("Baby Alfred #1")

        self.initialize()

    def initialize(self):
        self.grid ()

        self.respond = ttk.Button (self, Text = "Get Response", command = self.get_response)
        self.respond.grip(colum=0, row=0, sticky='nesw', padx=3, pady=3)

        self.usr_input = ttk.Entry(self, state='normal')
        self.usr_input. grid (column=1, row=0, sticky='nesw', padx=3, pady=3)

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
gui_example,tk.mainloop()

