residence_limit = 90
shengen_constaint = 180
total_time_in_es = 0
visits = [[1,10], [30,54], [60, 89], [120, 159]]

for visit in visits:
    total_time_in_es += visit[1] - visit[0] + 1

overstay_time = total_time_in_es - residence_limit
print('Вы превысили время пребывания, на:', overstay_time)
assert (overstay_time == 10 + 25 + 30 + 40 - residence_limit)