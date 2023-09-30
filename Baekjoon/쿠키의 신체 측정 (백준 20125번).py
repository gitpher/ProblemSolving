N = int(input())

head_found = False
heart_location_y = 0
heart_location_x = 0
length_of_left_arm = 0
length_of_right_arm = 0
length_of_waist = 0
length_of_left_leg = 0
length_of_right_leg = 0

for i in range(N):
    row = input()
    for j in range(len(row)):
        if row[j] == '*':
            if not head_found:
                head_found = True
                heart_location_y = i + 2
                heart_location_x = j + 1
            elif i == heart_location_y - 1:
                if j < heart_location_x - 1:
                    length_of_left_arm += 1
                elif j > heart_location_x - 1:
                    length_of_right_arm += 1
            elif i > heart_location_y - 1:
                if j == heart_location_x - 1:
                    length_of_waist += 1
                elif j == heart_location_x - 2:
                    length_of_left_leg += 1
                elif j == heart_location_x:
                    length_of_right_leg += 1

print(heart_location_y, heart_location_x)
print(length_of_left_arm, length_of_right_arm, length_of_waist, length_of_left_leg, length_of_right_leg)
