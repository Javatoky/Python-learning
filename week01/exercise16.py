contacts = []

def add_contact(name:str, phone:str, email:str):
    contact = {"Name": name, "Phone": phone, "Email": email}
    contacts.append(contact)
    print(f"联系人 {name} 已添加")

def show_contacts():
    if not contacts:
        print("暂无联系人。")
        return
    print("╔════╦════════════════╦═══════════════╦════════════════════════╗")
    print("║   #║  姓名          ║          电话 ║         邮箱           ║")
    print("╠════╬════════════════╬═══════════════╬════════════════════════╣")
    for contact in contacts:
        print(f"║{contact['Name']:>4}║{contact['Phone']:>14}║{contact['Email']:>24}║")
    print("╚════╩════════════════╩═══════════════╩════════════════════════╝")

def get_email_domain() -> list:
    email_domain = {contact['Email'].split("@")[-1] for contact in contacts}
    return email_domain

def search_contact(key:str) -> list:
    result = [contact for contact in contacts if key in contact['Name']]
    return result
def main():
    test_contacts = [
        {"Name": "张三", "Phone": "13800138001", "Email": "zhangsan@example.com"},
        {"Name": "李四", "Phone": "13900139002", "Email": "lisi@gmail.com"},
        {"Name": "王五", "Phone": "13700137003", "Email": "wangwu@163.com"},
        {"Name": "赵六", "Phone": "13600136004", "Email": "zhaoliu@example.com"},
        {"Name": "李七", "Phone": "13500135005", "Email": "qianqi@example.com"}
    ]
    for contact in test_contacts:
        add_contact(contact['Name'], contact['Phone'], contact['Email'])
    show_contacts()
    result = search_contact("李")
    print("搜索'李'结果：")
    for contact in result:
        print(f"{'-':^4}{contact['Name']}（{contact['Phone']}）")
    print("邮箱域名统计：")
    email_domain = get_email_domain()
    print(f"{'':4}总共{len(email_domain)}个邮箱域名：{email_domain}")

main()