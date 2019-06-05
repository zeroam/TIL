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
		cout << "문자열을 입력하십시오 (끝내려면 q) : ";
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
			cout << "다음 문자열을 입력하시오 (끝내려면 q) : ";
			getline(cin, str);
		}
		cout << "끝";
	}
}