// calling.cpp -- �Լ� ����, �Լ� ����, �Լ� ȣ��
#include <iostream>

void simple();		// �Լ� ����

int main()
{
	using namespace std;
	cout << "main()���� simple() �Լ��� ȣ���մϴ�:\n";
	simple();		// �Լ� ȣ��
	cout << "main()�� simple() �Լ��� ����˴ϴ�.\n";
	return 0;
}

// �Լ� ����
void simple()
{
	using namespace std;
	cout << "����� simple() �Լ��Դϴ�.\n";
}