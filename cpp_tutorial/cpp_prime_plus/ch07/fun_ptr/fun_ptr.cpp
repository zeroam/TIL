// fun_ptr.cpp -- �Լ��� �����ϴ� ������
#include <iostream>
double gildong(int);
double moonsoo(int);

// �� ��° �Ű������� int���� �Ű������� ���ϴ�
// double�� �Լ��� �����ϴ� �����ʹ�
void estimate(int lines, double (*pf)(int));

int main()
{
	using namespace std;
	int code;

	cout << "�ʿ��� �ڵ��� �� ���� �Է��Ͻʽÿ�: ";
	cin >> code;
	cout << "ȫ�浿�� �ð� ����:\n";
	estimate(code, gildong);
	cout << "�ڹ����� �ð� ����:\n";
	estimate(code, moonsoo);
	return 0;
}

double gildong(int lns)
{
	return 0.05 * lns;
}

double moonsoo(int lns)
{
	return 0.03 * lns + 0.0004 * lns * lns;
}

void estimate(int lines, double (*pf) (int))
{
	using namespace std;
	cout << lines << "���� �ۼ��ϴ� �� ";
	cout << (*pf) (lines) << "�ð��� �ɸ��ϴ�.\n";
}