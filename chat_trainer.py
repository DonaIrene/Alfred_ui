from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer



bot = ChatBot(
    'alfred',
    storage_adapter ='chatterbot.storage.SQLStorageAdapter',
    logic_adapters = [
        {
        'import_path': 'chatterbot.logic.BestMatch',
        'defeault_response': "I'm sorry, but I do not understand.",
        'maximum_similarity_threshold': 0.90
        }
    ],
    database_uri = 'sqlite:///database.sqlite3'
)

treiner = ListTrainer(bot)

treiner.train = ([
    'Oi',
    'Tudo bem?',
    'Sim e com você?',
    'Ainda Bem, é bom ouvir isso!'
])


while True:
    try:
        bot_input = bot.get_response(input())
        print(bot_input)
        

    except (KeyboardInterrupt, EOFError, SystemError):
        break

response = bot.get_response('')
print(response)