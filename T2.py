def display_menu():          
    print("Help")
    print("====")
    print("The following commands are recognized:")
    print("Display help:                          wildlife> help") 
    print("Exit the application:                  wildlife> exit") 
  
def main():
    display_menu()             
    while True:
        user_input = input("wildlife> ").strip().lower() 
        if user_input == "help":
            display_menu()
        elif user_input == "exit":
            print("Exit")
            return             
        else:
            print("Error") 
    
main()
