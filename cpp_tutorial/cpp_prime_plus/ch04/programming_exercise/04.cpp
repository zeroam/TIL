#include "04.h"
#include <iostream>
#include <string>

void exercise::number4()
{
	using namespace std;

	string first_name;
	string last_name;
	string full_name;

	cout << "�۽�Ʈ ���� (�̸�)�� �Է��Ͻÿ�: ";
	getline(cin, first_name);
	cout << "��Ʈ ���� (��)�� �Է��Ͻÿ�: ";
	getline(cin, last_name);

	full_name = last_name + ", " + first_name;
	cout << "�ϳ��� ���ڿ��� �����: " << full_name << endl;
}