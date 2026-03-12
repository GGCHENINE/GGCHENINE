#1
from itertools import count
from unittest import result


def exercise1():
    print("Hello, World!")


#2
def exercise2():
    a = 10
    b = 20
    print("a+b=", a + b)


#3
def exercise3():
    score = 80
    if score >= 90:
        print("及格")
    else:
        print("不及格")


#4
def exercise4():
    score = input("请输入成绩:")
    score = int(score)
    if score >= 90:
        print("优秀")
    elif score >= 80:
        print("良好")
    elif score >= 60:
        print("及格")
    else:
        print("不及格")


#5
def exercise5():
    score1 = int(input("请输入语文成绩:"))
    score2 = int(input("请输入数学成绩:"))

    if score1 >= 60 and score2 >= 60:
        print("语文及格，数学及格")
    elif score1 >= 60 and score2 < 60:
        print("语文及格，数学不及格")
    elif score1 < 60 and score2 >= 60:
        print("语文不及格，数学及格")
    else:
        print("语文不及格，数学不及格")

    total = score1 + score2
    average = total / 2
    print("总分", total)
    print("平均分", average)

#6
def exercise6():
    spend = [50,80,120,30,0,200,60]
    total = 0
    for cost in spend:
        total = total + cost
    print("一周总消费:",total)
    if total > 500:
        print("本周消费偏高")
    else:
        print("本周消费正常")
    avg = total / 7
    print("一周平均消费:",avg)

#7
def exercise7():
    scores = [88, 92, 75, 63, 99, 81]
    max_score = scores[0]
    min_score = scores[0]
    total = 0
    for score in scores:
        if score > max_score:
            max_score = score
        if score < min_score:
            min_score = score
        total = total + score
        avg = total / len(scores)
    print("最高分:",max_score)
    print("最低分:",min_score)
    print("总分:",total)
    print("平均分:",avg)

#8
def exercise8():
    steps = [3200, 8100, 5200, 0, 4500, 12000, 6800]
    max_steps = steps[0]
    min_steps = steps[0]
    total = 0
    for step in steps:
        if step > max_steps:
            max_steps = step
        if step < min_steps:
            min_steps = step
        total = total + step
        avg = total / len(steps)
    print("最多步数:",max_steps)
    print("最少步数:",min_steps)
    print("总步数:",total)
    print("平均步数:",avg)


#9
def exercise9():
    scores = [88, 45, 62, 90, 58, 73, 0, 100]
    pass_count = 0
    fail_count = 0
    for score in scores:
        if score >= 60:
            pass_count = pass_count + 1
        else:
            fail_count = fail_count + 1

    print("及格人数：",pass_count)
    print("不及格人数:",fail_count)

#10风控入门——交易规则打分与拦截
# def exercise10():
    amounts = [12, 880, 55, 3000, 120, 499, 500, 501, 0, -20, 9999]
    risk = 0
    for amount in amounts:
        if amount <= 0:
            risk = risk + 100
        elif amount > 5000:
            risk = risk + 60
        elif 500< amount <= 5000:
            risk = risk + 30
        # elif amount = 499 or 500 or 501:
            risk = risk + 20 
        elif amount%2:
            risk = risk + 5
    if risk >= 60:
        print("pass")
#10正确版本
# def exercise10():
    amounts = [12, 880, 55, 3000, 120, 499, 500, 501, 0, -20, 9999]

    pass_count = 0
    block_count = 0
    total_risk = 0
    max_risk = 0

    for amt in amounts:
        risk = 0

        # A: 异常金额（叠加）
        if amt <= 0:
            risk = risk + 100

        # B/C: 金额区间（互斥）
        if amt > 5000:
            risk = risk + 60
        elif 500 < amt <= 5000:
            risk = risk + 30

        # D: 卡边金额（叠加）
        if amt == 499 or amt == 500 or amt == 501:
            risk = risk + 20

        # E: 偶数（叠加）
        if amt % 2 == 0:
            risk = risk + 5

        if risk >= 60:
            result = "BLOCK"
            block_count = block_count + 1
        else:
            result = "PASS"
            pass_count = pass_count + 1

        print("amt=" + str(amt), "risk=" + str(risk), result)

        total_risk = total_risk + risk
        if risk > max_risk:
            max_risk = risk

    avg_risk = round(total_risk / len(amounts), 2)
    print("PASS=" + str(pass_count))
    print("BLOCK=" + str(block_count))
    print("max_risk=" + str(max_risk))
    print("avg_risk=" + str(avg_risk))

