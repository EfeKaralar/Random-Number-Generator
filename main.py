# x0=seed; a=multiplier; b=increment; m=modulus; n=desired array length;
# Requirements --> 0<a<m; 0<=b<m; 0<=x0<m
def linearRandomGenerator(x0, a, b, m, n):
    results = []
    for i in range(n):
        x0 = (a * x0 + b) % m
        results.append(x0)
    return results

print(linearRandomGenerator(13, 3, 5, 20, 3))
