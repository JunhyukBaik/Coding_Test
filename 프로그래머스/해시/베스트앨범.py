def solution(genres, plays):
    answer = []
    dic = {}
    
    for i in range(len(genres)):
        if genres[i] not in dic:
            dic[genres[i]] = [plays[i], i, plays[i], i, 0] #(장르 총 재생수, 1등번호, 1등재생수, 2등번호, 2등재생수)
        else:
            dic[genres[i]][0] += plays[i]
            if plays[i] > dic[genres[i]][2]:
                dic[genres[i]][3] = dic[genres[i]][1]
                dic[genres[i]][4] = dic[genres[i]][2]
                dic[genres[i]][1] = i
                dic[genres[i]][2] = plays[i]
            elif plays[i] == dic[genres[i]][2]:
                dic[genres[i]][3] = i
                dic[genres[i]][4] = plays[i]
            else:
                if plays[i] > dic[genres[i]][4]:
                    dic[genres[i]][3] = i
                    dic[genres[i]][4] = plays[i]
                             
    dic = sorted(dic.items(), key=lambda x:x[1][0], reverse = True)
    
    for i in dic:
        answer.append(i[1][1])
        if i[1][4] != 0:
            answer.append(i[1][3])   
            
    return answer