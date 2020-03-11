def course_selection(course_list):
    sorted_course_list = sorted(course_list, key=lambda x: (x[1], x[0]))
    best_courses = [sorted_course_list[0]]
    
    for course in sorted_course_list:
        if course[0] > best_courses[-1][1]:
            best_courses.append(course)
    
    return best_courses


if __name__ == '__main__':
    print(course_selection([(6, 10), (2, 3), (4, 5), (1, 7), (6, 8), (9, 10)]))
    print(course_selection([(1, 2), (3, 4), (0, 6), (5, 7), (8, 9), (5, 9)]))
    print(course_selection([(4, 7), (2, 5), (1, 3), (8, 10), (5, 9), (2, 5), (13, 16), (9, 11), (1, 8)]))
 