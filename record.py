#1
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
def excercise9():
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



if __name__ == "__main__":
    exercise10()