import textwrap

raw_data = """
   Name:  Alice Smith  ;  Age: 25 ; City:  Beijing  ;  Score: 92.5
   Name:Bob Jones;Age:30;City: Shanghai;Score:88.0
   Name:  Charlie Brown  ;Age:  22;  City:Shenzhen ;Score:  95.5  
"""

first_prcessing = textwrap.dedent(raw_data)
lines = first_prcessing.strip().split("\n")
clean_text = []
for line in lines:
    line = {key.strip():value.strip() for key, value in (item.split(":") for item in line.split(";"))}
    clean_text.append(line)
print("[")
for line in clean_text:
    print(f"    {line}")
print("]")

for line in clean_text:
    line['Score'] = float(line['Score'])
    line['Age'] = int(line['Age'])
name_with_score = [(line['Name'], line['Score']) for line in clean_text]
name_with_score.sort(key=lambda x: float(x[1]), reverse=True)
print(f"最高分：{name_with_score[0][0]}({name_with_score[0][1]}分)")