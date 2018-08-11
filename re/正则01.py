
def check_phone(phone):
    '''根据一定规则判断手机号是否合法'''
    if not phone.isdigit():
        return False
    if len(phone) != 11:
        return False
    if phone[0] != '1':
        return False
    if phone[1] not in ['3', '5', '7', '8']:
        return False
    return True

print(check_phone('13186817687'))
print(check_phone('23186817687'))

# 使用正则表达式，需要导入re模块
import re
# 匹配上返回match对象 ，没匹配上返回None
m = re.match('1[3578]\d{9}','13245893421')
print(m)