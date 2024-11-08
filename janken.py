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
        
    prin = 'null'
    if you == 1 :
        if enemy == 2:
            you_count += 1
            prin = '勝ち'
        elif enemy == 3:
            prin = '負け'
            
    if you == 2 :
        if enemy == 3:
            you_count += 1
            prin = '勝ち'
        elif enemy == 1:
            prin = '負け'
            
    if you == 3 :
        if enemy == 1:
            you_count += 1
            prin = '勝ち'
        elif enemy == 2:
            prin = '負け'
        

    print(f'\n相手の手 : {enemy} \nあなたの手 : {you}\nあなたの{prin}\n\n----------------')
    
print(f'あなたの勝利数は{you_count}です。')


