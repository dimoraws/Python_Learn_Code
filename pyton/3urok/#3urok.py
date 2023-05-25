#3urok

residence_limit = 90
shengen_constaint = 180

visit_1 = [1, 10]

visit_2 = [21, 30]

visit_3 = [45, 46]

visit_4 = [91, 100]

visits = [visit_1, visit_2, visit_3, visit_4]

total_time_in_es = 0

for visit in visits:
    total_time_in_es += visit[1] - visit[0] + 1


assert total_time_in_es == 10 + 10 + 2 + 10

if total_time_in_es > residence_limit:
    # На сколько дней превышен
    residence_fault = shengen_constaint - total_time_in_es
    print('Лимит пребывания в Евросоюзе, превышен на:', residence_fault)
    print('Пожалуйста выберите другие даты')
else:
    print('Не волнуйтесь, вы успеваете побывать в ЕС')

print('Вы пробудеете в ЕС дней:', total_time_in_es)