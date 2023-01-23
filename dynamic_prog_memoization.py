def add_to_80(n):
    print('long time calculation...')
    return n + 80

print(add_to_80(5))
print(add_to_80(5))


# Memoization - 1 - hard coded
cache = {}
def add_to_80_memoization(n):
    if n in cache:
        return cache[n]
    print('caching, long time calculation...')
    cache[n] = n + 80
    return cache[n]

print(add_to_80_memoization(5))
print(add_to_80_memoization(5))



# Memoization - 2 - lru caching from functools
# Saves up to the maxsize most recent calls
# A dictionary is used to cache results

from functools import lru_cache

@lru_cache(maxsize=200)
def add_to_80_lru(n):
    print('lru caching, long time calculation...')
    return n + 80

print(add_to_80_lru(5))
print(add_to_80_lru(5))
print(add_to_80_lru.cache_info())


# Fibonacci using dynamic programming 
# Memoization
cache = {}
def fibonacci(n):
    if n in cache:
        return cache[n]
    if n < 2:
        return n
    else:
        cache[n] = fibonacci(n-1) + fibonacci(n-2)
        return cache[n]

print(fibonacci(7))
print(cache)

# lru caching
@lru_cache(maxsize=200)
def fibonacci_lru(n):
    if n < 2:
        return n
    else:     
        return fibonacci_lru(n-1) + fibonacci_lru(n-2)

print(fibonacci_lru(7))
print(fibonacci_lru.cache_info())
