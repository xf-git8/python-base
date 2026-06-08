def build_profile(first, last, **user_info)->dict:
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info
user_profile = build_profile('娜娜','欧阳',age=34,height=175.6)
print(user_profile)