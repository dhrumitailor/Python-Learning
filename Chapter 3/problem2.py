letter = '''Dear [Recipient's Name],
I hope this letter finds you well. I wanted to take a moment to express my gratitude for your support and kindness. Your presence in my life has been a source of strength and inspiration, and I am truly thankful for everything you do.
I look forward to many more wonderful moments together. Thank you once again for being such an amazing person.
Sincerely,
[Your Name]'''
recipient_name = input("Enter the recipient's name: ")
sender_name = input("Enter your name: ")
personalized_letter = letter.replace("[Recipient's Name]", recipient_name).replace("[Your Name]",
sender_name)
print("\nHere is your personalized letter:\n")
print(personalized_letter)
