# import speech_recognition as sr
# import requests
# import win32com.client
# import time

# recognizer = sr.Recognizer()
# Speaker = win32com.client.Dispatch("SAPI.SpVoice")

# def fetch_news(url, cat):
#     try:
#         r = requests.get(url)
#         r.raise_for_status()
#         data = r.json()["news"]

#         titles = [d["title"] for d in data if "title" in d and d.get("language") == "en"  and cat in d.get("category", [])]
#         descriptions = [d["description"] for d in data if "description" in d and d.get("language") == "en"  and cat in d.get("category", [])]
#         published = [d["published"].split(" ")[0] for d in data if "published" in d and d.get("language") == "en"  and cat in d.get("category", [])]
#         urls = [d["url"] for d in data if "url" in d and d.get("language") == "en"  and cat in d.get("category", [])]
#         cate=[d["category"] for d in data if "category" in d and d.get("language") == "en" and cat in d.get("category", [])]
#         for t, d, p, u, c in zip(titles, descriptions, published, urls, cate):
#             print(f"Title:\n{t}\nDescription:\n{d}\nPublished:\n{p}\nurl:\n{u}\nCategory:\n{c}\n")
#             Speaker.Speak(f"Title: {t}")
#             Speaker.Speak(f"Description: {d}")
#             Speaker.Speak(f"Published on: {p}")
#             Speaker.Speak(f"For more details, visit the URL")
#             while Speaker.Status.RunningState == 2:  # 2 indicates that the speaker is speaking
#                 time.sleep(1)
#             time.sleep(5)  # Wait for 5 seconds before moving to the next news item

#     except Exception as e:
#         print(f"Error: {e}")

# def main():
#     url = f'https://api.currentsapi.services/v1/latest-news?apiKey=bxc0hg6IzVfeYWpmW9-OiclHRPk8uUOmPREivANKmYKnJmNc'
#     Speaker.Speak('Hello user, which kind of news do you want to hear?')
#     print('General news, Sports news, Regional news, Programming news, Technology news, Academia news, Gadgets news, World news, Game news')
#     Speaker.Speak('General news, Sports news, Regional news, Programming news, Technology news, Academia news, Gadgets news, World news, Game news')
#     valid_categories = ["general", "sports", "regional", "programming", "technology", "academia", "gadgets", "world", "game"]

#     while True:
#         with sr.Microphone() as source:
#             print("Adjusting for ambient noise... Please wait.")
#             recognizer.adjust_for_ambient_noise(source)
#             print("Listening...")
#             audio = recognizer.listen(source)

#             try:
#                 print("Recognizing...")
#                 text = recognizer.recognize_google(audio).lower().strip()
#                 print("You said: " + text)
#                 print(f"Valid categories: {valid_categories}")

#                 # Check if any valid category is mentioned in the text
#                 matched_categories = [cat for cat in valid_categories if cat in text]
#                 if matched_categories:
#                     category = matched_categories[0]
#                     print(f"Matched category: {category}")
#                     fetch_news(url, category)
                    
#                 else:
#                     print("Invalid category.")
#                     Speaker.Speak('Invalid category. Please try again.')

#             except sr.UnknownValueError:
#                 print("Google Speech Recognition could not understand the audio")
#             except sr.RequestError as e:
#                 print(f"Could not request results from Google Speech Recognition service; {0}".format(e))

# if __name__ == "__main__":
#     main()

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>Using ASYNCIO<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

# import speech_recognition as sr
# import requests
# import win32com.client
# import asyncio
# import sys

# stop_flag = False
# exit_flag = False
# recognizer = sr.Recognizer()
# Speaker = win32com.client.Dispatch("SAPI.SpVoice")

# async def fetch_news(url, cat):
#     global stop_flag, exit_flag
#     try:
#         r = requests.get(url)
#         r.raise_for_status()
#         data = r.json()["news"]

#         titles = [d["title"] for d in data if "title" in d and d.get("language") == "en" and cat in d.get("category", [])]
#         descriptions = [d["description"] for d in data if "description" in d and d.get("language") == "en" and cat in d.get("category", [])]
#         published = [d["published"].split(" ")[0] for d in data if "published" in d and d.get("language") == "en" and cat in d.get("category", [])]
#         urls = [d["url"] for d in data if "url" in d and d.get("language") == "en" and cat in d.get("category", [])]
#         cate = [d["category"] for d in data if "category" in d and d.get("language") == "en" and cat in d.get("category", [])]

