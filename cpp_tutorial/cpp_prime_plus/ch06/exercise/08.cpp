#include "08.h"
#include <iostream>
#include <fstream>
#include <string>

void num8::program()
{
	using namespace std;

	ifstream inFile;
	inFile.open("test.txt");
	if (!inFile.is_open())
	{
		cout << "������ ���� �� �����ϴ�.\n���α׷��� �����մϴ�.";
		return;
	}

	char ch;
	int count = -1;
	while (!inFile.eof())
	{
		if (inFile.fail())
		{
			cout << "������ ����ġ�� �Է��� ����Ǿ����ϴ�.\n";
			break;
		}
		count++;
		inFile.get(ch);
	}
	inFile.close();
	cout << "���ڼ��� �� " << count << "�� �Դϴ�.";
}