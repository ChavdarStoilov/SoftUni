parentheses = input()

que = []
case = True

for ch in parentheses:

    if ch in "[{(":
        que.append(ch)
    elif not que:
        case = False
        break
    else:
        last = que.pop()
        if f'{last}{ch}' not in "[](){}}":
            case = False
            break

        else:
            case = True


if case and not que:
    print("YES")
else:
    print("NO")