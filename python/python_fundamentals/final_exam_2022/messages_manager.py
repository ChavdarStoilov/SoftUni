capacity_of_messages = int(input())

command = input()
records = {}

while command != "Statistics":

    action = command.split("=")
    user_or_sender = action[1]

    if action[0] == "Add":
        if user_or_sender not in records.keys():
            records[user_or_sender] = {"sent": int(action[2]), "received": int(action[3])}

    elif action[0] == "Message":
        if user_or_sender in records.keys() and action[2] in records.keys():
            records[user_or_sender]["sent"] += 1
            records[action[2]]["received"] += 1

        if records[user_or_sender]["sent"] + records[user_or_sender]["received"] >= capacity_of_messages:
            records.pop(user_or_sender)
            print(f"{user_or_sender} reached the capacity!")
        elif records[action[2]]["sent"] + records[action[2]]["received"] >= capacity_of_messages:
            records.pop(action[2])
            print(f"{action[2]} reached the capacity!")

    elif action[0] == "Empty":
        if user_or_sender in records.keys():
            records.pop(user_or_sender)
        elif user_or_sender == "All":
            records.clear()

    command = input()

print(f"Users count: {len(records)}")

for person in records.items():
    user = person[0]
    messages = person[1]['sent'] + person[1]["received"]
    if messages != 0:
        print(f"{user} - {messages}")


# messages_cap = int(input())
# command = input()
#
# users = []
# send_and_received = []
# users_dict = {}
#
# while True:
#     commands = command.split('=')
#
#     if command == "Statistics":
#         break
#
#     if commands[0] == "Add":
#         if commands[0] not in users:
#             users.append(commands[1])
#             send = int(commands[2])
#             received = int(commands[3])
#             sum_send_received = send + received
#             send_and_received.append(sum_send_received)
#
#     if commands[0] == "Message":
#         if commands[1] in users and commands[2] in users:
#             count = 0
#             count2 = 0
#             for x in users:
#                 if commands[1] == x:
#                     send_and_received[count] += 1
#                     if send_and_received[count] >= messages_cap:
#                         send_and_received.pop(count)
#                         print(f"{users[count]} reached the capacity!")
#                         users.pop(count)
#                 else:
#                     count += 1
#             count = 0
#             for sec in users:
#                 if commands[2] == sec:
#                     send_and_received[count2] += 1
#                     if send_and_received[count2] >= messages_cap:
#                         send_and_received.pop(count2)
#                         print(f"{users[count2]} reached the capacity!")
#                         users.pop(count2)
#                 else:
#                     count2 += 1
#             count2 = 0
#
#     if commands[0] == "Empty":
#         if commands[1] == "All":
#             users.clear()
#             send_and_received.clear()
#         if commands[1] in users:
#             user_count = 0
#             for u in users:
#                 if commands[1] == u:
#                     users.pop(user_count)
#                     send_and_received.pop(user_count)
#                 else:
#                     user_count += 1
#     command = input()
#
# print(f"Users count: {len(users)}")
# for i, k in zip(users, send_and_received):
#     print(f"{i} - {k}")
