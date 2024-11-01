def find_common_participants(first_group, second_group, razd = ','):
    group1 = set(first_group.split(razd)) # создаем множества для обеих групп разделяя методом split
    group2 = set(second_group.split(razd))
    common_participants = group1.intersection(group2) # проверяем пересечения
    return sorted(common_participants) # сортируем по алфавиту


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"
razdelitel = '|'

print(find_common_participants(participants_first_group, participants_second_group, razdelitel))
