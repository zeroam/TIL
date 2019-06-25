// sayings1.cpp -- Ȯ�� ������ String Ŭ������ ����Ѵ�
#include <iostream>
#include "string1.h"

const int ArSize = 10;
const int MaxLen = 81;

int main()
{
	using std::cout;
	using std::cin;
	using std::endl;

	String name;
	cout << "�ȳ��Ͻʴϱ�? ������ ��� �ǽʴϱ�?\n";
	cin >> name;

	cout << name << " ��! ������ ���� �Ӵ� " << ArSize
		<< "���� �Է��� �ֽʽÿ�(�������� Enter):\n";

	String sayings[ArSize];		// ��ü���� �迭
	char temp[MaxLen];			// ���ڿ� ������ ���� �ӽ� ����

	int i;
	for (i = 0; i < ArSize; i++)
	{
		cout << i + 1 << ": ";
		cin.get(temp, MaxLen);
		while (cin && cin.get() != '\n')
		{
			continue;
		}
		if (!cin || temp[0] == '\0')	// �Է��� �����߰ų� �� �� �Է��̸�
		{								// i�� ������Ű�� �ʴ´�
			break;
		}
		else
		{
			sayings[i] = temp;			// �����ε� ���� �����ڸ� ����Ѵ�
		}
	}
	int total = i;
	if (total > 0)
	{
		cout << "(������ ���� �Ӵ���� �Է��ϼ̽��ϴ�.)\n";
		for (i = 0; i < total; i++)
		{
			cout << sayings[i][0] << ": " << sayings[i] << endl;
		}

		int shortest = 0;
		int first = 0;
		for (i = 1; i < total; i++)
		{
			if (sayings[i].length() < sayings[shortest].length())
			{
				shortest = i;
			}
			if (sayings[i] < sayings[first])
			{
				first = i;
			}
		}
		cout << "���� ª�� �Ӵ�:\n" << sayings[shortest] << endl;
		cout << "���������� ���� �տ� ������ �Ӵ�:\n" << sayings[first] << endl;

		cout << "�� ���α׷��� " << String::HowMany()
			<< "���� String ��ü�� ����Ͽ����ϴ�. �̻�!\n";
	}
	else
	{
		cout << "�Է� ����! �̻�.\n";
	}

	return 0;
}