#         for t, d, p, u, c in zip(titles, descriptions, published, urls, cate):
#             if stop_flag or exit_flag:
#                 return
#             print(f"Title:\n{t}\nDescription:\n{d}\nPublished:\n{p}\nurl:\n{u}\nCategory:\n{c}\n")
#             Speaker.Speak(f"Title: {t}")
#             Speaker.Speak(f"Description: {d}")
#             Speaker.Speak(f"Published on: {p}")
#             Speaker.Speak(f"For more details, visit the URL")
#             while Speaker.Status.RunningState == 2:  # 2 indicates that the speaker is speaking
#                 await asyncio.sleep(1)
#             await asyncio.sleep(3)  # Wait for 3 seconds before moving to the next news item

#     except Exception as e:
#         print(f"Error: {e}")

# async def listen_for_stop():
#     global stop_flag
#     while not stop_flag:
#         with sr.Microphone() as source:
#             recognizer.adjust_for_ambient_noise(source)
#             audio = recognizer.listen(source)
#             try:
#                 text = recognizer.recognize_google(audio).lower().strip()
#                 if "stop" in text:
#                     stop_flag = True
#                     Speaker.Speak("Stopping the news")
#                     print("Command taken... stopping the news")
#             except sr.UnknownValueError:
#                 pass
#             except sr.RequestError as e:
#                 print(f"Could not request results from Google Speech Recognition service; {e}")
#         await asyncio.sleep(1)

# async def listen_for_exit():
#     global exit_flag
#     while not exit_flag:
#         with sr.Microphone() as source:
#             recognizer.adjust_for_ambient_noise(source)
#             audio = recognizer.listen(source)
#             try:
#                 text = recognizer.recognize_google(audio).lower().strip()
#                 if "exit" in text:
#                     exit_flag = True
#                     Speaker.Speak("Exiting")
#                     print("Thankyou for listening the news")
#             except sr.UnknownValueError:
#                 pass
#             except sr.RequestError as e:
#                 print(f"Could not request results from Google Speech Recognition service; {e}")
#         await asyncio.sleep(1)


# async def main():
#     global stop_flag, exit_flag
#     url = f'https://api.currentsapi.services/v1/latest-news?apiKey=bxc0hg6IzVfeYWpmW9-OiclHRPk8uUOmPREivANKmYKnJmNc'
#     print('General news, Sports news, Regional news, Programming news, Technology news, Academia news, Gadgets news, World news, Game news')
#     # Speaker.Speak('Hello user, which kind of news do you want to hear?')
#     # Speaker.Speak('General news, Sports news, Regional news, Programming news, Technology news, Academia news, Gadgets news, World news, Game news')
#     valid_categories = ["general", "sports", "regional", "programming", "technology", "academia", "gadgets", "world", "game"]

#     while not exit_flag:
#         with sr.Microphone() as source:
#             print("Adjusting for ambient noise... Please wait.")
#             recognizer.adjust_for_ambient_noise(source)
#             print("Listening...")
#             audio = recognizer.listen(source)

#             try:
#                 print("Recognizing...")
#                 text = recognizer.recognize_google(audio).lower().strip()
#                 print("You said: " + text)
#                 print(f"Valid categories: {valid_categories}")

#                 # Check if any valid category is mentioned in the text
#                 matched_categories = [cat for cat in valid_categories if cat in text]
#                 if matched_categories:
#                     category = matched_categories[0]
#                     print(f"Matched category: {category}")
#                     # fetch_task = asyncio.create_task(fetch_news(url, category))
#                     # stop_task = asyncio.create_task(listen_for_stop())
#                     # stop_exit = asyncio.create_task(listen_for_exit())
#                     # await asyncio.gather(fetch_task, stop_task, stop_exit)
#                     stop_flag = False  # Reset the stop_flag for the next round of news fetching
#                     print("Invalid category.")
#                     Speaker.Speak('Invalid category. Please try again.')

#             except sr.UnknownValueError:
#                 print("Google Speech Recognition could not understand the audio")
#             except sr.RequestError as e:
#                 print(f"Could not request results from Google Speech Recognition service; {e}")

# if __name__ == "__main__":
#     asyncio.run(main())


#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>Using THREADS<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

# import speech_recognition as sr
# import requests
# import win32com.client
# import time
# from concurrent.futures import ThreadPoolExecutor

# stop_flag = False
# exit_flag = False
# recognizer = sr.Recognizer()
# Speaker = win32com.client.Dispatch("SAPI.SpVoice")

# def fetch_news(url, cat):
#     global stop_flag, exit_flag
#     try:
#         r = requests.get(url)
#         r.raise_for_status()
#         data = r.json()["news"]

#         titles = [d["title"] for d in data if "title" in d and d.get("language") == "en" and cat in d.get("category", [])]
#         descriptions = [d["description"] for d in data if "description" in d and d.get("language") == "en" and cat in d.get("category", [])]
#         published = [d["published"].split(" ")[0] for d in data if "published" in d and d.get("language") == "en" and cat in d.get("category", [])]
#         urls = [d["url"] for d in data if "url" in d and d.get("language") == "en" and cat in d.get("category", [])]
#         cate = [d["category"] for d in data if "category" in d and d.get("language") == "en" and cat in d.get("category", [])]

