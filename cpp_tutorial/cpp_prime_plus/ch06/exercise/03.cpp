#include "03.h"
#include <iostream>
#include <iomanip>

void num3::program()
{
	using namespace std;
	cout << "���� ���� ���� �߿��� �ϳ��� �����Ͻʽÿ�. (�������� q)" << endl;
	cout << left;
	cout << setw(20) << "c) camera" << "p) pianist\n";
	cout << setw(20) << "t) tree" << "g) game\n";

	char ch;
	while ((ch = cin.get()) != 'q')
	{
		switch (ch)
		{
		case 'c':
			cout << "ī�޶� ���\n";
			break;
		case 'p':
			cout << "�ǾƴϽ�Ʈ ���\n";
			break;
		case 't':
			cout << "���� ���\n";
			break;
		case 'g':
			cout << "���� ���\n";
			break;
		case ' ':
		case '\t':
		case '\n':
			break;
		default:
			cout << "c, p, t, g �߿��� �ϳ��� �����Ͻʽÿ�.(�������� q) : ";
			break;
		}
	}
}
