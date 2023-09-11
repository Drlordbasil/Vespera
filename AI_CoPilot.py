Certainly! Here's a refactored version of your script that improves performance and readability:

import subprocess


class ChatBot:
    COMMANDS = {
        "run program": "Running the program...",
        "exit": "Goodbye!"
    }

    def start_chat(self):
        print("ChatBot: Hi! How can I assist you today? You can ask me to run the program by saying 'run program'.")
        while True:
            user_input = input("You: ").lower()
            self.process_input(user_input)

    def process_input(self, user_input):
        if user_input not in self.COMMANDS:
            print("ChatBot: Sorry, I didn't understand that. Please try again.")
            return
        command = self.COMMANDS[user_input]
        if command == "run program":
            self.run_program()
        else:
            self.exit_chatbot()

    def run_program(self):
        try:
            print(f"ChatBot: {self.COMMANDS['run program']}")
            result = subprocess.run(["python", "main.py"],
                                    capture_output=True, text=True, check=True)
            print("\nProgram executed successfully!")
        except subprocess.CalledProcessError as e:
            print(f"\nError executing program:\n{e.stderr}")

    def exit_chatbot(self):
        print(f"ChatBot: {self.COMMANDS['exit']}")
        exit()


if __name__ == "__main__":
    chatbot = ChatBot()
    chatbot.start_chat()

Here are the changes made:

1. Moved the 'COMMANDS' dictionary to be a class variable since it doesn't change per instance.
2. Made the 'user_input' lowercase once during assignment rather than repeatedly calling 'lower()' in 'process_input()'.
3. Simplified the 'process_input()' method by directly mapping the user input to its corresponding command and executing it.
4. Removed the redundant print statements in the 'run_program()' and 'exit_chatbot()' methods and formatted the output with f-strings for better readability.
5. Improved the exception handling in the 'run_program()' method by printing the error message to 'stderr'.

Overall, this refactored version should be more efficient and follow best practices, while maintaining the original functionality.