while True:
    user_input=input("Enter the input (type 'stop' to end): ")
    if user_input.lower()=="stop":
        print("Program Stopped")
        break
    else:
        print(f"Yor entered {user_input}")