class Student:

    def __init__(self, name, id, major):
        self.name = name
        self.id = id
        self.major = major
        self.grades = GradeManager()

    def change_student_info(self, new_name, new_id, new_major):
        """학생 기본 정보 수정 메소드"""
        self.name = new_name
        self.id = new_id
        self.major = new_major

    def print_report_card(self):
        """학생 성적표 출력 메소드"""
        print('코드잇 대학 성적표\n')
        print(f'학생 이름:{self.name}')
        print(f'학생 번호:{self.id}')
        print(f'소속 학과:{self.major}')
        print(f'평균 학점:{self.grades.get_average_gpa()}')


class GradeManager:

    def __init__(self):
        self._grades = []

    def add_grade(self, grade):
        if 0 <= grade <= 4.3:
            self._grades.append(grade)
        else:
            print("수업 학점은 0과 4.3 사이여야 합니다!")

    def get_average_gpa(self):
        return sum(self._grades) / len(self._grades)

        

if __name__ == '__main__':
    # 학생 인스턴스 정의
    younghoon = Student("강영훈", 20120034, "통계학과")
    younghoon.change_student_info("강영훈", 20130024, "컴퓨터 공학과")

    # 학생 성적 추가
    younghoon.grades.add_grade(3.0)
    younghoon.grades.add_grade(3.33)
    younghoon.grades.add_grade(3.67)
    younghoon.grades.add_grade(4.3)

    # 학생 성적표 
    younghoon.print_report_card()
