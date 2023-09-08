import imaplib
import email
import re
from bs4 import BeautifulSoup
mail = imaplib.IMAP4_SSL('imap.gmail.com')  # Replace with your email provider's IMAP server
mail.login('tanishqagargdevi@gmail.com', 'eyostsyetyzevqmo')
mail.select('Inbox')  # You can change 'inbox' to the desired mailbox/folder
key = 'Subject'
value = 'visit'
search_criterion = f'SUBJECT "{value}"'
# Search for emails with specific subject
result, data = mail.search(None, search_criterion)
# result, data = mail.search(None, key, value)  #Search for emails with specific key and value
email_ids = data[0].split()  #IDs of all emails that we want to fetch 
import json
extracted_data_list = []

for email_id in email_ids:
    result, msg_data = mail.fetch(email_id, '(RFC822)')
    msg = email.message_from_bytes(msg_data[0][1])
    for part in msg.walk():
        if part.get_content_type() == "text/plain":
            email_body = part.get_payload(decode=True).decode()
            name_match = re.search(r'\*Name:\*\s*(\w+)', email_body)
            age_match = re.search(r'\*Age:\*\s*(\d+)', email_body)
            gender_match = re.search(r'\*Gender:\*\s*(\w+)', email_body)
            phone_match = re.search(r'\*Phone:\*\s*(\w+)', email_body)
            test_match = re.search( r'\*Labs:\*\s*([\s\S]*?)(?=\n\*Collection Date:|$)', email_body)
            collection_match = re.search(r'\*Collection Date:\*\s*(\d{4}-\d{2}-\d{2})', email_body)
            user_match = re.search(r'\*User\'s name:\*\s*(.*)', email_body)
            user_phone_match = re.search(r'\*User\'s phone:\*\s*(\w+)', email_body)
            mail_match = re.search(r'\*User\'s mail:\*\s*(.*)', email_body)
            source_match=re.search(r'\*Collection type:\*\s*(.*)',email_body)
            address_match=re.search(r'\*Address of Patient:\*\s*([\s\S]*?)(?=\n\*Package & Test Details:|\Z)',email_body)
            if name_match and age_match and gender_match and phone_match and test_match and collection_match and user_match and user_phone_match and mail_match and  mail_match and source_match and  address_match:
                name = name_match.group(1)
                age = age_match.group(1)
                gender = gender_match.group(1)
                phone = phone_match.group(1)
                test = test_match.group(1).strip()
                test_list=test.split("\n")     
                collection = collection_match.group(1)
                user = user_match.group(1)
                user_phone=user_phone_match.group(1)
                user_mail=mail_match.group(1)
                source_type=source_match.group(1)
                user_address=address_match.group(1).strip()
                extracted_data = {
                        "name": name,
                        "age": age,
                        "gender": gender,
                        "phone": phone,
                        "test": test_list,
                        "collection_date": collection,
                        "user": user,
                        "user_phone": user_phone,
                        "mail": user_mail,
                        "source_type": source_type,
                        "user_address": user_address
                    }
                extracted_data_list.append(extracted_data)
            else :
                print("some error occured")
with open('extracted_data.json', 'w') as json_file:
    json.dump(extracted_data_list, json_file)
print("Data saved to extracted_data.json")




