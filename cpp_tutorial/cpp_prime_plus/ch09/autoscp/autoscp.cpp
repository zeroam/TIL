// autoscp.cpp -- �ڵ� ������ ��� ������ �����Ѵ�
#include <iostream>
void oil(int x);
int main()
{
	using namespace std;

	int texas = 31;
	int year = 2011;
	cout << "main()����, texas = " << texas << ", &texas = ";
	cout << &texas << endl;
	cout << "main()���� year = " << year << ", &year = ";
	cout << &year << endl;
	oil(texas);
	cout << "main()����, texas = " << texas << ", &texas = ";
	cout << &texas << endl;
	cout << "main()����, year = " << year << ", &year = ";
	cout << &year << endl;
	return 0;
}

void oil(int x)
{
	using namespace std;
	int texas = 5;

	cout << "oil()����, texas = " << texas << ", &texas = ";
	cout << &texas << endl;
	cout << "oil()����, x = " << x << ", &x = ";
	cout << &x << endl;
	{
		int texas = 113;
		cout << "��Ͽ���, texas = " << texas;
		cout << ", &texas = " << &texas << endl;
		cout << "��Ͽ���, x = " << x << ", &x = ";
		cout << &x << endl;
	}
	cout << "����� ����� ��, texas = " << texas;
	cout << ", &texas = " << &texas << endl;
}