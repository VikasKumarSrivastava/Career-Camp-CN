# sample input 1 [()]{}{[()()]()} --> True
# sample input 2 [[}[  -->False
# Ques from code studio --> ValidParenthesis
def isValidParenthesis(s: str) -> bool:
    # Write your code here
    st=[]
    for e in s:
        if e in '[{(':
            st.append(e)
        elif e==')':
            if len(st) != 0 and st[-1] =='(':
                st.pop()
            else:
                return False
        elif e=='}':
            if len(st)!=0 and st[-1]=='{':
                st.pop()
            else:
                return False
        elif e==']':
            if len(st)!=0 and st[-1]=='[':
                st.pop()
            else:
                return False
    if st :
        return False
    else:
        return True	
