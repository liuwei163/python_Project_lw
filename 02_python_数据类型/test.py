"""
goods_info = {
    101: {"name": "无尽之刃", "price": 3600},
    102: {"name": "饮血剑", "price": 3200},
    103: {"name": "暴风之剑", "price": 1300},
    104: {"name": "多兰剑", "price": 450},
}

# 打印所有的键值对
# print(goods_info.items())


def print_intro():
    print("欢迎来到武器商店！")
    print("-----------------------------------")
    for key, val in goods_info.items():
        print('编号：{}，名称：{}，单价：{}' .format(key, val['name'], val['price']))
    print("-----------------------------------")
    print("请按照以下操作完成交易。。。")


def git_user_input():
    while True:
        try:
            n = input("请输入要购买的产品编号和数量，（格式：编号 数量），或输入'q'退出")
            if n.lower() == 'q':
                return None, None
            return n


def get_cid_count(n):
    cid = int(n.split()[0])
    count = int(n.split()[1])
    return cid, count


def get_total_price(cid, count):
    total_price = 0
    total_price = goods_info[cid]['price'] * count
    return total_price


def pay(total_price):
    while True:
        money = float(input('总价为{}元，请输入金额：'.format(total_price)))
        if money >= total_price:
            print('支付成功，找回：{}元'.format(money-total_price))
            break
        else:
            print('金额不足,支付失败')


def main():
    # 1.输出介绍信息
    n = print_intro()
    # 2.获取编号和数量
    cid, count = get_cid_count(n)
    # 3.计算出商品总价格
    total_price = get_total_price(cid, count)
    print(total_price)
    # 4.支付
    pay(total_price)


# 调用函数
main()

"""

# 商品信息使用常量命名，便于维护
GOODS_INFO = {
    101: {"name": "无尽之刃", "price": 3600},
    102: {"name": "饮血剑", "price": 3200},
    103: {"name": "暴风之剑", "price": 1300},
    104: {"name": "多兰剑", "price": 450},
}


def print_intro():
    """打印商店介绍和商品列表"""
    print("欢迎来到武器商店！")
    print("请按照以下操作完成交易...")
    print("-----------------------------------")
    for key, val in GOODS_INFO.items():
        print(f'编号：{key}，名称：{val["name"]}，单价：{val["price"]}元')
    print("-----------------------------------")


def get_user_input():
    """获取用户输入，包含输入验证"""
    while True:
        try:
            n = input("请输入要购买的产品编号和数量（格式：编号 数量），或输入'q'退出：")
            if n.lower() == 'q':
                return None, None

            # 处理多余空格
            parts = n.strip().split()
            if len(parts) != 2:
                print("输入格式错误！请使用'编号 数量'的格式（例如：102 3）")
                continue

            cid = int(parts[0])
            count = int(parts[1])

            # 验证商品编号是否存在
            if cid not in GOODS_INFO:
                print(f"错误：商品编号 {cid} 不存在！")
                continue

            # 验证数量是否有效
            if count <= 0:
                print("错误：数量必须大于0！")
                continue

            return cid, count

        except ValueError:
            print("输入错误！请确保编号和数量都是数字")
        except Exception as e:
            print(f"发生错误：{e}")


def get_total_price(cid, count):
    """计算商品总价格"""
    return GOODS_INFO[cid]['price'] * count


def pay(total_price):
    """处理支付流程"""
    print(f"\n需要支付的总价为：{total_price}元")

    while True:
        try:
            money_input = input("请输入支付金额（输入'c'取消交易）：")

            if money_input.lower() == 'c':
                print("交易已取消")
                return False

            money = float(money_input)

            if money < 0:
                print("金额不能为负数！")
                continue

            if money < total_price:
                print(f'金额不足，还差{total_price - money:.2f}元')
                continue

            change = money - total_price
            print(f'支付成功！找零：{change:.2f}元')
            return True

        except ValueError:
            print("请输入有效的金额数字！")


def print_receipt(cid, count, total_price):
    """打印收据"""
    print("\n" + "=" * 30)
    print("交易成功！以下是您的收据：")
    print("=" * 30)
    print(f"商品：{GOODS_INFO[cid]['name']}")
    print(f"数量：{count}")
    print(f"单价：{GOODS_INFO[cid]['price']}元")
    print(f"总价：{total_price}元")
    print("=" * 30)
    print("感谢光临，欢迎下次再来！")


def main():
    """主程序"""
    while True:
        # 1. 输出介绍信息
        print_intro()

        # 2. 获取编号和数量
        cid, count = get_user_input()

        # 检查是否退出
        if cid is None:
            print("再见！")
            break

        # 3. 计算商品总价格
        total_price = get_total_price(cid, count)

        # 显示购买信息
        print(f"\n您选择了：{GOODS_INFO[cid]['name']} x {count}")
        print(f"小计：{total_price}元")

        # 4. 支付
        if pay(total_price):
            # 5. 打印收据
            print_receipt(cid, count, total_price)

        # 询问是否继续
        continue_shopping = input("\n是否继续购物？(y/n): ")
        if continue_shopping.lower() != 'y':
            print("谢谢惠顾，再见！")
            break
        print("\n" + "-" * 30 + "\n")


# 调用主函数
if __name__ == "__main__":
    main()
