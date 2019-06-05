#include "04.h"
#include <iostream>
long double probability(unsigned numbers, unsigned picks);
void num4::program()
{
	using namespace std;
	long double result;
	double total, choices;
	cout << "첫번째 수의 개수와 뽑을 수를 입력하십시오: ";
	cin >> total >> choices;
	result = probability(total, choices);

	cout << "두번째 수의 개수와 뽑을 수를 입력하십시오: ";
	cin >> total >> choices;
	result *= probability(total, choices);

	cout << "당신이 이길 확률은 ";
	cout << result << "번 중에서 한 번 입니다.\n";
}

long double probability(unsigned numbers, unsigned picks)
{
	long double result = 1.0;
	long double n;
	unsigned p;

	for (n = numbers, p = picks; p > 0; n--, p--)
		result = result * n / p;
	return result;
}
