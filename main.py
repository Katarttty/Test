
score=5
total=5

Mark = int(score/total)*100
def pass_fail():
    for x in range(Mark):
        if Mark >= 50:
            print(Mark)
            print('pass')
            break
        elif Mark < 50:
            print(Mark)
            print('fail')
            break

pass_fail()


