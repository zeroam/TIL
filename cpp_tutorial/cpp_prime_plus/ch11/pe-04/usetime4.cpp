// usetime4.cpp
#include <iostream>
#include "mytime4.h"

int main()
{
	using std::cout;
	using std::endl;
	Time aida(3, 35);
	Time tosca(2, 48);
	Time temp;

	cout << "Aida¿Í Tosca:\n";
	cout << aida << "; " << tosca << endl;	// operator<<()
	temp = aida + tosca;	// operator+()
	cout << "Aida + tosca: " << temp << endl;
	temp = aida * 1.17;
	cout << "Aida * 1.17: " << temp << endl;
	cout << "10 * Tosca: " << 10 * tosca << endl;

	return 0;
}