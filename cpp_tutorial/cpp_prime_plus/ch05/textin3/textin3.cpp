// textin3.cpp -- ���� ������ ���� �б�
#include <iostream>
int main()
{
	using namespace std;
	char ch;
	int count = 0;
	cin.get(ch);					// ���� �ϳ��� �д´�
	while (cin.fail() == false)		// EOF���� �˻��Ѵ�
	{
		cout << ch;					// ���ڸ� �����Ѵ�
		++count;
		cin.get(ch);				// ���� ���ڸ� �д´�
	}
	cout << count << " ���ڸ� �о����ϴ�.\n";

	return 0;
}