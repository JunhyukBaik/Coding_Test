def solution(n, lost, reserve):
    set_rsv = set(reserve) - set(lost)
    set_lst = set(lost) - set(reserve)
    for rsv in set_rsv:
        if rsv - 1 in set_lst:
            set_lst.remove(rsv - 1)
        elif rsv + 1 in set_lst:
            set_lst.remove(rsv + 1)
    answer = n - len(set_lst)
    return answer