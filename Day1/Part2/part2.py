earlier_position = 50
position = 50
ans_count = 0
# with open('../TestDay1Input.txt', 'r') as f:
with open('../Day1Input.txt', 'r') as f:
    for line in f:
        Direction = line[0]
        Number = int(line[1:])
        print(f"direction : {Direction}, Number : {Number}")
        position = (position - Number)%100 if Direction == 'L' else (position + Number)%100
        ans_count += Number//100 
        if earlier_position != 0:
            if Direction == 'L':
                ans_count += 1 if (earlier_position - (Number%100) <= 0) else 0
            elif Direction == 'R':
                ans_count += 1 if (earlier_position + (Number%100) >= 100) else 0

        earlier_position = position


print(ans_count)