#10修正版
def exercise10():
    amounts = [12, 880, 55, 3000, 120, 499, 500, 501, 0, -20, 9999]

    pass_count = 0
    block_count = 0
    max_risk = 0
    total_risk = 0

    for amt in amounts:
        risk = 0

        if amt <= 0:
            risk = risk + 100

        if amt > 5000:
            risk = risk +60

        elif 500 < amt <= 5000:
            risk = risk +30
        
        if amt in (499,501,500):
            risk = risk + 20

        if amt %2 == 0:
            risk = risk + 5
        
        if risk >= 60:
            result = "BLOCK"
            block_count = block_count + 1
        else: 
            result = "PASS"
            pass_count = pass_count + 1

        print("amt=" + str(amt), "risk=" + str(risk), result) 
        total_risk += risk
    avg_risk = round(total_risk / len(amounts),2)

    if risk > max_risk:
        max_risk = risk

    print("passcount=",pass_count)
    print("blockcount=",block_count)
    print("maxrisk=",max_risk)
    print("averagerisk=",avg_risk)

#11风控常用特征——连续失败次数（streak）与最长连续失败
# def exercise11():
    events = ["PASS","PASS","BLOCK","BLOCK","BLOCK","PASS","BLOCK","PASS","PASS","BLOCK","BLOCK"]

    streak = 0
    PASS = 0 
    BLOCK = 0 
    max_block_streak = 0 

    for event in events:
        if event == "BLOCK":
            streak += 1
            BLOCK = BLOCK + 1

            if streak >= max_block_streak:
                max_block_streak = streak
        else:
            streak = 0
            PASS = PASS + 1

    print("max_block_streak=" + str(max_block_streak))
    print("PASS=" + str(PASS))
    print("BLOCK=" + str(BLOCK))

#11修正
def exercise11():
    events = ["PASS","PASS","BLOCK","BLOCK","BLOCK","PASS","BLOCK","PASS","PASS","BLOCK","BLOCK"]

    streak = 0
    max_block_streak = 0
    block_segments = 0
    pass_count = 0
    block_count = 0

    for i, event in enumerate(events):
        if event == "BLOCK":
            block_count += 1
            streak += 1

            # 段数：当前是 BLOCK，且前一个不是 BLOCK（或 i==0）
            if i == 0 or events[i - 1] != "BLOCK":
                block_segments += 1

            if streak > max_block_streak:
                max_block_streak = streak
        else:
            pass_count += 1
            streak = 0

        print("i=" + str(i), "event=" + str(event), "streak=" + str(streak))

    print("PASS=" + str(pass_count))
    print("BLOCK=" + str(block_count))
    print("block_segments=" + str(block_segments))
    print("max_block_streak=" + str(max_block_streak))

# 12逻辑练习
def exercise12():
    words = [10, 15, 0, 20, 25, 30, 5, 5, 40]
    day_with_words = 0
    day_without_words = 0
    max_words = 0 
    avg_words = 0
    totalwords = 0

    for word in words:
        if word >0:
            day_with_words += 1
            totalwords += word
            if word > max_words:
                max_words = word
        else:
            day_without_words += 1

    avg_words = totalwords / len(words)

    print("背单词天数="+str(day_with_words))
    print("没背单词天数="+str(day_without_words))
    print("最多一天背单词"+str(max_words))
    print("平均每天背"+str(round(avg_words,2)))


