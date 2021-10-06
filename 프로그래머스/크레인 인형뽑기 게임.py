def solution(board, moves):
    answer = 0
    cnt = 0

    for j in moves:
        for i in range(len(board)):
            if board[i][j-1] == 0:
                continue
            else:
                if board[i][j-1] != cnt:
                    cnt = board[i][j-1]
                else:
                    answer += 2
                    cnt = 0
                board[i][j-1] = 0
                break
    return answer