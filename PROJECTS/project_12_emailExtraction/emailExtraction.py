# import imaplib as im
# import email
# from email.header import decode_header
# import re

# # Regular expression to match email addresses
# email_regex = r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+'

# def extract_emails(text):
#     """Extract email addresses from a given text using regex."""
#     return re.findall(email_regex, text)

# def print_mail_contents(email_list):
#     for email_data in email_list:
#         print(f"Extracted Emails: {', '.join(email_data['email'])}")
#         print(f"Date: {email_data['date']}")
#         print(f"Subject: {email_data['subject']}\n")

# def you_received_mails_till_now(extracted_emails,unique_mails):
#     unique_mails.update(extracted_emails["email"])
#     print('Mails received so far:',unique_mails)

# unique_mails=set()
# email_data=[]
# # Connect to the IMAP server and log in
# mail = im.IMAP4_SSL("imap.gmail.com")
# user_mail=input("User please enter your mail ")
# user_password=input('Enter your password / Enter your app code ')
# mail.login("23sahil2004@gmail.com", "iwdm tltl mjhz jzea")
# #23sahil2004@gmail.com,iwdm tltl mjhz jzea
# # Select the inbox
# mail.select("inbox")

# # Search for all emails
# status, messages = mail.search(None, "ALL")

# # Get the list of email IDs
# ids = messages[0].split()

# # Loop through each email ID
# for id in ids:
#     status, msg_data = mail.fetch(id, "(RFC822)")
    
#     for response_part in msg_data:
#         if isinstance(response_part, tuple):
#             # Parse the email message
#             msg = email.message_from_bytes(response_part[1])
            
#             # Get the 'From', 'Date', and 'Subject' fields and decode them
#             from_ = msg["From"]
#             date_ = msg["Date"]
#             subject_ = msg["Subject"]
            
#             decoded_from, encoding = decode_header(from_)[0]
#             decoded_date, encoding = decode_header(date_)[0]
#             decoded_subject, encoding = decode_header(subject_)[0]
            
#             if isinstance(decoded_from, bytes):
#                 decoded_from = decoded_from.decode(encoding if encoding else 'utf-8')
#             if isinstance(decoded_date, bytes):
#                 decoded_date = decoded_date.decode(encoding if encoding else 'utf-8')
#             if isinstance(decoded_subject, bytes):
#                 decoded_subject = decoded_subject.decode(encoding if encoding else 'utf-8')
            
#             # Extract emails from the 'From' field
#             extracted_emails = {
#                 "email": extract_emails(decoded_from),
#                 "date": decoded_date,
#                 "subject": decoded_subject
#             }
            
#             # Check if the email is multipart
#             if msg.is_multipart():
#                 for part in msg.walk():
#                     # Look for plain text or HTML parts
#                     if part.get_content_type() in ["text/plain", "text/html"]:
#                         try:
#                             # Get the email body
#                             body = part.get_payload(decode=True).decode()
#                             # Extract emails from the body
#                             extracted_emails["email"] += extract_emails(body)
#                         except Exception as e:
#                             print("Error decoding body:", e)
#             else:
#                 # For non-multipart emails, just decode the payload
#                 try:
#                     body = msg.get_payload(decode=True).decode()
#                     extracted_emails["email"] += extract_emails(body)
#                 except Exception as e:
#                     print("Error decoding body:", e)
            
#             email_data.append(extracted_emails)
#             # you_received_mails_till_now(extracted_emails, unique_mails)
    
# while True:
#     try:
#         ch=int(input("Choose operation:\n1)Print entire mail account details\n2)unique mails\n3)Exit\n"))
#         if ch in [1,2,3]:
#             if ch==1:
#                 print_mail_contents(email_data)
#                 continue
#             elif ch==2:
#                 you_received_mails_till_now(extracted_emails, unique_mails)
#                 continue
#             elif ch==3:
#                 mail.logout()
#                 exit()
#         else:
#             print('Input between 1-3')
#             continue
#     except (NameError,ValueError) as e:
#         print(e)

# # Close the connection
# mail.logout()

import imaplib
import email
from email.header import decode_header
import re
import logging
import sys

