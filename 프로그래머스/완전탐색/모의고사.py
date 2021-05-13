def solution(answers):
    answer = [0,0,0]
    no_1 = [1,2,3,4,5]
    no_2 = [2,1,2,3,2,4,2,5]
    no_3 = [3,3,1,1,2,2,4,4,5,5]
    for i in range(len(answers)):
        if answers[i] == no_1[i%5]:
                answer[0] += 1
        if answers[i] == no_2[i%8]:
            answer[1] += 1
        if answers[i] == no_3[i%10]:
            answer[2] += 1
    result = []
    if answer[0] == max(answer):
        result.append(1)
    if answer[1] == max(answer):
        result.append(2)
    if answer[2] == max(answer):
        result.append(3)
    return result