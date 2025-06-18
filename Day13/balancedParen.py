s = "()[{}()]"
st = []
for it in s:
    if it == '(' or it == '{' or it == '[':
        st.append(it)
    else:
        if len(st) == 0:
            print (False)
            break
        ch = st[-1]
        st.pop()
        if (it == ')' and ch == '(') or (it == ']' and ch == '[') or (it == '}' and ch == '{'):
            continue
        else:
            print (False)
            break
print (len(st) == 0) 