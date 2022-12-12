class Time:
    max_hours = 23
    max_minutes = 59
    max_seconds = 59

    def __init__(self, hours: int, minutes: int, seconds: int):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def set_time(self, hours: int, minutes: int, seconds: int):

        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def get_time(self):

        return f'{self.hours:02d}:{self.minutes:02d}:{self.seconds:02d}'

    def next_second(self):

        self.seconds += 1

        if self.seconds > self.max_seconds:
            self.seconds = 0
            self.minutes += 1


        if self.minutes > self.max_minutes:
            self.minutes = 0
            self.hours += 1


        if self.hours > self.max_hours:
            self.hours = 0


        return self.get_time()


time = Time(9, 30, 59)
print(time.next_second())

time = Time(10, 59, 59)
print(time.next_second())

time = Time(16, 35, 54)
print(time.next_second())

time = Time(1, 2, 3)
time.set_time(3, 2, 1)
print(time.next_second())

time = Time(1, 20, 30)
print(time.get_time())


time = Time(0, 0, 0)
print(time.next_second())


#
# class Time:
#     max_hours = 23
#     max_minutes = 59
#     max_seconds = 59
#
#     def __init__(self, hours, minutes, seconds):
#         self.hours = hours
#         self.minutes = minutes
#         self.seconds = seconds
#
#     def set_time(self, hours, minutes, seconds):
#         self.hours = hours
#         self.minutes = minutes
#         self.seconds = seconds
#
#     def get_time(self):
#         if self.hours < 10 or self.minutes < 10 or self.hours < 10:
#             return f"{self.hours:02d}:{self.minutes:02d}:{self.seconds:02d}"
#
#     def next_second(self):
#         self.seconds += 1
#         if self.seconds > Time.max_seconds:
#             self.seconds = self.seconds % 60
#             self.minutes += 1
#         if self.minutes > Time.max_minutes:
#             self.minutes = self.minutes % 60
#             self.hours += 1
#         if self.hours > Time.max_hours:
#             self.hours = self.hours // 60
#         return self.get_time()

#
# time = Time(9, 30, 59)
# print(time.next_second())
#
# time = Time(10, 59, 59)
# print(time.next_second())

# time = Time(16, 35, 54)
# print(time.next_second())

# time = Time(1, 2, 3)
# time.set_time(3, 2, 1)
# print(time.next_second())
#
# time = Time(1, 20, 30)
# print(time.get_time())
#
#
# time = Time(0, 0, 0)
# print(time.next_second())