def distance(current, selection):
    if selection == 0:
        selection = 11
    if current == 0:
        current = 11
    dist = 0
    if current % 3 == 0:  # 오른쪽
        current -= 1
        dist += 1 + abs((selection - current)) / 3
    elif current % 3 == 1:  # 왼쪽
        current += 1
        dist += 1 + abs((selection - current)) / 3
    elif current % 3 == 2:  # 중간
        dist += abs((selection - current)) / 3

    return dist


def solution(numbers, hand):
    cur_left = 10
    cur_right = 12
    answer = ''
    for i in numbers:
        if i == 1 or i == 4 or i == 7:
            cur_left = i
            answer += 'L'
        elif i == 3 or i == 6 or i == 9:
            cur_right = i
            answer += 'R'
        else:
            left_dist = distance(cur_left, i)
            right_dist = distance(cur_right, i)
            if left_dist > right_dist:
                cur_right = i
                answer += 'R'
            elif left_dist < right_dist:
                cur_left = i
                answer += 'L'
            else:
                if hand == 'left':
                    cur_left = i
                    answer += 'L'
                else:
                    cur_right = i
                    answer += 'R'
    return answer