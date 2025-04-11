def get_my_chosun_name(family_name, month, day):
    list_month = ['쌍', '쇠', '복', '돌', '팽', '육', '쌍', '개', '칠', '갑', '삼', '방']
    list_day = ['봉', '구', '욕', '포', '똥', '삼', '식', '석', '놈', '님', '년', '돌', '단', '득', '방', '질', '장', '걸', '래', '룡', '동', '순', '자', '박', '창', '언', '것', '포', '만', '단', '국']
    
    return('당신의 조선시대 이름은 ' + family_name + list_month[month-1] + list_day[day-1])

print(get_my_chosun_name('이', 5, 6))