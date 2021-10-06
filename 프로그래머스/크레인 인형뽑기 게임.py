def solution(board, moves):
    answer = 0
    stack = []
    
    for j in moves:
        for i in range(len(board)):
            if board[i][j-1] == 0:
                continue
            else:
                stack.append(board[i][j-1])
                board[i][j-1] = 0
                
                if len(stack) > 1:
                    if stack[-1] == stack[-2]:
                        del stack[-1]
                        del stack[-1]
                        answer += 2                
                break
    return answer
