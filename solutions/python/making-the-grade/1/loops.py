def round_scores(student_scores):
    rounded_scores = []
    for score in student_scores:
        rounded_scores.append(round(score))
    return rounded_scores

def count_failed_students(student_scores):
    counts=0
    for i in student_scores:
        if i<=40 :
            counts+=1
    return counts

def above_threshold(student_scores, threshold):
    best=[]
    for i in student_scores:
        if i>= threshold:
            best.append(i)
    return best

def letter_grades(highest):
    step = (highest - 40) // 4
    return [41 + i * step for i in range(4)]

def student_ranking(student_scores, student_names):
    Count=1
    list=[]
    for i,j in zip(student_scores,student_names):
        list.append(f"{Count}. {j}: {i}")
        Count+=1
    return list

def perfect_score(student_info):
    for student in student_info:
        if student[-1] == 100:
            return student
    return []
