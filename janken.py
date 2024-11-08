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
