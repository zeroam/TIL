#include "08.h"
#include <iostream>
#include <cstring>

void num8::program()
{
	using std::cout;
	using std::cin;
	using std::endl;

	char words[20];
	int count = 0;
	cout << "���� �ܾ���� �Է��Ͻʽÿ� (�������� done�� �Է�) :" << endl;
	
	while (!cin.fail())
	{
		cin >> words;
		if (strcmp(words, "done") == 0)
			break;
		count++;
	}

	cout << "�� " << count << " �ܾ �ԷµǾ����ϴ�.";
}
