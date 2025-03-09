def send_messages(messages,sent_message):
    for message in messages:
        sent_message.append(message)
        print(message)

sent_messages = []
message =['Hey','how','are','you','doing']

send_messages(message[:],sent_messages)
print(message)
print(sent_messages)