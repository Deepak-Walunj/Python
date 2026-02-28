import requests
import random

def fetch_question():
    try:
        req = requests.get("https://opentdb.com/api.php?amount=1&type=multiple")
        req.raise_for_status()  
        data = req.json()['results'][0]
        question = data['question']
        correct_answer = data['correct_answer']
        incorrect_answers = data['incorrect_answers']
        options = incorrect_answers + [correct_answer]
        random.shuffle(options)
        return {
            'question': question,
            'options': options,
            'correct_answer': correct_answer
        }
    except requests.exceptions.RequestException as e:
        print(f"Error fetching question: {e}")
        return None
    except (KeyError, IndexError) as e:
        print(f"Error parsing question data: {e}")
        return None


def main():
    levels = [1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000, 160000, 320000, 640000, 1250000, 2500000, 5000000, 10000000]
    money = 0
    i = 0

    while i < len(levels):
        Questions = fetch_question()
        question = Questions['question']
        options = Questions['options']
        correct_answer = Questions['correct_answer']

        print(f"And the next question on your screen is: {question}")
        print("And the options for this question are:")
        print(f"1) {options[0]}                2) {options[1]}")
        print(f"3) {options[2]}                4) {options[3]}")

        try:
            op = int(input(f"Enter your choice (1-4): ..... you can quit the game also, you will not lose any money if you quit now, otherwise you will fall off to Rs {money}\nPress 5 to quit: "))
        except ValueError:
            print("Please enter a number between 1 and 5")
            continue
        if op == 5:
            if i == 0:
                print("You have chosen to quit the game without answering any questions. You take home Rs 0")
                print(f'The correct answer was...{correct_answer}')
            else:
                print(f"So you have chosen to quit the game!\nTotal money you take home is Rs {levels[i - 1]}")
                print(f'The correct answer was...{correct_answer}')
            break
        elif 1 <= op <= 4:
            given_ans = options[op - 1]
            if given_ans == correct_answer:
                print(f"Congratulations! You have won Rs {levels[i]}")
                if levels[i] == 10000:
                    money = 10000
                elif levels[i] == 320000:
                    money = 320000
                elif levels[i] == 10000000:
                    money = 10000000
                i += 1
            else:
                print("Wrong answer. Unfortunately, you lost.")
                print(f"Since you gave the wrong answer, you can only take the boundary level money. You take home Rs {money}")
                print(f'The correct answer was...{correct_answer}')
                break
        else:
            print("Invalid option... Enter a number between 1 and 5")

    if i == len(levels):
        print(f"Game over. You take home Rs {levels[-1]}")

if __name__ == "__main__":
    main()
