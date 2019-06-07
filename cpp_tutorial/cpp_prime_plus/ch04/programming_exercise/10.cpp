#include "10.h"
#include <iostream>
#include <array>

void exercise::number10()
{
	std::array<float, 3> run_result;

	std::cout << "달리기 결과를 입력하시오: ";
	std::cin >> run_result[0];
	std::cout << "달리기 결과를 입력하시오: ";
	std::cin >> run_result[1];
	std::cout << "달리기 결과를 입력하시오: ";
	std::cin >> run_result[2];

	float total = run_result[0] + run_result[1] + run_result[2];
	float mean = total / 3;

	std::cout << "달리기 결과 | "
		<< "  --횟수 : " << 3
		<< "  --평균 : " << mean;
}