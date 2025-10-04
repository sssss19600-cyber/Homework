N, L, T, M = map(int, input().split())

cycles = M // T

result = N * (L ** cycles)

print(result)
