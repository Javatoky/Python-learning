raw_records = [
    "  Alice, 25,  92.5, Beijing  ",
    "  Bob, 30, 78.0,  Shanghai",
    "  Charlie, 22, 95.5, Shenzhen  ",
    " Diana, 28, 88.0, Beijing",
    " Eve, 35, 72.0,   Guangzhou ",
]

def parse_record(line: str) -> dict:
    str_list = [word.strip() for word in line.strip().split(",")]
    person_info = {
        "name": str_list[0],
        "age": str_list[1],
        "score": str_list[2],
        "city": str_list[3]
    }
    return person_info

def filter_records(records: list[dict], **criteria) -> list[dict]:
    new_records = []
    for personal_info in records:
        if "min_score" in criteria:
            if float(personal_info.get('score')) < criteria["min_score"]:
                continue
        if 'city' in records:
            if personal_info.get('city') != criteria['city']:
                continue
        if 'min_age' in records:
            if int(personal_info.get('age')) < criteria['age']:
                continue
        new_records.append(personal_info)
    return new_records

def format_table(records: list[dict]) -> str: 
    table_lines = [f'{"Name":<10} {"Age":<5} {"Score":<8} {"City":<10}']
    for personal_info in records:
        info_str = f'{personal_info.get("name"):<10} {personal_info.get("age"):<5} {personal_info.get("score"):<8} {personal_info.get("city"):<10}'
        table_lines.append(info_str)
    return "\n".join(table_lines)

def main():
    first_records = []
    for line in raw_records:
        first_records.append(parse_record(line))
    second_records = filter_records(first_records, min_score = 80.0)
    third_records = filter_records(second_records, city = "Beijing")
    print(format_table(third_records))

main()

# 在filter_records中使用**kwargs，接受关键字参数，通过解包以字典的形式接受，而且数量不限
# 是为了灵活接纳多种关键字参数，让函数使用更加灵活，而非需要固定数目的参数