#include "08.h"
#include <iostream>

using namespace std;

struct PizzaCompany
{
	char* name = new char[20];
	float radius;
	float weight;
};

void exercise::number8()
{
	PizzaCompany* pa = new PizzaCompany;

	cout << "���� ȸ���� �̸��� �Է��Ͻÿ�: ";
	cin.getline(pa->name, 20);
	cout << "������ ������ �Է��Ͻÿ�: ";
	cin >> pa->radius;
	cout << "������ �߷��� �Է��Ͻÿ�: ";
	cin >> pa->weight;

	cout << "ȸ���̸� : " << pa->name << endl;
	cout << "���� ���� : " << pa->radius << endl;
	cout << "���� �߷� : " << pa->weight << endl;
}