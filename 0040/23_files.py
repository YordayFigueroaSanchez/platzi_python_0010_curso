# file = open('0040/text.txt', 'r')
# print(file.read())
# print(file.readline())
# for line in file:
    # print(line)
# file.close()

with open('0040/text.txt', 'r') as file:
    for line in file:
        print(line)
