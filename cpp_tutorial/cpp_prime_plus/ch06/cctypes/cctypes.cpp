// cctypes.cpp -- ctype.h ���̺귯�� ���
#include <iostream>
#include <cctype>	// ���� ���� �Լ����� ����
int main()
{
	using namespace std;
	cout << "�м��� �׽�Ʈ�� �Է��Ͻʽÿ�. "
		"�Է��� ���� @���� ǥ���Ͻʽÿ�.\n";

	char ch;
	int whitespace = 0;
	int digits = 0;
	int chars = 0;
	int punct = 0;
	int others = 0;

	cin.get(ch);				// ù ���ڸ� �Է¹޴´�
	while (ch != '@')			// ���� ǥ�� �������� �˻��Ѵ�
	{
		if (isalpha(ch))		// �������ΰ�?
			chars++;
		else if (isspace(ch))	// ȭ��Ʈ �����̽��ΰ�?
			whitespace++;
		else if (isdigit(ch))	// �����ΰ�?
			digits++;
		else if (ispunct(ch))	// �������ΰ�?
			punct++;
		else
			others++;
		cin.get(ch);			// ���� ���ڸ� �Է¹޴´�
	}
	cout << "���ĺ� ���� " << chars << ", "
		<< "ȭ��Ʈ�����̽� " << whitespace << ", "
		<< "���� " << digits << ", "
		<< "������ " << punct << ", "
		<< "��Ÿ " << others << endl;

	return 0;
}