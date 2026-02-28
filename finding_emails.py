with open('emails.txt', 'r') as file:
    emails=file.readlines()
    
print(emails)
for mail in emails:
    if "gmail" in mail:
        print(mail.rstrip())
    # if "outlook" in mail:
    #     print(mail.rstrip())
    # if "@" in mail:
    #     print(mail.rstrip())
        