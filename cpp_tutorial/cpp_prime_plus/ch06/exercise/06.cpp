#include "06.h"
#include <iostream>

namespace num6
{
	void program()
	{
		using namespace std;

		int num;

		cout << "����� ����� �� ���Դϱ�? ";
		while (!(cin >> num) || num < 0)
		{
			cout << "�߸��� �Է��Դϴ�.\n";
			cout << "����� ����� �� ���Դϱ�? ";
			cin.clear();
			cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
		}

		donator* donas = new donator[num];
		for (int i = 0; i < num; i++)
		{
			cout << "����ڸ� : ";
			cin >> donas[i].name;
			cout << "��αݾ� : ";
			cin >> donas[i].donation;
		}

		if (num == 0)
		{
			cout << "����ڰ� �����ϴ�.\n";
			return;
		}

		int count = 0;
		cout << "��� �����\n";
		for (int i = 0; i < num; i++)
		{
			if (donas[i].donation >= 10000)
			{
				cout << "����ڸ� : " << donas[i].name << ", ��α� : " << donas[i].donation << endl;
				count++;
			}
		}
		
		if (count == 0)
			cout << "����ڰ� �����ϴ�.\n";

		count = 0;
		cout << "�Ҿ� �����\n";
		for (int i = 0; i < num; i++)
		{
			if (donas[i].donation < 10000)
			{
				cout << "����ڸ� : " << donas[i].name << ", ��α� : " << donas[i].donation << endl;
				count++;
			}
		}

		if (count == 0)
			cout << "����ڰ� �����ϴ�.\n";
	}
}
