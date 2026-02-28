from flask import Flask, render_template, request, jsonify
import imaplib
import email
from email.header import decode_header
import re

app = Flask(__name__)

EMAIL_REGEX = r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+'

def extract_emails(text):
    return re.findall(EMAIL_REGEX, text)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/fetch_emails', methods=['POST'])
def fetch_emails():
    email_address = request.form.get('email')
    password = request.form.get('password')
    email_data = []

    try:
        mail = imaplib.IMAP4_SSL("imap.gmail.com")
        mail.login(email_address, password)
        mail.select("inbox")
        status, messages = mail.search(None, "ALL")

        if status != "OK":
            return jsonify({"error": "Failed to retrieve emails"}), 500

        email_ids = messages[0].split()
        for i in range(0, len(email_ids), 100):
            batch = email_ids[i:i+100]
            fetch_range = f"{batch[0].decode()}:{batch[-1].decode()}"
            status, msg_data = mail.fetch(fetch_range, "(BODY.PEEK[HEADER.FIELDS (From Date Subject)])")

            if status != "OK":
                continue

            for response_part in msg_data:
                if isinstance(response_part, tuple):
                    msg = email.message_from_bytes(response_part[1])
                    from_ = msg["From"]
                    date_ = msg["Date"]
                    subject_ = msg["Subject"]
                    decoded_from, encoding = decode_header(from_)[0]
                    decoded_from = decoded_from.decode(encoding or 'utf-8', errors='replace') if isinstance(decoded_from, bytes) else decoded_from
                    decoded_subject, encoding = decode_header(subject_)[0]
                    decoded_subject = decoded_subject.decode(encoding or 'utf-8', errors='replace') if isinstance(decoded_subject, bytes) else decoded_subject
                    email_data.append({
                        "email": extract_emails(decoded_from),
                        "date": date_,
                        "subject": decoded_subject
                    })
        mail.logout()
    except Exception as e:
        return jsonify({"error": str(e)}), 500

    return jsonify(email_data)

@app.route('/unique_emails', methods=['POST'])
def unique_emails():
    email_address = request.form.get('email')
    password = request.form.get('password')
    unique_mails = set()

    try:
        mail = imaplib.IMAP4_SSL("imap.gmail.com")
        mail.login(email_address, password)
        mail.select("inbox")
        status, messages = mail.search(None, "ALL")

        if status != "OK":
            return jsonify({"error": "Failed to retrieve emails"}), 500

        email_ids = messages[0].split()
        for i in range(0, len(email_ids), 100):
            batch = email_ids[i:i+100]
            fetch_range = f"{batch[0].decode()}:{batch[-1].decode()}"
            status, msg_data = mail.fetch(fetch_range, "(BODY.PEEK[HEADER.FIELDS (From)])")

            if status != "OK":
                continue

            for response_part in msg_data:
                if isinstance(response_part, tuple):
                    msg = email.message_from_bytes(response_part[1])
                    from_ = msg["From"]
                    decoded_from, encoding = decode_header(from_)[0]
                    decoded_from = decoded_from.decode(encoding or 'utf-8', errors='replace') if isinstance(decoded_from, bytes) else decoded_from
                    unique_mails.update(extract_emails(decoded_from))
        mail.logout()
    except Exception as e:
        return jsonify({"error": str(e)}), 500

    return jsonify(list(unique_mails))

if __name__ == '__main__':
    app.run(debug=True)
