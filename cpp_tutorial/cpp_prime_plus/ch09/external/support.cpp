// support.cpp -- �ܺ� ������ ����Ѵ�
// external.cpp�� �������Ѵ�
#include <iostream>
extern double warming;	// �ٸ� ���Ϸκ��� warming;�� ���

// �Լ� ����
void update(double dt);
void local();

using std::cout;

void update(double dt)	// ���� ������ �����Ѵ�
{
	extern double warming;	// ������ �缱��
	warming += dt;		// ���� warming�� ����Ѵ�
	cout << "���� warming�� " << warming;
	cout << "���� ���ŵǾ����ϴ�.\n";
}

void local()	// ���� ������ ����Ѵ�
{
	double warming = 0.8;	// �� ������ �ܺ� ���� warming�� ������

	cout << "���� warming�� " << warming << "�� �Դϴ�.\n";
		// ��� ���� ���� �����ڸ� ����Ͽ�
		// ���� ������ �����Ѵ�
	cout << "�׷���, ���� warming�� " << ::warming;
	cout << "���Դϴ�.\n";
}