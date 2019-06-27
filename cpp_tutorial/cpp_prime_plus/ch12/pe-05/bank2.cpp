// bank.cpp -- Queue �������̽��� ����Ѵ�
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

	// �ʿ��� ���������� �غ��Ѵ�
	std::srand(std::time(0));
	cout << "��� ����: ���� ������ ATM\n";
	Queue line;

	int hours = 100;
	// �ùķ��̼��� 1�п� 1�ֱ⸦ �����Ѵ�
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

		// �ùķ��̼��� �����Ѵ�
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

	// �ùķ��̼� ����� ����Ѵ�
	cout << " ť�� ���� �� �� ��: " << customers << endl;
	cout << "�ŷ��� ó���� �� ��: " << served << endl;
	cout << "  �߱��� ���� �� ��: " << turnaways << endl;
	cout << "    ��� ť�� ����: ";
	cout.precision(2);
	cout.setf(ios_base::fixed, ios_base::floatfield);
	cout.setf(ios_base::showpoint);
	cout << (double)sum_line / cyclelimit << endl;
	cout << "    ��� ��� �ð�: "
		<< (double)line_wait / served << "��\n";
	cout << "�ð��� ��� �� ��: " << perhour << endl;
	cout << "�Ϸ�\n";


	return 0;
}

// x�� �� ���� ��� �ð� �����̴�(�� ����)
// �� �ð� ���� ���� �����ϸ� ���ϰ��� true�̴�
bool newcustomer(double x)
{
	return (std::rand() * x / RAND_MAX < 1);
}