// bank.cpp -- Queue �������̽��� ����Ѵ�
#include <iostream>
#include <cstdlib>		// rand()�� srand()�� ����� ����
#include <ctime>		// time()�� ����ϱ� ����
#include <iomanip>
#include "queue.h"

const int MIN_PER_HR = 60;

bool newcustomer(double x);		// �� ���� �����ߴ°�?

int main()
{
	using std::cin;
	using std::cout;
	using std::endl;
	using std::ios_base;

	// �ʿ��� ���������� �غ��Ѵ�
	std::srand(std::time(0));	// rand()�� ������ �ʱ�ȭ

	cout << "��� ����: ���� ������ ATM\n";
	cout << "ť�� �ִ� ���̸� �Է��Ͻʽÿ�: ";
	int qs;
	cin >> qs;
	Queue line(qs);				// line ť���� �ִ� qs����� ����� �� �ִ�

	cout << "�ùķ��̼� �ð� ���� �Է��Ͻʽÿ�: ";
	int hours;					// �ùķ��̼� �ð� ��
	cin >> hours;
	// �ùķ��̼��� 1�п� 1�ֱ⸦ �����Ѵ�
	long cyclelimit = MIN_PER_HR * hours;	// �ùķ��̼� �ֱ� ��

	cout << "�ð��� ��� �� ���� �Է��Ͻʽÿ�: ";
	double perhour;				// �ð��� ��� �� ��
	cin >> perhour;
	double min_per_cust;		// ��� �� ���� ����(�� ����)
	min_per_cust = MIN_PER_HR / perhour;

	Item temp;					// �� �� ������
	long turnaways = 0;			// ť�� ���� ���� �߱��� ���� �� ��
	long customers = 0;			// ť�� ���� �� �� ��
	long served = 0;			// �ùķ��̼ǿ��� �ŷ��� ó���� �� ��
	long sum_line = 0;			// ť�� ���� ����
	int wait_time = 0;			// ATM�� �� ������ ����ϴ� �ð�
	long line_wait = 0;			// ������ ���� ���� ����� ���� �ð�

	// �ùķ��̼��� �����Ѵ�
	for (int cycle = 0; cycle < cyclelimit; cycle++)
	{
		if (newcustomer(min_per_cust))	// �� ���� �����ߴ�
		{
			if (line.isfull())
			{
				turnaways++;
			}
			else
			{
				customers++;
				temp.set(cycle);		// cycle�� �����ð��� ��
				line.enqueue(temp);		// ť�� �� ���� �߰��Ѵ�
			}
		}
		if (wait_time <= 0 && !line.isempty())
		{
			line.dequeue(temp);		// ���� ���� �޴´�
			wait_time = temp.ptime();	// wait_time�� �����Ѵ�
			line_wait += cycle - temp.when();	// �ش� ���� ���� ���� ����� �ð�
			served++;				// ó���� �� �� ����
		}
		if (wait_time > 0)
		{
			wait_time--;
		}
		sum_line += line.queuecount();	// ť�� ���� ����
	}

	// �ùķ��̼� ����� ����Ѵ�
	if (customers > 0)
	{
		cout << " ť�� ���� �� �� ��:" << customers << endl;
		cout << "�ŷ��� ó���� �� ��: " << served << endl;
		cout << "  �߱��� ���� �� ��: " << turnaways << endl;
		cout << " ��� ť�� ����: ";
		cout << std::setprecision(2);
		cout << std::fixed << std::showpoint;
		cout << (double)sum_line / cyclelimit << endl;
		cout << " ��� ��� �ð�: "
			<< (double)line_wait / served << "��\n";
	}
	else
	{
		cout << "���� �� �� �����ϴ�!\n";
	}
	cout << "�Ϸ�!\n";

	return 0;
}

// x�� �� ���� ��� �ð� �����̴� (�� ����)
// �� �ð� ���� ���� �����ϸ� ���ϰ��� true�̴�
bool newcustomer(double x)
{
	return (std::rand() * x / RAND_MAX < 1);
}