#3urok

residence_limit = 90
shengen_constaint = 180

visits = [[1, 10], [21, 30], [45, 46], [251, 260]]

# 10, 10 + 10, 10 + 10 + 2, 10

days_in_eu = []

total_time_in_es = 0

for visit in visits:
    past_days = 0
    for past_visit in visits:
        #if past_visit[0] <= visit[0] and past_visit[0] > visit[0] - shengen_constaint:
        if visit[0] - shengen_constaint < past_visit[0] <= visit[0]:
            past_days += past_visit[1] - past_visit[0] + 1
    days_in_eu.append(past_days) 

    total_time_in_es += visit[1] - visit[0] + 1


#assert total_time_in_es == 10 + 10 + 2 + 10
print(days_in_eu)
assert days_in_eu == [10, 10 + 10, 10 + 10 + 2, 10]

for visit, days in zip(visits, days_in_eu):
    if days > residence_limit:
        print('В течении этой поздкти', visit, 'выпребывали слишком долго:', days)

if total_time_in_es > residence_limit:
    # На сколько дней превышен
    residence_fault = shengen_constaint - total_time_in_es
    print('Лимит пребывания в Евросоюзе, превышен на:', residence_fault)
    print('Пожалуйста выберите другие даты')
else:
    print('Не волнуйтесь, вы успеваете побывать в ЕС')

print('Вы пробудеете в ЕС дней:', total_time_in_es)