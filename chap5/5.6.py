import random


national_values = {'富强', '民主', '文明', '和谐'}
social_values = {'自由', '平等', '公正', '法制'}
citizen_values = {'爱国', '敬业', '诚信', '友善'}
all_values = national_values | social_values | citizen_values
question_list = ['national', 'social', 'citizen', 'all']


def question(value_set: set):
    answer = set()
    times = 0

    while answer != value_set:
        user_input = input('请输入一项核心价值观的内容：')
        if user_input in value_set:
            print('答对了！请继续。\n你已经回答了以下内容：', end='')
            answer.add(user_input)
        else:
            print('答错了！请继续。\n你已经回答了以下内容：', end='')
        print(answer)
        times += 1
    print('恭喜你，全部回答正确。太棒了！\n这个问题你一共回答了%d次。' % times)


print("""
=================================================
===社会主义核心价值观问答程序，按'q'退出程序！===
================================================= 
""")
key = input('按Enter键选择答题：')
if key == 'q':
    exit()

random_choice = random.choice(question_list)
if random_choice == 'national':
    print('请回答国家层面的价值目标。')
    question(national_values)
elif random_choice == 'social':
    print('请回答社会层面的价值取向。')
    question(social_values)
elif random_choice == 'citizen':
    print('请回答公民个人层面的价值准则。')
    question(citizen_values)
else:
    print('请回答社会主义核心价值观全部12项内容。')
    question(all_values)



