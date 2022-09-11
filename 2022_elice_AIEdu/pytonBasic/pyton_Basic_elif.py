answer=32
submit=int(input())

if answer<submit:
    print("정답보다 더 큰 수를 입력했습니다.")
elif answer>submit:
    print("정답보다 더 작은 수를 입력했습니다.")
else:
    print("정답!")