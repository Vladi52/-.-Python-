def appearance(intervals):
    iteration_fre_visit, answer, itter = 0, 0, 0
    min_lesson_time, max_lesson_time = intervals['lesson'][0], intervals['lesson'][-1]
    pupils, tutor = intervals['pupil'], intervals['tutor']

    while itter < len(pupils):
        if itter + 2 < len(pupils):
            if pupils[itter + 1] < pupils[itter] < pupils[itter + 2] and (itter + 2) % 2 == 0:
                del pupils[itter + 1]
                itter -= 1
            elif pupils[itter + 1] < pupils[itter] < pupils[itter + 2] and (itter + 2) % 2 != 0:
                del pupils[itter]
                del pupils[itter]
                itter -= 1
            elif pupils[itter] >= pupils[itter + 2]:
                del pupils[itter + 1]
                del pupils[itter + 1]
                itter -= 1
        itter += 1

    if len(pupils) > len(tutor):
        frequent_visit, rare_visit = pupils, tutor
    else:
        frequent_visit, rare_visit = tutor, pupils

    while iteration_fre_visit < len(frequent_visit):
        iteration_rar_visit = 0
        while iteration_rar_visit < len(rare_visit):

            left_bord = max(frequent_visit[iteration_fre_visit], rare_visit[iteration_rar_visit])
            right_board = min(frequent_visit[iteration_fre_visit + 1], rare_visit[iteration_rar_visit + 1])
            if left_bord < right_board:
                if left_bord < min_lesson_time <= right_board:
                    total_time = range(min_lesson_time, right_board + 1)
                    answer += total_time[-1] - total_time[0]
                elif right_board < max_lesson_time:
                    total_time = range(left_bord, right_board + 1)
                    answer += total_time[-1] - total_time[0]
                else:
                    total_time = range(left_bord, max_lesson_time + 1)
                    answer += total_time[-1] - total_time[0]
            iteration_rar_visit += 2
        iteration_fre_visit += 2
    return answer


tests = [
    {'data': {'lesson': [1594663200, 1594666800],
              'pupil': [1594663340, 1594663389, 1594663390, 1594663395, 1594663396, 1594666472],
              'tutor': [1594663290, 1594663430, 1594663443, 1594666473]},
     'answer': 3117
     },
    {'data': {'lesson': [1594702800, 1594706400],
              'pupil': [1594702789, 1594704500, 1594702807, 1594704542, 1594704512, 1594704513, 1594704564, 1594705150,
                        1594704581, 1594704582, 1594704734, 1594705009, 1594705095, 1594705096, 1594705106, 1594706480,
                        1594705158, 1594705773, 1594705849, 1594706480, 1594706500, 1594706875, 1594706502, 1594706503,
                        1594706524, 1594706524, 1594706579, 1594706641],
              'tutor': [1594700035, 1594700364, 1594702749, 1594705148, 1594705149, 1594706463]},
     'answer': 3577
     },
    {'data': {'lesson': [1594692000, 1594695600],
              'pupil': [1594692033, 1594696347],
              'tutor': [1594692017, 1594692066, 1594692068, 1594696341]},
     'answer': 3565
     },
]

if __name__ == '__main__':
    for i, test in enumerate(tests):
        test_answer = appearance(test['data'])
        assert test_answer == test['answer'], f'Error on test case {i}, got {test_answer}, expected {test["answer"]}'
