#include "10.h"
#include <iostream>
#include <array>

void exercise::number10()
{
	std::array<float, 3> run_result;

	std::cout << "�޸��� ����� �Է��Ͻÿ�: ";
	std::cin >> run_result[0];
	std::cout << "�޸��� ����� �Է��Ͻÿ�: ";
	std::cin >> run_result[1];
	std::cout << "�޸��� ����� �Է��Ͻÿ�: ";
	std::cin >> run_result[2];

	float total = run_result[0] + run_result[1] + run_result[2];
	float mean = total / 3;

	std::cout << "�޸��� ��� | "
		<< "  --Ƚ�� : " << 3
		<< "  --��� : " << mean;
}