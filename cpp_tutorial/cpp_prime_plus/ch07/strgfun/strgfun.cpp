// strgfun.cpp -- ���ڿ� �Ű������� �Լ�
#include <iostream>
unsigned int c_in_str(const char* str, char ch);
int main()
{
	using namespace std;
	char mmm[15] = "minimum";		// �迭�� ��� �ִ� ���ڿ�

	const char *wail = "ululate";			// wail�� ���ڿ��� �����Ѵ�

	unsigned int ms = c_in_str(mmm, 'm');
	unsigned int us = c_in_str(wail, 'u');
	cout << mmm << "���� m�� " << ms << "�� ����ֽ��ϴ�.\n";
	cout << wail << "���� u�� " << us << "�� ����ֽ��ϴ�.\n";
	return 0;
}

// �� �Լ��� str ���ڿ��� ��� �ִ�
// ch ������ ������ ī��Ʈ �Ѵ�
unsigned int c_in_str(const char* str, char ch)
{
	int count = 0;

	while (*str)
	{
		if (*str == ch)
			count++;
		str++;
	}
	return count;
}