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
            ans_count+=1 

print(ans_count)




