#include "07.h"
#include <iostream>

using namespace std;

struct PizzaCompany
{
	char* name = new char[20];
	float radius;
	float weight;
};

void exercise::number7()
{
	PizzaCompany company;
	PizzaCompany* pa = &company;

	cout << "���� ȸ���� �̸��� �Է��Ͻÿ�: ";
	cin.getline(pa->name, 20);
	cout << "������ ������ �Է��Ͻÿ�: ";
	cin >> pa->radius;
	cout << "������ �߷��� �Է��Ͻÿ�: ";
	cin >> pa->weight;

	cout << "ȸ���̸� : " << company.name << endl;
	cout << "���� ���� : " << company.radius << endl;
	cout << "���� �߷� : " << company.weight << endl;
}