class Email:

    def __init__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = False


    def send(self):
        self.is_sent = True

    def get_info(self):
        return f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}"

emails = []

the_information = input().split()

while the_information[0] != "Stop":

    sender, receiver, content = [index for index in the_information]
    email = Email(sender, receiver, content)
    emails.append(email)
    the_information = input().split()

some_index = input().split(", ")

for idx in some_index:
    emails[int(idx)].send()

for the_mail in emails:
    print(the_mail.get_info())