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

	cout << "���� �۽�Ʈ ���� (�̸�) : ";
	cin.getline(first_name, CHAR_NUM);
	cout << "���� ��Ʈ ���� (��) : ";
	cin.getline(last_name, CHAR_NUM);
	cout << "�л��� ���ϴ� ����: ";
	cin >> score;
	cout << "����: ";
	cin >> age;

	if (score == 'A' || score == 'B' || score == 'C') {
		score = score + 1;
	}
	else {
		score = 'F';
	}

	cout << "����: " << last_name << ", " << first_name << endl;
	cout << "����: " << score << endl;
	cout << "����: " << age << endl;

}