# Configure logging for debugging and error reporting
logging.basicConfig(filename='email_extraction.log', level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

EMAIL_REGEX = r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+'

def extract_emails(text):
    """Extract email addresses from a given text using regex."""
    return re.findall(EMAIL_REGEX, text)

def print_mail_contents(email_list):
    """Print all emails with date and subject from the email list."""
    if not email_list:
        logging.info("No emails to print.")
        print("No emails to print.")
        return
    for email_data in email_list:
        emails = [e for e in email_data["email"] if isinstance(e, str)]
        if emails:
            print(f"Extracted Emails: {', '.join(emails)}")
        print(f"Date: {email_data.get('date', 'N/A')}")
        print(f"Subject: {email_data.get('subject', 'N/A')}\n")

def you_received_mails_till_now(unique_mails):
    """Print unique email addresses received so far."""
    if not unique_mails:
        logging.info("No unique emails to print.")
        print("No unique emails to print.")
    else:
        print(f"Unique Emails Received So Far: {', '.join(unique_mails)}")

def main():
    """Main function to run the email extraction process."""
    unique_mails = set()
    email_data = []

    try:
        # Connect to IMAP server
        mail = imaplib.IMAP4_SSL("imap.gmail.com")
        user_email = input("Enter your email: ")
        user_password = input("Enter your password / app code: ")

        # Log in with user input
        mail.login(user_email, user_password)
        logging.info(f"Logged in as {user_email}")

        mail.select("inbox")

        # Search for all emails in the inbox
        status, messages = mail.search(None, "ALL")
        if status != "OK":
            logging.error("Failed to retrieve email messages.")
            print("Error: Unable to retrieve messages.")
            return [], set()
        # print("success")
        email_ids = messages[0].split()
        # print(email_ids)
        logging.infoemail_ids = messages[0].split()[-10]
        # print(email_ids)
        logging.info(f"Found {len(email_ids)} emails in the inbox.")
        # if len(email_ids) > 100:
        #     email_ids = email_ids[-100:]
        # else:
        #     email_ids = email_ids
        print(f"Found {len(email_ids)} emails in the inbox.")
        # Fetch and process emails
        # for id in email_ids:
        #     status, msg_data = mail.fetch(id, "(BODY.PEEK[HEADER.FIELDS (From Date Subject)])")
        for i in range(0,len(email_ids),100):
            batch=email_ids[i:i+100]
            # print(batch)
            fetch_range = f"{batch[0].decode()}:{batch[-1].decode()}"
            # print(fetch_range)
            status, msg_data = mail.fetch(fetch_range, "(BODY.PEEK[HEADER.FIELDS (From Date Subject)])")
        
            if status != "OK":
                logging.error(f"Failed to fetch email with ID {id}.")
                continue
            # print("Status is ok")
            for response_part in msg_data:
                if isinstance(response_part, tuple):
                    # Parse the email message
                    msg = email.message_from_bytes(response_part[1])

                    # Get the 'From', 'Date', and 'Subject' fields and decode them
                    from_ = msg["From"]
                    date_ = msg["Date"]
                    subject_ = msg["Subject"]

                    decoded_from, encoding = decode_header(from_)[0]
                    if isinstance(decoded_from, bytes):
                        decoded_from = decoded_from.decode(encoding or 'utf-8', errors='replace')

                    decoded_subject, encoding = decode_header(subject_)[0]
                    if isinstance(decoded_subject, bytes):
                        decoded_subject = decoded_subject.decode(encoding or 'utf-8', errors='replace')

                    decoded_date = date_  # No need to decode date if it's plain text

                    # Extract emails from the 'From' field
                    extracted_emails = {
                        "email": extract_emails(decoded_from),
                        "date": decoded_date,
                        "subject": decoded_subject
                    }

                    # Check if the email is multipart
                    # if msg.is_multipart():
                    #     for part in msg.walk():
                    #         if part.get_content_type() in ["text/plain", "text/html"]:
                    #             try:
                    #                 body = part.get_payload(decode=True)
                    #                 if isinstance(body, bytes):
                    #                     body = body.decode('utf-8', errors='replace')
                    #                 extracted_emails["email"] += extract_emails(body)
                    #             except Exception as e:
                    #                 logging.error(f"Error decoding body: {e}")
                    # else:
                    #     try:
                    #         body = msg.get_payload(decode=True)
                    #         if isinstance(body, bytes):
                    #             body = body.decode('utf-8', errors='replace')
                    #         extracted_emails["email"] += extract_emails(body)
                    #     except Exception as e:
                    #         logging.error(f"Error decoding body: {e}")

                    # Append extracted email and update unique emails
                    email_data.append(extracted_emails)
                    unique_mails.update(extracted_emails["email"])
        # print("Overall status is ok")
    except imaplib.IMAP4.error as e:
        logging.error(f"IMAP error: {e}")
        print(f"IMAP error: {e}")
        sys.exit(1)
    except Exception as e:
        logging.error(f"Unexpected error: {e}")
        print(f"Unexpected error: {e}")
        sys.exit(1)
    finally:
        # Ensure logout
        try:
            if 'mail' in locals():
                mail.logout()
        except Exception as e:
            logging.error(f"Error logging out: {e}")

    # User input for actions
    while True:
        try:
            choice = int(input("Choose operation:\n1) Print all email details\n2) Show unique emails\n3) Exit\n"))
            if choice == 1:
                logging.info("User printed all his mails")
                print_mail_contents(email_data)
            elif choice == 2:
                logging.info("User checked all his unique mails")
                you_received_mails_till_now(unique_mails)
            elif choice == 3:
                logging.info("User exited the application.")
                break
            else:
                print("Input must be between 1 and 3.")
        except ValueError as e:
            logging.error(f"Invalid input: {e}")
            print("Invalid input. Please enter a number between 1 and 3.")
        except Exception as e:
            logging.error(f"Unexpected error: {e}")
            print(f"Unexpected error: {e}")

if __name__ == "__main__":
    main()
