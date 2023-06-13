

if __name__ == "__main__":
    secret_nummber =int (9)

    while True:
        user_input :int = int(input("Guess my serect number: "))
        if user_input == secret_nummber:
            print("you won")
            break
        else:
            print("you no do")