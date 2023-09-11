import subprocess


class ChatBot:
    def __init__(self):
        self.commands = {
            "run program": self.run_program,
            "exit": self.exit_chatbot
        }

    def start_chat(self):
        print("ChatBot: Hi! How can I assist you today? You can ask me to run the program by saying 'run program'.")
        while True:
            user_input = input("You: ")
            self.process_input(user_input.lower())

    def process_input(self, user_input):
        if user_input in self.commands:
            self.commands[user_input]()
        else:
            print("ChatBot: Sorry, I didn't understand that. Please try again.")

    def run_program(self):
        print("ChatBot: Running the program...")
        result = subprocess.run(["python", "main.py"],
                                capture_output=True, text=True)
        if result.returncode == 0:
            print("\nProgram executed successfully!")
        else:
            print(f"\nError executing program:\n{result.stderr}")

    def exit_chatbot(self):
        print("ChatBot: Goodbye!")
        exit()


if __name__ == "__main__":
    chatbot = ChatBot()
    chatbot.start_chat()
