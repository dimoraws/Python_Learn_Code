#urok2_up2

residence_limit = 90
shengen_constaint = 180
total_time_in_es = 0
visits = [[1,10], [61,90], [101, 140], [141, 160], [271, 290]]
day_for_visits = []
for visit in visits:
    day_for_visit = 0
    for past_visit in visits:
        if past_visit[0] < visit[0] and (visit[0] - shengen_constaint < past_visit[0]):
            # Считаем только визиты вплоть до текущего
            day_for_visit += past_visit[1] - past_visit[0] + 1

    day_for_visit += visit[1] - visit[0] + 1
    day_for_visits.append(day_for_visit)

print(day_for_visits)
assert (day_for_visits == [10, 10 + 30, 10 + 30 + 40, 10 + 30 + 40 + 20, 40 + 20 + 20])

for visit, total_days in zip(visits, day_for_visits):
    if __name__ == '__main__':
        if total_days > residence_limit:
            overstay_time = total_days - residence_limit
            print('Во впремя визита', visit, 'количество время пребывания превышено на', overstay_time, 'дней')