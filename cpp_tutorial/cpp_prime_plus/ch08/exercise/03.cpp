#include "03.h"
#include <iostream>
#include <string>
#include <locale>

namespace num3
{
	void program()
	{
		using namespace std;

		locale loc;
		string str;
		cout << "���ڿ��� �Է��Ͻʽÿ� (�������� q) : ";
		getline(cin, str);
		while (!cin.fail())
		{
			if (str[0] == 'q')
			{
				break;
			}
			for (size_t i = 0; i < str.length(); i++)
			{
				cout << toupper(str[i], loc);
			}

			cout << endl;
			cout << "���� ���ڿ��� �Է��Ͻÿ� (�������� q) : ";
			getline(cin, str);
		}
		cout << "��";
	}
}