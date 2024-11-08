while n<1:
    you = int(input('----------------\nグー : 1\nチョキ : 2\n パー : 3\nあなたの手 >>'))
    if you > 3 or you < 1:
        print('半角数字1~3')
    elif you == enemy:
        print('あいこ\n\n----------------')
        enemy = r.randrange(1,4)
    else:
        n = 1