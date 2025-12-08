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
    for key,val in goods_info.items():
        print('编号：{}，名称：{}，单价：{}' .format(key, val['name'], val['price']))
    print("-----------------------------------")
    n = input("请输入要购买的产品编号和数量，如 102 3：")
    return n


def get_cid_count(n):
    cid = int(n.split()[0])
    count = int(n.split()[1])
    return cid, count


def get_total_price(cid, count):
    # total_price = 0
    total_price = goods_info[cid]['price']*count
    return total_price


def main():
    #1.输出介绍信息
    n = print_intro()
    #2.获取编号和数量
    cid, count = get_cid_count(n)
    #3.计算出商品总价格
    total_price = get_total_price(cid, count)
    #4.支付

# 调用函数
main()