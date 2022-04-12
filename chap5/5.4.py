import random


def randomphone():
    digit = ''
    for i in range(8):
        digit += str(random.randint(0, 9))
    return digit


def random10num(isp):
    for i in range(10):
        print(random.choice(isp) + randomphone(), end='\t')


telecom = ['133', '153', '180', '181', '189', '177']
mobile = ["134", "135", "136", "137", "138",
          "139", "150", "151", "152", "157",
          "158", "159", "182", "183", "184",
          "187", "188", "147", "178"]
unicom = ["130", "132", "155", "156", "185", "186", "145", "176", "179"]

ispid = input("""
1. 中国电信
2. 中国移动
3. 中国联通
请从以上运营商中选择一个：
""")


if ispid in ['1', '2', '3']:
    if ispid == '1':
        random10num(telecom)
    elif ispid == '2':
        random10num(mobile)
    elif ispid == '3':
        random10num(unicom)
else:
    print("没有选择运营商")
