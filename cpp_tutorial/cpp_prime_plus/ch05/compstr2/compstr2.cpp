// compstr2.cpp -- string Ŭ������ ����Ͽ� ���ڿ� ��
#include <iostream>
#include <string>

int main()
{
	using namespace std;
	string word = "?ate";
	for (char ch = 'a'; word != "mate"; ch++)
	{
		cout << word << endl;
		word[0] = ch;
	}
	cout << "������ ���� �Ŀ� �ܾ�� " << word << "�Դϴ�.\n";

	return 0;
}