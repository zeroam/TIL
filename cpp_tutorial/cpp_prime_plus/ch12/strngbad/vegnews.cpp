// vegnews.cpp -- new�� delete�� Ŭ������ �Բ� ����Ѵ�
#include <iostream>
#include "strngbad.h"

using std::cout;

void callme1(StringBad&);		// ������ �����Ѵ�
void callme2(StringBad);		// ������ �����Ѵ�

int main()
{
	using std::endl;
	{
		cout << "���� ����� �����Ѵ�.\n";
		StringBad headline1("Celery Stalks at Midnight");
		StringBad headline2("Lettuce Prey");
		StringBad sports("Spinach Leaves Bowl for Dollars");
		StringBad sports2 = StringBad(sports);
		cout << "headline1: " << headline1 << endl;
		cout << "headline2: " << headline2 << endl;
		cout << "sports: " << sports << endl;
		callme1(headline1);
		cout << "headline1: " << headline1 << endl;
		callme2(headline2);
		cout << "headline2: " << headline2 << endl;
		cout << "�ϳ��� ��ü�� �ٸ� ��ü�� �ʱ�ȭ:\n";
		StringBad sailor = sports;
		cout << "sailor: " << sailor << endl;
		cout << "�ϳ��� ��ü�� �ٸ� ��ü�� ����:\n";
		StringBad knot;
		knot = headline1;
		cout << "knot: " << knot << endl;
		cout << "�� ����� �������´�.\n";
	}
	cout << "main()�� ��\n";

	return 0;
}

void callme1(StringBad& rsb)
{
	cout << "������ ���޵� StringBad:\n";
	cout << "    \"" << rsb << "\"\n";
}

void callme2(StringBad sb)
{
	cout << "������ ���޵� StringBad:\n";
	cout << "    \"" << sb << "\"\n";
}