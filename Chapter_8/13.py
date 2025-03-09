def build_profile(first,last,**user_info):
    user_info['First_name'] = first
    user_info['Last_name'] = last
    return user_info


user_profile = build_profile('Harshvardhan','Tomar',City='Gwalior',Status='Single')
print(user_profile)