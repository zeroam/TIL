#include "03.h"
#include <iostream>
#include <cstring>

void exercise::number3()
{
	using namespace std;

	const int CHAR_NUM = 20;
	const int FULL_SIZE = CHAR_NUM + CHAR_NUM + 2;
	char* first_name = new char[CHAR_NUM];
	char* last_name = new char[CHAR_NUM];
	char* full_name = new char[FULL_SIZE];

	cout << "�۽�Ʈ ���� (�̸�)�� �Է��Ͻÿ�: ";
	cin.getline(first_name, CHAR_NUM);
	cout << "��Ʈ ���� (��)�� �Է��Ͻÿ�: ";
	cin.getline(last_name, CHAR_NUM);

	strcpy_s(full_name, FULL_SIZE, last_name);
	strcat_s(full_name, FULL_SIZE, ", ");
	strcat_s(full_name, FULL_SIZE, first_name);
	cout << "�ϳ��� ���ڿ��� �����: " << full_name << endl;
}