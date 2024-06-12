from lib import ui

while True:
    choice = input("CLI or Tkinter?")
    
    if choice.lower() == "tkinter":
        ui.create_ui()
        break
    
    elif choice.lower() == "cli":
        ui.cli_interface()
        break
    
    else:
        print("Invalid choice, choose again.")
