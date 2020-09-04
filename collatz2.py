def collatz(number):
    if number % 2 == 0:
        return number // 2

    if number % 2 == 1:
        return 3 * number + 1

print("整数を入力してください：")

try:
    number = int(input())

except ValueError:
    print("整数値を入力してください")
    number = int(input())
    
while True:
    print(number)
    if number == 1:
        break
    number = collatz(number)
