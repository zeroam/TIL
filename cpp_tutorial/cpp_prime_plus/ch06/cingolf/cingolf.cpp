// cingolf.cpp -- ���� �ƴ� �Է��� �����Ѵ�
#include <iostream>
const int Max = 5;
int main()
{
	using namespace std;
	// �����͸� �Է¹޴´�.
	int golf[Max];
	cout << "���� ������ �Է��Ͻʽÿ�.\n";
	cout << "�� " << Max << " ���� ������ �Է��ؾ� �մϴ�.\n";
	int i;
	for (i = 0; i < Max; i++)
	{
		cout << "round #" << i + 1 << ": ";
		while (!(cin >> golf[i]))
		{
			cin.clear();		// �Է��� �ʱ�ȭ �Ѵ�
			while (cin.get() != '\n')
				continue;		// �ҷ� �Է��� �����Ѵ�
			cout << "���� ������ �Է��Ͻʽÿ�: ";
		}
	}

	// ����� ����Ѵ�
	double total = 0.0;
	for (i = 0; i < Max; i++)
		total += golf[i];

	// ����� �����Ѵ�
	cout << "�� " << Max << "������ ��� ���� = "
		<< total / Max << endl;

	return 0;
}