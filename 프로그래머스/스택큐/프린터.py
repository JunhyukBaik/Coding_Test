import copy
def solution(priorities, location):
    answer = 0
    cnt = 0
    i = 0
    num_list = copy.deepcopy(priorities)
    num_list.sort(reverse=True)
    
    for i in range(len(priorities)):
        priorities[i] = (priorities[i], i)
    
    while(True):
        if priorities[cnt][0] < num_list[0]:
            tmp = priorities[cnt]
            del priorities[cnt]
            priorities.append(tmp)          
        elif priorities[cnt][0] == num_list[0]:
            del num_list[0]
            #print(num_list)
            cnt += 1
        print(priorities, num_list)
        if cnt >= len(priorities):
            break
    for a in range(len(priorities)):
        if location == priorities[a][1]:
            answer = a + 1
            break
    #print(priorities, num_list)
    return answer

p=[2, 3, 9, 1, 1, 1]	
l= 0
print(solution(p,l))