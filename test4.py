students = [{'name': 'Alice', 'scores': {'Math': 85, 'English': 92, 'Science': 88}},
            {'name': 'Bob', 'scores': {'Math': 78, 'English': 88, 'Science': 82}},
            {'name': 'Charlie', 'scores': {'Math': 90, 'English': 95, 'Science': 91}}]


def calculate_score(stus):
    for name_, scores_ in ((s['name'], s['scores'].values()) for s in stus):
        total_score = sum(scores_)
        average_score = total_score / len(scores_)
        print(f"{name_}的总分是{total_score}，平均分是{average_score:.2f}")


calculate_score(students)
