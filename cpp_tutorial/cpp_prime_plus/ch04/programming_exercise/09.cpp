#include "09.h"
#include <iostream>

using namespace std;

struct CandyBar
{
	char name[20];
	float weight;
	int cal;
};

void print_struct(CandyBar snack);

void exercise::number9()
{
	// 구조체 초기화
	/*
	CandyBar snacks[3] = {
		{ "snack1", 3.12, 20 },
		{ "snack2", 1.2, 10 },
		{ "snack3", 5.243, 40 }
	};
	*/

	// 선언  후 값 대입
	CandyBar* snacks = new CandyBar[3];
	snacks[0] = { "snack1", 3.12, 20 };
	snacks[1] = { "snack2", 1.2, 10 };
	snacks[2] = { "snack3", 5.243, 40 };


	print_struct(snacks[0]);
	print_struct(snacks[1]);
	print_struct(snacks[2]);
}

