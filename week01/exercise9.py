for i in range(1, 21):
    if i % 2 != 0:
        print(i)

print("\n")
for i in range(100, 1, -10):
    print(i)  # 倒数指的是数学上的还是倒着数数。。。

for i in range(2, 13, 2):
    if i > 7:
        print(i)
        break
else:
    print("没有大于7的数字")

print("\n")
answer = 42
guess_number = 1
while True:
    if guess_number == answer:
        print(f"在第{guess_number}次猜到了")
        break
    guess_number += 1

## while (guess_number := 1) !=answer:
##      guess_number += 1
## print(f"在第{guess_number}次猜到了")