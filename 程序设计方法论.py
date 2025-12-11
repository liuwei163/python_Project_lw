"""
自顶而下
    一个解决复杂问题行之有效的方法被称作自顶而下的设计方法，
其基本思想是以一个总问题开始，试图把它表达为很多小问题组成的解决方案。
再用同样的技术依次攻破每个小问题，最终问题变得非常小，以至于可以很容易解决。
然后只需把所有的碎片组合起来，就可以得到一个程序
#####################################################################
自底而上
    执行中等规模程序的最好方法是从结构图最底层开始，而不是从顶部开始，然后逐步上升。
或者说，先运行和测试每一个基本函数，再测试由基础函数组成的整体函数，这样有助于定位错误
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
    print("请按照以下操作完成交易。。。")
    print("-----------------------------------")
    for key, val in goods_info.items():
        print('编号：{}，名称：{}，单价：{}' .format(key, val['name'], val['price']))
    print("-----------------------------------")
    n = input("请输入要购买的产品编号和数量，如 102 3：")
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
