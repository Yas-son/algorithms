# Глава 3.Рекурсия (60стр)

def factorial_recursive(n):
    if n == 1: 
        return n # Условие завершения (базовый случай)
    else:
        return n*factorial_recursive(n-1) # Рекурсия (рекурсионный случай)
print(factorial_recursive(7))




# def fib(n):
#     if n in [1, 2]: # Если n содержиться в списке [1, 2] - базовый  
#         return 1
#     else:
#         return fib(n-1) + fib(n-2)
# list = []
# for e in range(1, 10): # Тоже базовый случай (ограничивает работу)
#     list.append(fib(e)) # Просмотр первых 10 чисел фибоначи 
# # (def fib(n)) - рекурсивный случай
# print(list) # 1 1 2 3 5 8 13 21 34
