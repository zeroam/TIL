#include "02.h"
#include <iostream>
#include <string>

void exercise::number2()
{
	using namespace std;

	string first_name;
	string last_name;
	char score;
	int age;

	cout << "영문 퍼스트 네임 (이름) : ";
	getline(cin, first_name);
	cout << "영문 라스트 네임 (성) : ";
	getline(cin, last_name);
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