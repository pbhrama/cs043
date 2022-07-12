file = open("world.txt")
lang_list = []
key = "Hindi"
for line in file:
    line = line.strip()
    lang_list.append(line)
file.close()

i = 0
while i < len(lang_list) and lang_list[i] != key:
    i += 1
if i < len(lang_list):
    print(key + " was found at index " + str(i))
else:
    print("Could not find in language list")


def insertion(lst):
    for key_position in range(1, len(lst)):
        key_value = lst[key_position]
        scan_position = key_position - 1

        while (scan_position >= 0) and (lst[scan_position] > key_value):
            lst[scan_position + 1] = lst[scan_position]
            scan_position -= 1

        lst[scan_position + 1] = key_value


insertion(lang_list)
print()
print(lang_list)

check_list = lang_list
check_list.sort()
check = 0
for i in range(len(lang_list)):
    if check_list[i] == lang_list[i]:
        check += 1
    if check == len(lang_list) and check == len(check_list):
        print("The insertion sort works!")
