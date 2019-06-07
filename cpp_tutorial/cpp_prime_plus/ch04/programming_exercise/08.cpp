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

	cout << "피자 회사의 이름을 입력하시오: ";
	cin.getline(pa->name, 20);
	cout << "피자의 지름을 입력하시오: ";
	cin >> pa->radius;
	cout << "피자의 중량을 입력하시오: ";
	cin >> pa->weight;

	cout << "회사이름 : " << pa->name << endl;
	cout << "피자 지름 : " << pa->radius << endl;
	cout << "피자 중량 : " << pa->weight << endl;
}