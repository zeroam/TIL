// bank.cpp -- Queue 인터페이스를 사용한다
#include <iostream>
#include <cstdlib>
#include <ctime>
#include "queue.h"

const int MIN_PER_HR = 60;

bool newcustomer(double x);

int main()
{
	using std::cin;
	using std::cout;
	using std::endl;
	using std::ios_base;

	// 필요하 여러가지를 준비한다
	std::srand(std::time(0));
	cout << "사례 연구: 히서 은행의 ATM\n";
	Queue line;

	int hours = 100;
	// 시뮬레이션은 1분에 1주기를 실행한다
	long cyclelimit = MIN_PER_HR * hours;

	Item temp;
	long turnaways;
	long customers;
	long served;
	long sum_line;
	int wait_time;
	long line_wait;

	double perhour = 0;
	while (true)
	{
		perhour++;
		double min_per_cust;
		min_per_cust = MIN_PER_HR / perhour;
		
		turnaways = 0;
		customers = 0;
		served = 0;
		sum_line = 0;
		wait_time = 0;
		line_wait = 0;

		// 시뮬레이션을 실행한다
		for (int cycle = 0; cycle < cyclelimit; cycle++)
		{
			if (newcustomer(min_per_cust))
			{
				if (line.isfull())
				{
					turnaways++;
				}
				else
				{
					customers++;
					temp.set(cycle);
					line.enqueue(temp);
				}
			}
			if (wait_time <= 0 && !line.isempty())
			{
				line.dequeue(temp);
				wait_time = temp.ptime();
				line_wait += cycle - temp.when();
				served++;
			}
			if (wait_time > 0)
			{
				wait_time--;
			}
			sum_line += line.queuecount();
		}




		if ((double)line_wait / served >= 1)
		{
			break;
		}
	}

	// 시뮬레이션 결과를 출력한다
	cout << " 큐에 줄을 선 고객 수: " << customers << endl;
	cout << "거래를 처리한 고객 수: " << served << endl;
	cout << "  발길을 돌린 고객 수: " << turnaways << endl;
	cout << "    평균 큐의 길이: ";
	cout.precision(2);
	cout.setf(ios_base::fixed, ios_base::floatfield);
	cout.setf(ios_base::showpoint);
	cout << (double)sum_line / cyclelimit << endl;
	cout << "    평균 대기 시간: "
		<< (double)line_wait / served << "분\n";
	cout << "시간당 평균 고객 수: " << perhour << endl;
	cout << "완료\n";


	return 0;
}

// x는 고객 간의 평균 시간 간격이다(분 단위)
// 이 시간 내에 고객이 도착하면 리턴값은 true이다
bool newcustomer(double x)
{
	return (std::rand() * x / RAND_MAX < 1);
}