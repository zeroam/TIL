// dowhile.cpp -- Ż�� ���� ����
#include <iostream>
int main()
{
	using namespace std;
	int n;

	cout << "1���� 10������ �� �߿��� ";
	cout << "���� �����ϴ� ���� �ѹ� ���߾� ���ʽÿ�.\n";
	do
	{
		cin >> n;			// ���� ���� ��ü�� �����Ѵ�
	} while (n != 7);		// ���߿� ������ �˻��Ѵ�
	cout << "�¾ҽ��ϴ�. ���� �����ϴ� ���� ��Ű ���� 7�Դϴ�.\n";

	return 0;
}