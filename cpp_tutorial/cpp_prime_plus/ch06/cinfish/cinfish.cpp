// cinfish.cpp -- ���� �ƴ� �Է����� ������ �����Ų��
#include <iostream>
const int Max = 5;
int main()
{
	using namespace std;
	// �����͸� �Է� �޴´�
	double fish[Max];
	cout << "���� ���� ������� ���Ը� �Է����ʽÿ�.\n";
	cout << "������ �ִ� " << Max << "�������� ���� �� �ֽ��ϴ�.\n"
		<< "<�Է��� �������� q�� �����ʽÿ�.>\n";
	cout << "fish #1: ";
	int i = 0;
	while (i < Max && cin >> fish[i])
		if (++i < Max)
			cout << "fish #" << i + 1 << ": ";

	// ����� ����Ѵ�
	double total = 0.0;
	for (int j = 0; j < i; j++)
		total += fish[j];

	// ����� �����Ѵ�
	if (i == 0)
		cout << "����⸦ �� ������ ���� ���ϼ̱���.\n";
	else
		cout << "����� " << i << "������ ��� ���Դ� "
		<< total / i << "�׷��Դϴ�.\n";
	cout << "���α׷��� �����մϴ�.\n";
	return 0;
}