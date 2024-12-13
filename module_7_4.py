team1_num = 5
team2_num = 6
score_1 = 40
score_2 = 42
team2_time = 18015.2
team1_time = 10717.6
tasks_total = 82
time_avg = 350.4

def challenge_result():
    if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
        return 'Победа команды Мастера кода'
    elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:
        return 'Победа команды Волшебники данных'
    else:
        return 'Ничья'

print('В команде Мастеров кода участников: %s' % 5)
print('Итого сегодня в командах участников: %s и %s' % (5, 6))
print('Команда Волшебники данных решила задач: {score_2}'.format(score_2 = 42))
print('Волшебники данных решили задачи за {} {}'.format(18015.2, 'с'))
print(f'Команды решили {score_1} и {score_2} задач.')
print(f'Результат битвы: {challenge_result()}')
print(f'Сегодня было решено {tasks_total} задачи, в среднем по {time_avg} секунды на задачу.')