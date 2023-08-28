def solution(nums):
    
    tot = len(nums) # 총 갯수
    typ = len(set(nums)) # 종류 갯수
    sel = tot // 2 # 선택 가능 갯수
    
    return typ if sel >= typ else sel
