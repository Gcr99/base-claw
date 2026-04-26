from src.agent import run_agent

def main():
    print("🦂 Base Claw Activated!")
    print("Type 'exit' to quit\n")

    while True:
        user_input = input(">> ")

        if user_input.lower() == "exit":
            break

        result = run_agent(user_input)
        print(result)

if __name__ == "__main__":
    main()
