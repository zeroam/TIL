// twoarg.cpp -- �Ű������� 2�� ����ϴ� �Լ�
#include <iostream>
using namespace std;
void n_chars(char, int);
int main()
{
	int times;
	char ch;

	cout << "���ڸ� �ϳ� �Է��Ͻʽÿ�: ";
	cin >> ch;
	while (ch != 'q')		// �������� q�� �Է��Ѵ�
	{
		cout << "������ �ϳ� �Է��Ͻʽÿ�: ";
		cin >> times;
		n_chars(ch, times);
		cout << "\n����Ϸ��� �ٸ� ���ڸ� �Է��ϰ�, "
			"�������� q�� �����ʽÿ�: ";
		cin >> ch;
	}
	cout << "���� times�� ���� " << times << "�Դϴ�.\n";
	cout << "���α׷��� �����մϴ�.\n";
	return 0;
}

void n_chars(char c, int n)			// c�� n�� ����Ѵ�
{
	while (n-- > 0)
		cout << c;
}