def korean_number(number):
    if number == 1:
        return '일'
    elif number == 2:
        return '이'
    elif number == 3:
        return '삼'
    elif number == 4:
        return '사'
    elif number == 5:
        return '오'
    elif number == 6:
        return '육'
    elif number == 7:
        return '칠'
    elif number == 8:
        return '팔'
    elif number == 9:
        return '구'
    else:
        return '십'
    
print(korean_number(8))
    