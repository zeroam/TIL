// randwalk.cpp -- Vector Ŭ������ ����Ѵ�
#include <iostream>
#include <fstream>
#include <cstdlib>				// rand(), srand()�� ����
#include <ctime>				// time()�� ����
#include "vect.h"

int main()
{
	using namespace std;
	using VECTOR::Vector;
	srand(time(0));				// ���� �߻��⿡ ���� �Ѹ���
	double direction;
	Vector step;
	Vector result(0.0, 0.0);
	unsigned long steps = 0;
	double target;
	double dstep;

	ofstream outfile;
	outfile.open("file.txt");

	cout << "��ǥ �Ÿ��� �Է��Ͻʽÿ�(�������� q): ";
	while (cin >> target)
	{
		cout << "������ �Է��Ͻʽÿ�: ";
		if (!(cin >> dstep))
		{
			break;
		}

		outfile << "��ǥ �Ÿ�: " << target << ", ����: " << dstep << endl;
		outfile << steps << ": " << "(x, y) = " << result << endl;
		while (result.magval() < target)
		{
			direction = rand() % 360;
			step.reset(dstep, direction, Vector::POL);
			result = result + step;
			steps++;
			outfile << steps << ": " << "(x, y) = " << result << endl;
		}
		outfile << steps << " ������ ���� �� ������ ���� ��ġ:\n";
		outfile << result << endl;
		result.polar_mode();
		outfile << " �Ǵ�\n" << result << endl;
		outfile << "������ ��տ��� ��� ��� �Ÿ� = "
			<< result.magval() / steps << endl;
		steps = 0;
		result.reset(0.0, 0.0);
		cout << "��ǥ �Ÿ��� �Է��Ͻʽÿ�(�������� q): ";
	}

	cout << "���α׷��� �����մϴ�.\n";
	cin.clear();
	while (cin.get() != '\n')
	{
		continue;
	}

	outfile.close();

	return 0;
}