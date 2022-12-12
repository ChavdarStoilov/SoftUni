# import math
# from collections import deque
#
# def operation(numbers, operator, result):
#     the_result = result
#
#     while numbers:
#
#         if result is None:
#             the_result = numbers.popleft()
#
#         if operator == '+':
#             the_result += numbers.popleft()
#
#         elif operator == '-':
#             the_result -= numbers.popleft()
#
#         elif operator == '*':
#             the_result *= numbers.popleft()
#
#         elif operator == '/':
#             the_result = math.floor(the_result / numbers.popleft())
#
#
#     return the_result
#
# def get_numbers(express, numbers, result):
#
#     while express:
#         num = express.popleft()
#
#         if num == '*' or num == '+' or num == '-' or num == '/':
#             if len(numbers) >= 1:
#                 result = operation(numbers, num, result)
#
#         else:
#             numbers.append(int(num))
#
#
#
#     return result
#
# expression = deque(input().split())
#
# temp_number = deque()
# temp_result = None
#
#
# print(get_numbers(expression, temp_number, temp_result))

from collections import deque
import math

expression = deque(input().split())
end_result = 0
result = deque()

while expression:
    num = expression.popleft()
    if num == '*' or num == '+' or num == '-' or num == '/':
        if len(result) >= 1:
            end_result = result.popleft()

            if num == '-':
                while result:
                    end_result = end_result - result.popleft()
                result.append(end_result)

            elif num == '+':
                while result:
                    end_result = end_result + result.popleft()
                result.append(end_result)

            elif num == '*':
                while result:
                    end_result = end_result * result.popleft()
                result.append(end_result)

            elif num == '/':
                while result:
                    end_result = math.floor(end_result / result.popleft())
                result.append(end_result)

    else:
        result.append(int(num))

print(''.join(str(i) for i in result))