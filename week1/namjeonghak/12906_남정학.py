def solution(arr):
    answer = []
    leng = len(arr)
    answer.append(arr[0])
    for i in range(1,leng):
        if arr[i]!=answer[-1]:
            answer.append(arr[i])
    return answer