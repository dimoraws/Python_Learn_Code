temperature = []

# .strip() удаление пробелов с обоих сторон текста
# ' aaabb    \n\r\t'.strip() ---> 'aaabb'
# .split() делает и одной строки на части, по линиям

print("Worked?")
# Расширение списка
# а = [1, 2, 3]
# b = [7, 8, 9]
# a.append(b)
# 1, 2, 3, [7, 8, 9]
# a.extend(b)
# 1, 2, 3, 7, 8, 9
with open('temperature.txt') as t:
    for line in t:
        temperature.append(int(line.strip()))

avg = sum(temperature)/len(temperature)

temperature_deviation = []

for t in temperature:
    temperature_deviation.append(t - avg)

print('Srednaya tempertura:', avg)

print(temperature)
# \n символ переноса строки



with open('average_temperature.txt', 'w') as average_temp:
    average_temp.write(str(avg))
    # "%.2f" % avg - выводит только 2 знака после запятой
with open('average_deviation.txt', 'w') as t_deviatin_file:
    for t in temperature_deviation:
        t_deviatin_file.write("%.2f\n" % t)