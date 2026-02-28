import win32com.client
import os

def get_speaker():
    return win32com.client.Dispatch("SAPI.SpVoice")

def read_file(filepath, speaker):
    try:
        with open(filepath, "r") as file:
            content = file.read()
            speaker.Speak(content)
    except FileNotFoundError:
        print('File not found.')
    except Exception as e:
        print(f'An error occurred: {e}')

def pronounce_word(word, speaker):
    try:
        speaker.Speak(word)
    except Exception as e:
        print(f'An error occurred: {e}')

def main():
    speaker = get_speaker()
    base_directory = "C:\\Users\\Deepak\\OneDrive\\Desktop\\Python\\PROJECTS\\project_8"

    while True:
        try:
            choice = int(input('Enter:\n1) For pronunciation\n2) To read a file\n3) To stop\n'))
            
            if choice == 1:
                word = input('Enter the word to be pronounced: ')
                pronounce_word(word, speaker)
                
            elif choice == 2:
                filename = input(f"Enter the file name to be read (ensure it's in {base_directory}):\n")
                filepath = os.path.join(base_directory, f"{filename}.txt")
                read_file(filepath, speaker)
                
            elif choice == 3:
                print("Exiting the program.")
                break
                
            else:
                print("Please enter a number between 1 and 3.")
                
        except ValueError:
            print('Invalid input, please enter a number.')
        except Exception as e:
            print(f'An error occurred: {e}')

if __name__ == "__main__":
    main()
