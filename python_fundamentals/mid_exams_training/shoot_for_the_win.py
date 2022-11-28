def targets(target):
    command = input()
    count_shooting = 0

    while command != "End":
        index_shoot = int(command)

        if index_shoot >= len(target):
            command = input()
            continue

        if target[index_shoot] in target and target[index_shoot] != -1:
            count_shooting += 1
            shoot_target = target[index_shoot]
            for num in range(len(target)):
                if shoot_target < target[num] != - 1:
                    target[num] -= shoot_target
                elif shoot_target >= target[num] != -1:
                    target[num] += shoot_target

            target[index_shoot] = -1

        command = input()

    end_result = [str(number) for number in target]
    return f"Shot targets: {count_shooting} -> {' '.join(end_result)}"

targets_for_shooting = input().split()
integers_targets = list(map(int, targets_for_shooting))
print(targets(integers_targets))
