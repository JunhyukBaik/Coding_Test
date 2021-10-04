def solution(arr):
    answer = []
    tmp = arr[0]
    answer.append(tmp)
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    for i in range(1,len(arr)):
        if arr[i] == answer[-1]:
            continue
        else:
            answer.append(arr[i])
    return answer