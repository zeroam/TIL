// cubes.cpp -- �Ϲ� �Ű������� ���� �Ű�����
#include <iostream>
double cube(double a);
double refcube(double& ra);
int main()
{
	using namespace std;
	double x = 3.0;

	cout << cube(x);
	cout << " = " << x << "�� ������\n";
	cout << refcube(x);
	cout << " = " << x << "�� ������\n";

	return 0;
}

double cube(double a)
{
	a *= a * a;
	return a;
}

double refcube(double& ra)
{
	ra *= ra * ra;
	return ra;
}