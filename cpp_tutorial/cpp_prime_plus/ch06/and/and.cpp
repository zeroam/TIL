// and.cpp -- ���� ������
#include <iostream>
const int ArSize = 6;
int main()
{
	using namespace std;
	float naaq[ArSize];		// NAAQ; New Age Awareness Quotients
	cout << "������� �������� �ڰ� ���� (NAAQ)�� �Է��Ͻʽÿ�.\n"
		<< ArSize << "���� �����͸� ��� �Է��߰ų�, ������ �Է��ϸ�\n"
		<< "while ������ Ż���մϴ�.\n";

	int i = 0;
	float temp;
	cout << "ù ��° ��: ";
	cin >> temp;
	while (i < ArSize && temp >= 0)		// �� ���� Ż������
	{
		naaq[i] = temp;
		++i;
		if (i < ArSize)					// �迭�� ������ ������ ���� ������
		{
			cout << "�� ���� ��: ";
			cin >> temp;				// ���� ���� �Է� �޴´�
		}
	}
	if (i == 0)
		cout << "�Է��� �����Ͱ� �����Ƿ� ���α׷��� �����մϴ�.\n";
	else
	{
		cout << "����� NAAQ�� �Է����ʽÿ�: ";
		float you;
		cin >> you;
		int count = 0;
		for (int j = 0; j < i; j++)
			if (naaq[j] > you)
				++count;
		cout << "����� �߿��� " << count;
		cout << "���� ��ź��� NAAQ�� �����ϴ�.\n";
	}

	return 0;
}