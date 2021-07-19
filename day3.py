import random
mycart = []
# 商品栏
shop = [
    ["电冰箱",3000],
    ["老干妈",13],
    ["啤酒",50],
    ["vivo x50",2700],
    ["Levono",6000],
]
prefer = [
         ["老干妈",0.7]*10,
         ["Levono",0.1]*20,
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
    chose = input("亲输入您想要的商品编号：") # "1"
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
                    mycart[len(mycart)-1][1] = shop[chose][1] * favour[1]
                    print("恭喜，成功添加购物车！您的余额还剩￥：",money)
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
for key ,value in  enumerate(mycart):
    print(key,value)
print("本次余额还剩：￥",money)
