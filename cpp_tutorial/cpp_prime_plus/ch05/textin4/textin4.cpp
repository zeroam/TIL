// textin4.cpp -- cin.get()���� ���� �б�
#include <iostream>

int main()
{
	using namespace std;
	char ch;					// char���� �ƴ϶� int���̾�� �Ѵ� -> char ���� ����
	int count = 0;

	while ((ch = cin.get()) != EOF)	// ���� �� �˻�
	{
		cout.put(char(ch));
		++count;
	}
	cout << count << " ���ڸ� �о����ϴ�.\n";

	return 0;
}