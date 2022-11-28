some_file_path = input().split("\\")

file_and_extension = some_file_path[-1].split(".")

print(f"File name: {file_and_extension[0]}\n"
      f"File extension: {file_and_extension[-1]}")