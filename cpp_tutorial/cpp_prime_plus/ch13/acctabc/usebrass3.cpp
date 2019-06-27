// usebrass3.cpp -- �߻��� ���� Ŭ������ ����ϴ� �پ��� �ܰ��� ���
#include <iostream>
#include <string>
#include "acctabc.h"

const int CLIENTS = 4;

int main()
{
	using std::cin;
	using std::cout;
	using std::endl;

	AcctABC* p_clients[CLIENTS];
	std::string temp;
	long tempnum;
	double tempbal;
	char kind;

	for (int i = 0; i < CLIENTS; i++)
	{
		cout << "���� �̸��� �Է��Ѵ�: ";
		getline(cin, temp);
		cout << "���� ������� ��ȣ�� �Է��Ѵ�: ";
		cin >> tempnum;
		cout << "���� ������ �Է��Ѵ�: $";
		cin >> tempbal;
		cout << "Brass ���¿� 1���� �Է��Ѵ�. �Ǵ�,"
			<< "BrassPlus ���¿� 2���� �Է��Ѵ� ";

		while (cin >> kind && (kind != '1' && kind != '2'))
		{
			cout << "1 �Ǵ� 2�� �Է��Ѵ�:";
		}
		if (kind == '1')
		{
			p_clients[i] = new Brass(temp, tempnum, tempbal);
		}
		else
		{
			double tmax, trate;
			cout << "���´�� �Ѱ踦 �Է��Ѵ�: $";
			cin >> tmax;
			cout << "�������� �Է��Ѵ�"
				<< "�Ҽ����� ����Ѵ�:";
			cin >> trate;
			p_clients[i] = new BrassPlus(temp, tempnum, tempbal, tmax, trate);
		}
		while (cin.get() != '\n')
		{
			continue;
		}
	}
	cout << endl;

	for (int i = 0; i < CLIENTS; i++)
	{
		p_clients[i]->ViewAcct();
		cout << endl;
	}

	for (int i = 0; i < CLIENTS; i++)
	{
		delete p_clients[i];		// ���� �޸�
	}
	cout << "���α׷��� �����մϴ�.\n";

	return 0;
}