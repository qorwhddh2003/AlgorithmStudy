def solution(s):
    answer = True
    
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    
    if s.count('p') + s.count('P') != s.count('y') + s.count('Y') : 
        answer = False

    return answer