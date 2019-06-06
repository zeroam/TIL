#include "01.h"
#include <iostream>

void exercise::number1()
{
	using namespace std;
	const int CHAR_NUM = 20;

	char first_name[CHAR_NUM];
	char last_name[CHAR_NUM];
	char score;
	int age;

	cout << "영문 퍼스트 네임 (이름) : ";
	cin.getline(first_name, CHAR_NUM);
	cout << "영문 라스트 네임 (성) : ";
	cin.getline(last_name, CHAR_NUM);
	cout << "학생이 원하는 학점: ";
	cin >> score;
	cout << "나이: ";
	cin >> age;

	if (score == 'A' || score == 'B' || score == 'C') {
		score = score + 1;
	}
	else {
		score = 'F';
	}

	cout << "성명: " << last_name << ", " << first_name << endl;
	cout << "학점: " << score << endl;
	cout << "나이: " << age << endl;

}
