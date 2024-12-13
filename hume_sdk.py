import json

# Load the JSON data
with open('messages_voor_dentist ones.json', 'r') as file:
    data = json.load(file)

# Sort messages by time
sorted_messages = sorted(data, key=lambda x: x.get('receivedAt'))

# Create a summary of the conversation
summary = []
for message in sorted_messages:
    if message['type'] == 'user_message':
        content = message['message']['content']
        summary.append(f"User: {content}")
    elif message['type'] == 'assistant_message':
        content = message['message']['content']
        summary.append(f"Assistant: {content}")

# Write the summary to a .txt file
with open('conversation_summary.txt', 'w') as summary_file:
    for line in summary:
        summary_file.write(line + '\n')