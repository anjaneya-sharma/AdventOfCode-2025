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
        if position == 0:
            ans_count+=((Number)//100 + 1) if earlier_position != 0 else (Number//100)
        elif Direction == 'L':
            ans_count += ((Number)//100 + int((earlier_position - (Number%100)) < 0))
            if earlier_position == 0:
                ans_count -= 1
        elif Direction == 'R':
            ans_count += ((Number)//100 + int((earlier_position + (Number%100)) > 100))
        
        earlier_poisition = position



print(ans_count)




