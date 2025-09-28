def split_and_join(line):
    words = line.split(" ")
    return "-".join(words)

line = input()
result = split_and_join(line)
print(result)