#         for t, d, p, u, c in zip(titles, descriptions, published, urls, cate):
#             if stop_flag or exit_flag:
#                 return
#             print(f"Title:\n{t}\nDescription:\n{d}\nPublished:\n{p}\nurl:\n{u}\nCategory:\n{c}\n")
#             Speaker.Speak(f"Title: {t}")
#             if stop_flag or exit_flag:
#                 return
#             Speaker.Speak(f"Description: {d}")
#             if stop_flag or exit_flag:
#                 return
#             Speaker.Speak(f"Published on: {p}")
#             if stop_flag or exit_flag:
#                 return
#             Speaker.Speak(f"For more details, visit the URL")
#             if stop_flag or exit_flag:
#                 return
#             while Speaker.Status.RunningState == 2:  # 2 indicates that the speaker is speaking
#                 time.sleep(1)
#             time.sleep(3)  # Wait for 3 seconds before moving to the next news item

#     except Exception as e:
#         print(f"Error: {e}")

# def listen_for_stop():
#     global stop_flag
#     while not stop_flag:
#         with sr.Microphone() as source:
#             recognizer.adjust_for_ambient_noise(source)
#             audio = recognizer.listen(source)
#             try:
#                 text = recognizer.recognize_google(audio).lower().strip()
#                 if "stop" in text:
#                     stop_flag = True
#                     Speaker.Speak("Stopping the news")
#                     print("Command taken... stopping the news")
#                     return
#             except sr.UnknownValueError:
#                 pass
#             except sr.RequestError as e:
#                 print(f"Could not request results from Google Speech Recognition service; {e}")
#         # time.sleep(1)

# def listen_for_exit():
#     global exit_flag
#     while not exit_flag:
#         with sr.Microphone() as source:
#             recognizer.adjust_for_ambient_noise(source)
#             audio = recognizer.listen(source)
#             try:
#                 text = recognizer.recognize_google(audio).lower().strip()
#                 if "exit" in text:
#                     exit_flag = True
#                     Speaker.Speak("Exiting")
#                     print("Thank you for listening to the news")
#                     return
#             except sr.UnknownValueError:
#                 pass
#             except sr.RequestError as e:
#                 print(f"Could not request results from Google Speech Recognition service; {e}")
#         # time.sleep(1)

# def main():
#     global stop_flag, exit_flag
#     #Speaker.Speak('Hello user, which kind of news do you want to hear?')
#     # Speaker.Speak('General news, Sports news, Regional news, Programming news, Technology news, Academia news, Gadgets news, World news, Game news')
#     url = f'https://api.currentsapi.services/v1/latest-news?apiKey=bxc0hg6IzVfeYWpmW9-OiclHRPk8uUOmPREivANKmYKnJmNc'
#     print('General news, Sports news, Regional news, Programming news, Technology news, Academia news, Gadgets news, World news, Game news')
#     valid_categories = ["general", "sports", "regional", "programming", "technology", "academia", "gadgets", "world", "game"]

#     while not exit_flag:
#         with sr.Microphone() as source:
#             print("Adjusting for ambient noise... Please wait.")
#             recognizer.adjust_for_ambient_noise(source)
#             print("Listening...")
#             audio = recognizer.listen(source)

#             try:
#                 print("Recognizing...")
#                 text = recognizer.recognize_google(audio).lower().strip()
#                 print("You said: " + text)

#                 # Check if any valid category is mentioned in the text
#                 matched_categories = [cat for cat in valid_categories if cat in text]
#                 if matched_categories:
#                     category = matched_categories[0]
#                     print(f"Matched category: {category}")

#                     with ThreadPoolExecutor() as executor:
#                         fetch_task = executor.submit(fetch_news, url, category)
#                         stop_task = executor.submit(listen_for_stop)
#                         exit_task = executor.submit(listen_for_exit)

#                         # Wait for either stop or exit command
#                         while not stop_flag and not exit_flag:
#                             time.sleep(1)

#                         # If exit command is given, stop everything
#                         if exit_flag:
#                             break

#                     stop_flag = False  # Reset the stop_flag for the next round of news fetching
#                 else:
#                     print("Invalid category.")
#                     Speaker.Speak('Invalid category. Please try again.')

#             except sr.UnknownValueError:
#                 print("Google Speech Recognition could not understand the audio")
#             except sr.RequestError as e:
#                 print(f"Could not request results from Google Speech Recognition service; {e}")

# if __name__ == "__main__":
#     main()


#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>Using PROCESS<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

import speech_recognition as sr
import requests
import win32com.client
import time
import multiprocessing

