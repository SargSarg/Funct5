#map
def map_(func, some_list):
    # some_list объект, над которым будет производиться преобразование
    # func функция, которая должна выполняться над каждым объектом
    outp = []
    for i in range(len(some_list)):
        outp.append(func(some_list[i]))
    return outp


L = ['THIS', 'IS', 'LOWER', 'STRING']
print(list(map(str.lower, L)))
# ['this', 'is', 'lower', 'string']

#filter
x = [-2, -1, 0, 1, -3, 2, -3]
def even(x): #вернуть только четные числа
   return x % 2 == 0
result = filter(even, [-2, -1, 0, 1, -3, 2, -3]) #функция filter вернет только нужные нам числа
print(list(result))   # [-2, 0, 2]

#lambada
# эти две функции выполняют одно и тоже — складывают два числа
def my_function(x1, x2):  # Обычная функция
   return x2 + x1
lambda x1, x2: x2 + x1  # Анонимная функция


d = {2 : "c", 1 : "d", 4 : "a", 3 : "b"}
# Чтобы отсортировать его по ключам, нужно сделать так:
print(dict(sorted(d.items())))
# {1: 'd', 2: 'c', 3: 'b', 4: 'a'}

# (вес, рост)
data = [
   (82, 191),
   (68, 174),
   (90, 189),
   (73, 179),
   (76, 184)]
sorted(data, key = lambda x: x[0] / (x[1]/100) ** 2)


a = ["asd", "bbd", "ddfa", "mcsa"] #посчитать число символов в каждом элементе списка
print(list(map(len, a))) #либо так
print(list(map(lambda x: len(x), a))) #либо так


a = ["это", "маленький", "текст", "обидно"] #перевести строки в верхний регистр(то есть КАПСОМ)
print(list(map(str.upper, a)))