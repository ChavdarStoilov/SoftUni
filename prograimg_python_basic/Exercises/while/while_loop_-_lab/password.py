user = str(input())
pwd = str(input())
data = str(input())

while data != pwd:
    data = str(input())

print(f"Welcome {user}!")