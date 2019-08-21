#include "stock3.h"

const int STKS = 4;

int main()
{
	// 초기화된 객체들의 배열을 생성한다.
	Stock stocks[STKS] = {
		Stock("NanoSmart", 12, 20.0),
		Stock("Boffo Objects", 200, 2.0),
		Stock("Monolithic Obelisks", 130, 3.25),
		Stock("Fleep Enterprises", 60, 6.5)
	};

	std::cout << "보유 주식 리스트:\n";
	int st;
	for (st = 0; st < STKS; st++)
	{
		std::cout << stocks[st];
	}

	// 첫 번째 원소에 포인터 지정
	const Stock* top = &stocks[0];
	for (st = 1; st < STKS; st++)
	{
		top = &top->topval(stocks[st]);
	}

	// 가장 가치 있는 주식의 최고치
	std::cout << "\n최고 가치의 주식:\n";
	std::cout << *top;
	return 0;
}
