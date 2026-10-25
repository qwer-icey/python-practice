num = input("请输入整数:").strip()
if num.lstrip("-").isdigit():
    print(f"{int(num)} is a great number")
else:
    print(f"{num}不是整数")
input("按回车键退出...")
    
