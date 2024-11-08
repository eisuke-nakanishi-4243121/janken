
import random as r

you_count = 0
for a in range(3):
    print(f'----ラウンド{a+1}----')
    n = 0
    you = 0
    enemy = r.randrange(1,4)
    while n<1:
    you = int(input('----------------\nグー : 1\nチョキ : 2\n パー : 3\nあなたの手 >>'))
    if you > 3 or you < 1:
        print('半角数字1~3')
    elif you == enemy:
        print('あいこ\n\n----------------')
        enemy = r.randrange(1,4)
    else:
        n = 1
        

    print(f'\n相手の手 : {enemy} \nあなたの手 : {you}\nあなたの{prin}\n\n----------------')
    
print(f'あなたの勝利数は{you_count}です。')

