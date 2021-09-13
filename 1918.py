import sys 


stack = []
result = ""

def calc_func(s1, c, s2):
    return s1 + s2 + c


fm = input()
p_cnt = 0

for i in range(len(fm)):
    if  fm[i] == '(' :
        p_cnt+=1
    elif fm[i] == ')' :
        s2 = stack.pop()
        c = stack.pop()
        s1 = stack.pop()
        stack.append(calc_func(s1,c,s2))
        top = stack.pop()
        if top == '*' or top == '/':
            s
        else :
            stack.append(top)
        p_cnt-=1
    elif fm[i] == '*' or fm[i] == '/' :
        
    elif fm[i] == '+' or fm[i] == '-' :

    else :
        stack.append(fm[i])