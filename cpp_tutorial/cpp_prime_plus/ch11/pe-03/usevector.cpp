// randwalk.cpp -- Vector 클래스를 사용한다
#include <iostream>
#include <cstdlib>				// rand(), srand()의 원형
#include <ctime>				// time()의 원형
#include "vect.h"

int main()
{
	using namespace std;
	using VECTOR::Vector;
	srand(time(0));				// 난수 발생기에 씨를 뿌린다
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

	cout << "목표 거리를 입력하십시오(끝내려면 q): ";
	while (cin >> target)
	{
		cout << "보폭을 입력하십시오: ";
		if (!(cin >> dstep))
		{
			break;
		}

		cout << "시도 횟수를 입력하십시오: ";
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

		cout << "최고 걸음 수 : " << maxSteps << endl;
		cout << "최저 걸음 수 : " << minSteps << endl;
		cout << "평균 걸음 수 : " << avrSteps << endl;

		cout << "목표 거리를 입력하십시오(끝내려면 q): ";
	}
	cout << "프로그램을 종료합니다.\n";
	cin.clear();
	while (cin.get() != '\n')
	{
		continue;
	}
	return 0;
}