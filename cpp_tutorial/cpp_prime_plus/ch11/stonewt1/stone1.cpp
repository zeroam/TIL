// stone1.cpp -- ����� ���� ��ȯ �Լ�
#include <iostream>
#include "stonewt1.h"

int main()
{
	using std::cout;
	Stonewt poppins(9, 2.8);		// 9����, 2.8�Ŀ��
	double p_wt = poppins;			// �Ͻ��� ��ȯ
	//double p_wt = static_cast<double>(poppins);
	cout << "double������ ��ȯ => ";
	cout << "Poppins: " << p_wt << "�Ŀ��\n";
	cout << "int������ ��ȯ => ";
	cout << "Poppins: " << int(poppins) << "�Ŀ��\n";
	//cout << "Poppins: " << static_cast<int>(poppins) << "�Ŀ��\n";

	return 0;
}