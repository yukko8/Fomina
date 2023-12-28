days = int(input("Введите количество дней "))
hours = int(input("Введите количество часов "))
minutes = int(input("Введите количество минут "))
seconds = int(input("Введите количество секунд "))
seconds_in_day = days * 86400
seconds_in_hour = hours * 3600
seconds_in_minute = minutes * 60
all_seconds = seconds_in_day + seconds_in_hour + seconds_in_minute + seconds
print(all_seconds)

