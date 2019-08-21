#include "stock3.h"

const int STKS = 4;

int main()
{
	// �ʱ�ȭ�� ��ü���� �迭�� �����Ѵ�.
	Stock stocks[STKS] = {
		Stock("NanoSmart", 12, 20.0),
		Stock("Boffo Objects", 200, 2.0),
		Stock("Monolithic Obelisks", 130, 3.25),
		Stock("Fleep Enterprises", 60, 6.5)
	};

	std::cout << "���� �ֽ� ����Ʈ:\n";
	int st;
	for (st = 0; st < STKS; st++)
	{
		std::cout << stocks[st];
	}

	// ù ��° ���ҿ� ������ ����
	const Stock* top = &stocks[0];
	for (st = 1; st < STKS; st++)
	{
		top = &top->topval(stocks[st]);
	}

	// ���� ��ġ �ִ� �ֽ��� �ְ�ġ
	std::cout << "\n�ְ� ��ġ�� �ֽ�:\n";
	std::cout << *top;
	return 0;
}
