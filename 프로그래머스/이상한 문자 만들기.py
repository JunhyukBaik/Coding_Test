def solution(s):
    answer = ''
    hj = 0 #홀짝
    for i in range(len(s)):
        if s[i] == ' ':
            hj = 0
            answer += ' '
            continue
            
        if hj % 2 == 0:
            answer += s[i].upper()
        else:
            answer += s[i].lower()
        hj += 1
        
    return answer