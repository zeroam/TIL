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

	cout << "���� �۽�Ʈ ���� (�̸�) : ";
	getline(cin, first_name);
	cout << "���� ��Ʈ ���� (��) : ";
	getline(cin, last_name);
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