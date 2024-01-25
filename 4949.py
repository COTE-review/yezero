while(1):
    line = input()
    line_1 = list(line)
    stack = []
    temp = True

    if(line =='.'):
        break
    for i in line_1:
        if( i == '(' or i == '['):
            stack.append(i)
        elif(i==')'):
            if not stack or stack[-1]=='[':
                temp = False
                break
            elif stack[-1] == '(':
                stack.pop()
        elif(i==']'):
            if not stack or stack[-1]=='(':
                temp = False
                break
            elif stack[-1] == '[':
                stack.pop()
    if temp == True and not stack:
        print("yes")
    else:
        print("no")
        
#문자열이 있는 동안에 while문 진행
#input으로 입력받아 리스트에 넣어줌 
#문자열이 '.'이면 while문 break
#괄호가 열리면 stack에 쌓아두기
#괄호가 안 열렸는데 닫히면 temp애 "false" 저장
#닫히는 괄호가 나왔을 때 stack의 최상단 원소가 똑같은 형태의 열린 괄호이면
#stack에서 뽑아줌
#temp가 "true"이고, stack이 비어있으면 yes를 출력
#그렇지 않으면 "no" 출력