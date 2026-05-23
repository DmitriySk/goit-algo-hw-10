import timeit

coins = [50, 25, 10, 5, 2, 1]

def add_to_result(result, coin):
    if coin in result:
        result[coin] += 1
    else:
        result[coin] = 1
    return result

def find_coins_greedy(sum):
    result = {}
    while sum > 0:
        for coin in coins:
            if sum >= coin:
                sum -= coin
                result = add_to_result(result, coin)
                break
    return result

def find_min_coins_data(sum):
    min_coins_required = [0] + [float("inf")] * sum
    last_coin_used = [0] * (sum + 1)
    for s in range(1, sum + 1):
        for coin in coins:
            if s >= coin and min_coins_required[s - coin] + 1 < min_coins_required[s]:
                min_coins_required[s] = min_coins_required[s - coin] + 1
                last_coin_used[s] = coin
    return min_coins_required, last_coin_used

def find_min_coins(sum, data=None):
    min_coins_required, last_coin_used = data or find_min_coins_data(sum)
    result = {}
    while sum > 0:
        coin = last_coin_used[sum]
        result = add_to_result(result, coin)
        sum -= coin

    return result

print("Жадібний алгоритм:", timeit.timeit(lambda: find_coins_greedy(113), number=100000))
print("Алгоритм динамічного програмування:", timeit.timeit(lambda: find_min_coins(113), number=100000))

min_coins_data = find_min_coins_data(1000)
print(
    "Алгоритм динамічного програмування при розрахованих даних:",
    timeit.timeit(lambda: find_min_coins(113, min_coins_data), number=100000)
)

