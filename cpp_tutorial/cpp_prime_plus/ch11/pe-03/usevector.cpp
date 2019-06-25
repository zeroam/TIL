// randwalk.cpp -- Vector Ŭ������ ����Ѵ�
#include <iostream>
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
	unsigned int n;
	double target;
	double dstep;
	
	unsigned long maxSteps;
	unsigned long minSteps;
	double avrSteps = 0;

	cout << "��ǥ �Ÿ��� �Է��Ͻʽÿ�(�������� q): ";
	while (cin >> target)
	{
		cout << "������ �Է��Ͻʽÿ�: ";
		if (!(cin >> dstep))
		{
			break;
		}

		cout << "�õ� Ƚ���� �Է��Ͻʽÿ�: ";
		if (!(cin >> n))
		{
			break;
		}
		
		unsigned int i;
		for (i = 0; i < n; i++)
		{
			while (result.magval() < target)
			{
				direction = rand() % 360;
				step.reset(dstep, direction, Vector::POL);
				result = result + step;
				steps++;
			}
			
			if (i == 0)
			{
				maxSteps = steps;
				minSteps = steps;
			}
			else
			{
				if (maxSteps < steps)
				{
					maxSteps = steps;
				}
				
				if (minSteps > steps)
				{
					minSteps = steps;
				}
			}

			avrSteps += steps;

			steps = 0;
			result.reset(0.0, 0.0);
		}
		avrSteps = static_cast<double>(avrSteps) / i;

		cout << "�ְ� ���� �� : " << maxSteps << endl;
		cout << "���� ���� �� : " << minSteps << endl;
		cout << "��� ���� �� : " << avrSteps << endl;

		cout << "��ǥ �Ÿ��� �Է��Ͻʽÿ�(�������� q): ";
	}
	cout << "���α׷��� �����մϴ�.\n";
	cin.clear();
	while (cin.get() != '\n')
	{
		continue;
	}
	return 0;
}