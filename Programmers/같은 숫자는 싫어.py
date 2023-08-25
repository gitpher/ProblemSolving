# def solution(arr):
#     answer = []
    
#     chk = [10]
#     for x in arr:
#         if x != chk[0]:
#             answer.append(x)
#             chk[0] = x
    
#     return answer

def solution(arr):
    answer = []
    answer.append(arr[0])
    
    for i in range(1, len(arr)):
        if arr[i] != arr[i-1]:
            answer.append(arr[i])
            
    return answer
