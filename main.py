from lib import ui

while True:
    choice = input("CLI or Tkinter?")
    
    if choice.lower() == "cli":
        ui.create_ui()
        break
    
    elif choice.lower() == "tkinter":
        ui.cli_interface()
        break
    
    else:
        print("Invalid choice, choose again.")
