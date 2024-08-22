import random
import string

def generate_password(length=12):
    # 定义密码字符集：字母（大小写）、数字和特殊字符
    characters = string.ascii_letters + string.digits + string.punctuation
    # 随机选择字符构成密码
    password = ''.join(random.choice(characters) for i in range(length))
    return password

if __name__ == "__main__":
    # 获取用户输入的密码长度
    try:
        length = int(input("请输入密码长度（默认12位）："))
    except ValueError:
        print("无效输入，使用默认长度12。")
        length = 12
    
    # 生成并输出密码
    password = generate_password(length)
    print(f"生成的密码是：{password}")
