from chatterbot import ChatBot
from chatterbot import trainers

alfred = ChatBot(
    'Baby Alfred',
    storage_adapter = 'K:\\Capturas Tokio\\sqlite-snapshot-202108231028',
    logic_adapters= [
        'chatterbot.logic.MathematicalEvaluation',
        'chatterbot.logic.TimeLogicAdapter'
    ],
    
    database_uri = 'sqlite:///database.sqlite3'
)

while True:
    try:
        alfred_input = alfred.get_response(input())
        print(alfred_input)

    except (KeyboardInterrupt, EOFError, SystemExit):
        break


trainer = trainers.ListTrainer(alfred)

trainer.train([
    'How are you?',
    'I am good.',
    'That is good to hear.',
    'Thank You',
    'You are welcome.',

])