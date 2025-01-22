# Создаем кортеж
immutable_var=1,2,7,6,4,"true","Hello"
# выводим на экран
print(immutable_var)
# добавляем элемент в кортеж, но он неизменяем
#immutable_var.append("88")
#print(immutable_var)
# Добавляем элементы в кортеж, но он не изменяем
#immutable_var.extend([34,43])
#print(immutable_var)
# удаляем элемент из кортежа, но он не изменяем
#immutable_var.remove(2)
#print(immutable_var)
# Изменить кортеж не возможно,
# если в строке 2 все элементы
# заключим в квадратные скобки,
# то все заработает.
mutable_list=[1,2,7,6,4,"true","Hello"]
print(mutable_list)
mutable_list.append("88")
print(mutable_list)
mutable_list.extend("66")
print(mutable_list)
mutable_list[5:7]=[]
print(mutable_list)
mutable_list.remove(2)
print(mutable_list)