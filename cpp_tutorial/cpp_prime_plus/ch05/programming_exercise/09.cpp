#include "09.h"
#include <iostream>
#include <string>

void num9::program()
{
	using std::cout;
	using std::cin;
	using std::endl;

	std::string words;
	int count = 0;
	cout << "���� �ܾ���� �Է��Ͻʽÿ� (�������� done�� �Է�) :" << endl;

	while (!cin.fail())
	{
		cin >> words;
		if (words == "done")
			break;
		count++;
	}

	cout << "�� " << count << " �ܾ �ԷµǾ����ϴ�.";
}