# 13近7天消费总额 & 超阈值天数
def exercise13():
    amounts = [120, 0, 300, 80, 500, 1000, 30, 60, 700, 0, 50, 400]
    total_amount = 0
    high_days = 0
    max_amount = 0
    avg_amount = 0

    for amt in amounts:
        total_amount += amt
        if amt >= 500:
            high_days += 1
        if amt > max_amount:
                max_amount = amt
    avg_amount = total_amount / len(amounts)

    print("总金额=" + str(total_amount))
    print("高消费天数=" + str(high_days))
    print("最大单日消费=" + str(max_amount))
    print("平均每天消费=" + str(round(avg_amount,2)))


# 14 简单“黑名单 + 大额”风控规则（引入字典）
# 第一次尝试
# def exercise14():
    transactions = [
    {"user_id": "u1", "amount": 100},
    {"user_id": "u2", "amount": 800},
    {"user_id": "u3", "amount": 5000},
    {"user_id": "u1", "amount": 2000},
    {"user_id": "u4", "amount": 50},
    {"user_id": "u2", "amount": 1200},
]
    blacklist = ["u2", "u5"]
    user_id = {}
    amount = 0
    tag = {}
    x = 0
    x1 = 0
    x2 = 0

    for user_id in transactions:
        if user_id in blacklist:
            result = "BLACKLIST"
            x2 = x2 + 1
        
        if amount >= 2000:
            tag = "HIGH_AMOUNT"
            x = x + 1
        else:
            tag = "NORMAL"
            x1 = x1 + 1
    
    print("user=" + str(user_id),"amount=" + str(amount),"tag:" + str(tag))
    print("BLACKLIST=" + str(x2))
    print("HIGH_AMOUNT=" + str(x))
    print("NORMAL=" + str(x1))

# 14 修正
def exercise14():
    transactions = [
    {"user_id": "u1", "amount": 100},
    {"user_id": "u2", "amount": 800},
    {"user_id": "u3", "amount": 5000},
    {"user_id": "u1", "amount": 2000},
    {"user_id": "u4", "amount": 50},
    {"user_id": "u2", "amount": 1200},
    ]
    blacklist = ["u2", "u5"]

    black_list = 0
    high_amount = 0
    normal_amount = 0

    for record in transactions:
        uid = record["user_id"]
        amt = record["amount"]

        if uid in blacklist:
            tag = "BLACKLIST"
            black_list = black_list + 1
        elif amt >= 2000:
                tag = "HIGH_AMOUNT"
                high_amount = high_amount + 1
        else:
            tag = "NORMAL"
            normal_amount = normal_amount + 1


        print("user=" + uid , "amount=" + str(amt), "tag=" + tag)
    print("BLACKLIST=" + str(black_list))
    print("HIGH_AMOUNT=" + str(high_amount))
    print("NORMAL=" + str(normal_amount))

#15按用户统计风险特征（用字典做聚合）
# first test
# def exercise15():
    # transactions = [
    # {"user_id": "u1", "amount": 100},
    # {"user_id": "u2", "amount": 800},
    # {"user_id": "u3", "amount": 5000},
    # {"user_id": "u1", "amount": 2000},
    # {"user_id": "u4", "amount": 50},
    # {"user_id": "u2", "amount": 1200},
    # {"user_id": "u3", "amount": 300},
    # ]   


    # for status in transactions:
    #     uid = status["user_id"]
    #     amt = status["amount"]
    #     if uid not in status:
    #         status[uid] = {"total":0,"count":0,"max":0}
    #         status[uid]["count"] += 1
    #         status[uid]["total"] += amt

    #     if amt >= status[uid]["max"]:
    #         max = status["amount"]


    #     print(f"user={uid},total={total},count={count},max={max}")


                

if __name__ == "__main__":
    exercise15()