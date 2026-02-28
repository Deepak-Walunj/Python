import speech_recognition as sr
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
