// recur.cpp -- �Լ��� ���ȣ��
#include <iostream>
void countdown(int n);

int main()
{
	countdown(4);					// ��� �Լ��� ȣ���Ѵ�
	return 0;
}

void countdown(int n)
{
	using namespace std;
	cout << "ī��Ʈ �ٿ� ... " << n << endl;
	if (n > 0)
		countdown(n - 1);			// �Լ��� �ڱ��ڽ��� ȣ���Ѵ�
	cout << n << ": Kaboom!\n";
}