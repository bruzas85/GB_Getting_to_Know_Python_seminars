'''Задача 21.
Напишите программу для печати всех уникальных 
значений в словаре. 
Input: [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, 
{"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII 
":" S007 "}] 
Output: {'S005', 'S002', 'S007', 'S001', 'S009'}
'''

my_list = [{"V": " S001 "}, {"V": " S002 "}, {"VI": " S001 "}, 
{"VI": " S005 "}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII ":" S007 "}] 
set_values = set()

for i in my_list:
    print(i)
    set_values.add(list(i.values())[0])
print(*set_values)
print(type(set_values))