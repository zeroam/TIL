// usetime4.cpp -- Time Ŭ������ �� ��° �巡��Ʈ ������ ����Ѵ�
#include <iostream>
#include "mytime3.h"

int main()
{
	using std::cout;
	using std::endl;

	Time aida(3, 35);
	Time tosca(2, 48);
	Time temp;

	cout << "Aida�� Tosca:\n";
	cout << aida << "; " << tosca << endl;
	temp = aida + tosca;			// operator+()
	cout << "Aida + Tosca: " << temp << endl;
	temp = aida * 1.17;				// ��� operator*()
	cout << "Aida * 1.17: " << temp << endl;
	cout << "10 * Tosca: " << 10 * tosca << endl;

	return 0;
}