recognizer = sr.Recognizer()
Speaker = win32com.client.Dispatch("SAPI.SpVoice")

def fetch_news(url, cat, stop_flag, exit_flag):
    try:
        r = requests.get(url)
        r.raise_for_status()
        data = r.json()["news"]

        titles = [d["title"] for d in data if "title" in d and d.get("language") == "en" and cat in d.get("category", [])]
        descriptions = [d["description"] for d in data if "description" in d and d.get("language") == "en" and cat in d.get("category", [])]
        published = [d["published"].split(" ")[0] for d in data if "published" in d and d.get("language") == "en" and cat in d.get("category", [])]
        urls = [d["url"] for d in data if "url" in d and d.get("language") == "en" and cat in d.get("category", [])]
        cate = [d["category"] for d in data if "category" in d and d.get("language") == "en" and cat in d.get("category", [])]

        for t, d, p, u, c in zip(titles, descriptions, published, urls, cate):
            if stop_flag.value or exit_flag.value:
                return
            print(f"Title:\n{t}\nDescription:\n{d}\nPublished:\n{p}\nurl:\n{u}\nCategory:\n{c}\n")
            Speaker.Speak(f"Title: {t}")
            if stop_flag.value or exit_flag.value:
                return
            Speaker.Speak(f"Description: {d}")
            if stop_flag.value or exit_flag.value:
                return
            Speaker.Speak(f"Published on: {p}")
            if stop_flag.value or exit_flag.value:
                return
            Speaker.Speak(f"For more details, visit the URL")
            if stop_flag.value or exit_flag.value:
                return
            while Speaker.Status.RunningState == 2:  # 2 indicates that the speaker is speaking
                time.sleep(1)
            time.sleep(3)  # Wait for 3 seconds before moving to the next news item

    except Exception as e:
        print(f"Error: {e}")

def listen_for_stop(stop_flag):
    while not stop_flag.value:
        with sr.Microphone() as source:
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source)
            try:
                text = recognizer.recognize_google(audio).lower().strip()
                if "stop" in text:
                    stop_flag.value = True
                    Speaker.Speak("Stopping the news")
                    print("Command taken... stopping the news")
                    return
            except sr.UnknownValueError:
                pass
            except sr.RequestError as e:
                print(f"Could not request results from Google Speech Recognition service; {e}")

def listen_for_exit(exit_flag):
    while not exit_flag.value:
        with sr.Microphone() as source:
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source)
            try:
                text = recognizer.recognize_google(audio).lower().strip()
                if "exit" in text:
                    exit_flag.value = True
                    Speaker.Speak("Exiting")
                    print("Thank you for listening to the news")
                    return
            except sr.UnknownValueError:
                pass
            except sr.RequestError as e:
                print(f"Could not request results from Google Speech Recognition service; {e}")

def main():
    url = 'https://api.currentsapi.services/v1/latest-news?apiKey=bxc0hg6IzVfeYWpmW9-OiclHRPk8uUOmPREivANKmYKnJmNc'
    print('General news, Sports news, Regional news, Programming news, Technology news, Academia news, Gadgets news, World news, Game news')
    valid_categories = ["general", "sports", "regional", "programming", "technology", "academia", "gadgets", "world", "game"]

    stop_flag = multiprocessing.Value('b', False)
    exit_flag = multiprocessing.Value('b', False)

    while True:
        with sr.Microphone() as source:
            print("Adjusting for ambient noise... Please wait.")
            recognizer.adjust_for_ambient_noise(source)
            print("Listening...")
            audio = recognizer.listen(source)

            try:
                print("Recognizing...")
                text = recognizer.recognize_google(audio).lower().strip()
                print("You said: " + text)

                # Check if any valid category is mentioned in the text
                matched_categories = [cat for cat in valid_categories if cat in text]
                if matched_categories:
                    category = matched_categories[0]
                    print(f"Matched category: {category}")

                    # Create processes
                    fetch_process = multiprocessing.Process(target=fetch_news, args=(url, category, stop_flag, exit_flag))
                    stop_process = multiprocessing.Process(target=listen_for_stop, args=(stop_flag,))
                    exit_process = multiprocessing.Process(target=listen_for_exit, args=(exit_flag,))

                    # Start processes
                    fetch_process.start()
                    stop_process.start()
                    exit_process.start()

                    # Wait for processes to finish
                    fetch_process.join()
                    stop_process.join()
                    exit_process.join()

                    # Reset the stop_flag for the next round of news fetching
                    stop_flag.value = False

                else:
                    print("Invalid category.")
                    Speaker.Speak('Invalid category. Please try again.')

            except sr.UnknownValueError:
                print("Google Speech Recognition could not understand the audio")
            except sr.RequestError as e:
                print(f"Could not request results from Google Speech Recognition service; {e}")

if __name__ == "__main__":
    main()
