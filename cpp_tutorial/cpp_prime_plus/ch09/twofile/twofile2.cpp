// twofile2.cpp -- �ܺ� ��ũ�� ���� ��ũ�� ������ ����
#include <iostream>
extern int tom;				// tom�� �ٸ� ���Ͽ� ���ǵǾ� �ִ�
static int dick = 10;		// �ܺ� dick�� ���� ������
int harry = 200;			// �ܺ� ������ �����Ѵ�
							// twofile1.cpp�� harry�� �浹���� �ʴ´�

void remote_access()
{
	using namespace std;
	cout << "remote_access()�� �����ϴ� �� ������ �ּ�:\n";
	cout << &tom << " = &tom, " << &dick << " = &dick, ";
	cout << &harry << " = &harry\n";
}