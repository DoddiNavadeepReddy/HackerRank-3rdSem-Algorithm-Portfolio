n = int(input())
candles = list(map(int, input().split()))

maximum = max(candles)
count = candles.count(maximum)

print(count)