grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]# Дан список оценок для имен по алфавиту
# изменяем первоначальный список, на список со средними оценками, сумму списка в индексе делим на длину списка в индексе
average=[[sum(grades[0])/len(grades[0])],[sum(grades[1])/len(grades[1])],[sum(grades[2])/len(grades[2])],[sum(grades[3])/len(grades[3])],[sum(grades[4])/len(grades[4])]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}# дано множество имен студентов не по алфавиту
name=list(students)# множество имен изменим на тип "список"
name=sorted(name)# присвоение переменной сортированного списка
dict={name[0]:average[0],name[1]:average[1],name[2]:average[2],name[3]:average[3],name[4]:average[4]}# создаем словарь из индексов
print(dict)# выводим словарь на экран
