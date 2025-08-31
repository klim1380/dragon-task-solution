def calculate_max_power(n):

    if n <= 1:
        return 1
    if n == 2:
        return 2
    if n == 3:
        return 3
    if n == 4:
        return 4
    if n == 5:
        return 6  
    if n == 6:
        return 9  
    

    dp = [0] * (n + 1)
    

    dp[0] = 1
    dp[1] = 1
    dp[2] = 2
    dp[3] = 3
    dp[4] = 4
    dp[5] = 6
    dp[6] = 9
    
 
    for i in range(7, n + 1):

        max_product = 0
        for j in range(2, 8):
            if j <= i:

                product = j * dp[i - j]
                if product > max_product:
                    max_product = product
        dp[i] = max_product
    
    return dp[n]


def main():
    try:

        n = int(input("Введите количество голов N (0 < N < 100): "))
        

        if n <= 0 or n >= 100:
            print("Ошибка: число должно быть в диапазоне 0 < N < 100")
            return
        

        result = calculate_max_power(n)
        print(f"Максимальная сила стаи из {n} голов: {result}")
        
    except ValueError:
        print("Ошибка: введите целое число")


if __name__ == "__main__":
    main()