// protos.cpp -- �Լ� ������ �Լ� ȣ��
#include <iostream>
void cheers(int);				// �Լ� ���� : ���ϰ��� ����
double cube(double x);			// �Լ� ���� : double���� �����Ѵ�

int main()
{
	using namespace std;
	cheers(5);					// �Լ� ȣ��
	cout << "�ϳ��� ���� �Է��Ͻʽÿ�: ";
	double side;
	cin >> side;
	double volume = cube(side);	// �Լ� ȣ��
	cout << "�� ���� ���̰� " << side << " ��Ƽ������ ������ü�� ���Ǵ� ";
	cout << volume << " ��������Ƽ�����Դϴ�.\n";
	cheers(cube(2));			// ���� ��ȣ�� ���� �۵��Ѵ�
	return 0;
}

void cheers(int n)
{
	using namespace std;
	for (int i = 0; i < n; i++)
		cout << "Cheers! ";
	cout << endl;
}

double cube(double x)
{
	return x * x * x;
}