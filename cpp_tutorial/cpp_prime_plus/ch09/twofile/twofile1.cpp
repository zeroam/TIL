// twofile1.cpp -- �ܺ� ��ũ�� ���� ��ũ�� ������ ����
#include <iostream>
int tom = 3;			// �ܺ� ������ ����
int dick = 30;			// �ܺ� ������ ����
static int harry = 300;	// ���� ����, ���� ��ũ

// �Լ� ����
void remote_access();

int main()
{
	using namespace std;
	cout << "main()�� �����ϴ� �� ������ �ּ�:\n";
	cout << &tom << " = &tom, " << &dick << " = &dick, ";
	cout << &harry << " = &harry\n";
	remote_access();
	return 0;
}