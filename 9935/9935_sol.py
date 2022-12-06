# 스택을 사용해서 문자열 구현 가능
arr = input()
bom_arr = input()

stack = []
bom_len = len(bom_arr)

for i in range(len(arr)):
    stack.append(arr[i])
    if ''.join(stack[-bom_len:]) == bom_arr:
        for _ in range(bom_len):
            stack.pop()

if stack:
    print(''.join(stack))
else:
    print('FRULA')
