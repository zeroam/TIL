#include "06.h"
#include <iostream>

using namespace std;

struct CandyBar
{
	char name[20];
	float weight;
	int cal;
};

void print_struct(CandyBar snack);

void exercise::number6()
{
	// ����ü �ʱ�ȭ
	/*
	CandyBar snacks[3] = {
		{ "snack1", 3.12, 20 },
		{ "snack2", 1.2, 10 },
		{ "snack3", 5.243, 40 }
	};
	*/

	// ����  �� �� ����
	CandyBar snacks[3];
	snacks[0] = { "snack1", 3.12, 20 };
	snacks[1] = { "snack2", 1.2, 10 };
	snacks[2] = { "snack3", 5.243, 40 };


	print_struct(snacks[0]);
	print_struct(snacks[1]);
	print_struct(snacks[2]);
}

void print_struct(CandyBar snack)
{
	cout << "���� name: " << snack.name
		<< ", weight: " << snack.weight
		<< ", cal: " << snack.cal << endl;
}
