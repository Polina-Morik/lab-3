def find_common_participants(participants_first_group, participants_second_group, raz = ","):
    participants_first_group = participants_first_group.split(raz)
    participants_second_group = participants_second_group.split(raz)
    rezult = set(participants_first_group).intersection(set(participants_second_group))
    rezult = list(rezult)
    rezult.sort()
    return rezult

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой
print(find_common_participants(participants_first_group, participants_second_group, raz = "|"))
