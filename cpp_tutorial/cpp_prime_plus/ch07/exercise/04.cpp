#include "04.h"
#include <iostream>
long double probability(unsigned numbers, unsigned picks);
void num4::program()
{
	using namespace std;
	long double result;
	double total, choices;
	cout << "ù��° ���� ������ ���� ���� �Է��Ͻʽÿ�: ";
	cin >> total >> choices;
	result = probability(total, choices);

	cout << "�ι�° ���� ������ ���� ���� �Է��Ͻʽÿ�: ";
	cin >> total >> choices;
	result *= probability(total, choices);

	cout << "����� �̱� Ȯ���� ";
	cout << result << "�� �߿��� �� �� �Դϴ�.\n";
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
