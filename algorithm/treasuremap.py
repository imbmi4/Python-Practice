def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        answer.append(bin(arr1[i] | arr2[i]))
        answer[i] = answer[i].replace("0b", "")
        answer[i] = answer[i].replace("1", "#")
        answer[i] = answer[i].replace("0", " ")
        while (len(answer[i]) != n):
            answer[i] = ' ' + answer[i]

    return answer