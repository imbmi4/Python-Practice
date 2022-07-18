import re


def Step1(id):
    return id.lower()


def Step2(id):
    # table = str.maketrans('~!@#$%^&*()=+[{]}:?,<>/','                       ') #야매
    # id = id.translate(table)
    # return id.replace(' ','')

    # id = re.sub('[^0-9a-z-_.]',"",id) #화이트리스트의 여집합

    id = re.sub('[~!@#$%^&*()=+\[{\]}:?,<>/]', "", id)  # 블랙리스트
    # return id.replace(' ','')
    return id


def Step3(id):
    return re.sub('\.\.+', '.', id)


def Step4(id):
    if (id[0] == '.'):
        id = id[1:]
    if (id == ''):
        return ''
    if (id[-1] == '.'):
        id = id[:-1]
    return id


def Step5(id):
    if (id == ''):
        id += 'a'
    return id


def Step6(id):
    if (len(id) >= 16):
        id = id[0:15]
        if (id[-1] == '.'):
            id = id[:-1]
    return id


def Step7(id):
    if (len(id) <= 2):
        while (len(id) != 3):
            id += id[-1]
    return id


def solution(new_id):
    answer = Step1(new_id)
    print("Step1: ", answer)
    answer = Step2(answer)
    print("Step2: ", answer)
    answer = Step3(answer)
    print("Step3: ", answer)
    answer = Step4(answer)
    print("Step4: ", answer)
    answer = Step5(answer)
    print("Step5: ", answer)
    answer = Step6(answer)
    print("Step6: ", answer)
    answer = Step7(answer)
    print("Step7: ", answer)
    return answer