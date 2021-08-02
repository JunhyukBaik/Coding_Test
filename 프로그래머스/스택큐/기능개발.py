def solution(progresses, speeds):
    dic = dict()
    cnt = 0
    for i in range(len(progresses)):
        complete = 100 - progresses[i]
        if complete % speeds[i] == 0:
            rst = complete // speeds[i]
        else:
            rst = complete // speeds[i] + 1

        if rst >= cnt:
            if rst not in dic:
                dic[rst] = 1
            else:
                dic[rst] += 1
            cnt = rst
        else:
            dic[cnt] += 1
    dic = sorted(dic.items())
    lst = list()
    for i in dic:
        lst.append(i[1])
    return lst