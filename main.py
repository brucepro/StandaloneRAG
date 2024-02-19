from commandhandler import CommandHandler

def process_string(input_string):
    # Your processing logic goes here
    databasefile = "none"
    collection = "ragtester1"
    handler = CommandHandler(databasefile,collection)
    commands_output = handler.process_command(input_string)
    
    return commands_output

while 1==1:
  input_string = input("Enter your string input: ")
  output = process_string(input_string)
  print(output)