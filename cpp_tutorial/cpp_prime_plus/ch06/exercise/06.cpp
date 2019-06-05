#include "06.h"
#include <iostream>

namespace num6
{
	void program()
	{
		using namespace std;

		int num;

		cout << "기부할 사람이 몇 명입니까? ";
		while (!(cin >> num) || num < 0)
		{
			cout << "잘못된 입력입니다.\n";
			cout << "기부할 사람이 몇 명입니까? ";
			cin.clear();
			cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
		}

		donator* donas = new donator[num];
		for (int i = 0; i < num; i++)
		{
			cout << "기부자명 : ";
			cin >> donas[i].name;
			cout << "기부금액 : ";
			cin >> donas[i].donation;
		}

		if (num == 0)
		{
			cout << "기부자가 없습니다.\n";
			return;
		}

		int count = 0;
		cout << "고액 기부자\n";
		for (int i = 0; i < num; i++)
		{
			if (donas[i].donation >= 10000)
			{
				cout << "기부자명 : " << donas[i].name << ", 기부금 : " << donas[i].donation << endl;
				count++;
			}
		}
		
		if (count == 0)
			cout << "기부자가 없습니다.\n";

		count = 0;
		cout << "소액 기부자\n";
		for (int i = 0; i < num; i++)
		{
			if (donas[i].donation < 10000)
			{
				cout << "기부자명 : " << donas[i].name << ", 기부금 : " << donas[i].donation << endl;
				count++;
			}
		}

		if (count == 0)
			cout << "기부자가 없습니다.\n";
	}
}
