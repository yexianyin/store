# author:jason
'''
    任务1：
        将导航系统与商城系统结合一起。
'''
import random


def aaa():
    mycart = []
    # # 商品栏
    shop = [
        ["电冰箱", 3000],
        ["老干妈", 13],
        ["啤酒", 50],
        ["vivo x50", 2700],
        ["Levono", 6000],
    ]
    prefer = [
        ["老干妈", 0.7] * 10,
        ["Levono", 0.1] * 20,
    ]

    favour = prefer[random.randint(0, len(prefer) - 1)]
    dis = False  # 是否使用优惠券

    while True:
        A = input("是否需要抽取优惠券（y/n）：")
        if A == "y":
            print("恭喜，您抽取了一张", favour[0], "的", favour[1], "折优惠券！")
            dis = True
            break
        elif A == "n":
            print("未抽取优惠券！")
            break
        else:
            print("输入非法！")

    money = input("请输入您的余额：")
    money = int(money)

    # 3.空的购物车
    mycart = []

    # 4.买东西

    while True:
        # 4.1 展示商品
        for key, value in enumerate(shop):
            print(key, value)

        # 4.2 请输入您想要的商品
        chose = input("亲输入您想要的商品编号：")  # "1"
        # 4.3
        if chose.isdigit():
            chose = int(chose)
            # 4.4 先判断是否存在该商品
            if chose > 6:
                print("您输入的商品不存在！别瞎弄！")
            else:
                # 4.5 判断您的余额是否足够
                if money < shop[chose][1]:
                    print("对不起，穷鬼，您的钱不够！请到其他超市买东西去！")
                else:
                    # 4.6 将商品添加到购物车 ，余额减去对应的钱
                    if dis and shop[chose][0] == favour[0]:
                        print(shop[chose][0], favour[0])
                        mycart.append(shop[chose])
                        money = money - shop[chose][1] * favour[1]
                        mycart[len(mycart) - 1][1] = shop[chose][1] * favour[1]
                        print("恭喜，成功添加购物车！您的余额还剩￥：", money)
                    else:
                        mycart.append(shop[chose])
                        money = money - shop[chose][1]
                        print("恭喜，成功添加购物车！您的余额还剩￥：", money)
        elif chose == "q" or chose == "Q":
            print("拜拜了，您嘞！欢迎下次光临！")
            break
        else:
            print("对不起，您输入有误，请重新输入！")

    # 打印购物小条
    print("以下是您的购物小条，请拿好：")
    for key, value in enumerate(mycart):
        print(key, value)
    print("本次余额还剩：￥", money)




data = {
    "北京":{
        "昌平":{
            "十三陵":["十三陵水库","沙河水库"],
            "高校":["北京邮电大学","中央戏剧学院","北京师范大学","华北电力大学","北京航空航天大学"],
            "天通苑":["海底捞","呷哺呷哺"]
        },
        "海淀":{
            "公主坟":["军事博物馆","中华世纪园"],
            "科普场馆":["中国科技馆","北京天文馆"],
            "高校":["北京大学","清华大学"],
            "景区":["北京植物园","香山公园","玉渊潭公园"]
        },
        "朝阳":{
            "龙城":["鸟化石国家地质公园","朝阳南北塔"],
            "双塔":["朝阳凌河公园","朝阳凤凰山"]
        },
        "延庆":{
            "龙庆峡":["龙庆峡景区"]
        }
    }
}

# 打印城市
def print_place(choice):
    for i in choice:
        print(i)

# 攻略
for i in data:
    print(i)


while True:
    city1 = input("请输入您要去的城市：")
    if city1 in data:
        print_place(data[city1])
        city2 = input("亲输入二级城市：")
        if city2 in data[city1]:
            print_place(data[city1][city2])
            city3  = input("亲输入三级地区：")
            if city3 in data[city1][city2]:
                print_place(data[city1][city2][city3])
                # 商城系统
                aaa()
                break
        else:
            print("当前二级城市不存在，别瞎弄！")
    elif city1 == 'q' or city1 == "Q":
        print("------------------欢迎下次光临Jason旅行社！------------------")
        break
    else:
        print("当前城市不存在，别瞎弄！")
