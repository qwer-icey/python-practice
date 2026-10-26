import random
num = random.randint(1, 10)
while True:
    play_num = input("请输入10以内的整数:").strip()
    if play_num.lstrip("-").isdigit() and int(play_num) == num:
        print(f"{int(play_num)} is the true number")
        break
    else:
        print(f"{play_num}错了，正确答案是{num}")
        break
input("按回车键退出...")
