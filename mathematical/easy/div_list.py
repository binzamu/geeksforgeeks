def create_divisor_set(a):
    divisor_set = [1]
    n = 2
    while n * n < a:
        if a % n == 0:
            divisor_set.append(n)
            divisor_set.append(a // n)
        n += 1
    
    if n * n == a:
        divisor_set.append(n)
    return divisor_set

def main():
    n = int(input())
    print(create_divisor_set(n))

if __name__ == "__main__":
    main()
