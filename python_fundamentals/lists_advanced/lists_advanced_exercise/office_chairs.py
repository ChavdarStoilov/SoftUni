representing = int(input())

have_enough = False
current_room = 0
free_chairs = 0

for rooms in range(representing):
    chairs_and_visitors = input().split()
    current_room += 1


    if len(chairs_and_visitors[0]) >= int(chairs_and_visitors[1]):

        free_chairs += len(chairs_and_visitors[0]) - int(chairs_and_visitors[1])

    elif len(chairs_and_visitors[1]) < int(chairs_and_visitors[1]):
        need_more = int(chairs_and_visitors[1]) - int(len(chairs_and_visitors[0]))
        print(f"{need_more} more chairs needed in room {current_room}")
        free_chairs -= need_more

if free_chairs >= 0:
    print(f"Game On, {free_chairs} free chairs left")