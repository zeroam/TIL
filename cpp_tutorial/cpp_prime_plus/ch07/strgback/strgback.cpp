// strgback.cpp -- char���� �����ϴ� �����͸� �����ϴ� �Լ�
#include <iostream>
char* buildstr(char c, int n);
int main()
{
	using namespace std;
	int times;
	char ch;

	cout << "���ڸ� �ϳ� �Է��Ͻʽÿ�: ";
	cin >> ch;
	cout << "������ �ϳ� �Է��Ͻʽÿ�: ";
	cin >> times;
	char* ps = buildstr(ch, times);
	cout << ps << endl;
	delete[] ps;
	ps = buildstr('+', 20);
	cout << ps << "-DONE-" << ps << endl;
	delete[] ps;

	return 0;
}

// n���� ���� c�� �̷���� ���ڿ��� �����
char* buildstr(char c, int n)
{
	char* pstr = new char[n + 1];
	pstr[n] = '\0';
	while (n-- > 0)
		pstr[n] = c;
	return pstr;
}