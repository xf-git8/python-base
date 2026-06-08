# use function and **variable build a user_profile
# **variable if define package to a dict(key=value,key=value===> {key:value,key:value})
# if print user_info  {key:value,key:value}
def build_profile(first,last,**user_info)->dict[str,str]:
    """
    Build a dict concat about user
    :param first:
    :param last:
    :param user_info:
    :return:
    """
    print(user_info)
    user_info['first_name'] = first
    user_info['last_name'] = last

    return user_info
user_profile = build_profile('娜娜','欧阳',age = 24,sex='woman')
print(user_profile)