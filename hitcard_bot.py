import requests
import json


# 发出 POST 请求，返回字节行迭代器
def post_card():
    url = 'http://yun.ujs.edu.cn/xxhgl/yqsb/grmrsb?v=9374'
    response = requests.post(url, headers=headers, data=data)
    return response.iter_lines()


def check_success(iter_lines):
    for line in iter_lines:
        if b'Success' in line:
            return True
    return False


def send_group_msg(group_id: int, msg: str):
    url = 'http://127.0.0.1:5700/send_group_msg'
    bot_headers = {'Content-Type': 'application/json'}
    bot_data = {
        "group_id": group_id,
        "message": msg
    }
    response = requests.post(url, headers=bot_headers, data=json.dumps(bot_data))
    return response.json()


if __name__ == '__main__':
    headers = {
        'User-Agent': '',
        'Cookie': ''
    }

    data = {'ykt': '学号',
            'dwmc': '学院',
            'zy': '专业',
            'bj': '班级',
            'xm': '姓名',
            'nl': '届',
            'sjh': '手机号',
            'sfyxszd': '是',
            'sfid': '320000',
            'csid': '321100',
            'xqid': '321112',
            'xxdz': '住址',
            'jqdt': '近14天内未离开镇江',
            'dzsj_m': '',
            'dzsj_d': '',
            'czjtgj': '',
            'jtgjbc': '',
            'yxzt': '无',
            'mqzdyqdyjcs': '',
            'zdyq': '',
            'sfgtjzryfrks': '否',
            'xsfxbj': '未返校',
            'xwwd': '0',
            'swwd': '0',
            'qtyc': '',
            'bz': '',
            'jzymqk': '已接种北京生物国药疫苗',
            'ywcdyz': '是',
            'ywcdez': '是',
            'ywcdsz': '是',
            'wjzyy': '其他原因',
            'latitude': '',
            'longitude': '',
            'btn': ''
            }

    iter_response = post_card()
    if check_success(iter_response):
        print(send_group_msg(int('群号'), '[机器人发送]打卡成功'))
    else:
        print(send_group_msg(int('群号'), '[机器人发送]打卡失败'))

