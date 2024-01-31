import pyttsx3

def robo(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

if __name__ == '__main__':
    print("Welcome to ROBO")
    print("Enter 'q' to quit.")

    while True:
        user_input = input("Enter text (or 'q' to quit): ")

        if user_input.lower() == 'q':
            print("Exiting the program. Goodbye!")
            break

        robo(user_input)


