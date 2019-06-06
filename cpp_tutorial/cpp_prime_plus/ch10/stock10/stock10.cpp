// stock10.cpp -- �����ڵ�� �ı��ڰ� �߰��� Stock Ŭ���� ����
#include <iostream>
#include "stock10.h"

// �����ڵ� (�޽����� ����ϴ� ����)
Stock::Stock()		// ����Ʈ ������
{
	std::cout << "����Ʈ �����ڰ� ȣ��Ǿ����ϴ�.\n";
	company = "no name";
	shares = 0;
	share_val = 0.0;
	total_val = 0.0;
}

Stock::Stock(const std::string& co, long n, double pr)
{
	std::cout << co << "�� ����ϴ� �����ڰ� ȣ��Ǿ����ϴ�.\n";
	company = co;

	if (n < 0)
	{
		std::cerr << "�ֽ� ���� ������ �� �� �����Ƿ�, "
			<< company << " shares�� 0���� �����մϴ�.\n";
		shares = 0;
	}
	else
	{
		shares = n;
	}
	share_val = pr;
	set_tot();
}

// Ŭ���� �ı���
Stock::~Stock()		// �޽����� ����ϴ� Ŭ���� �ı���
{
	std::cout << "�ȳ�, " << company << "!\n";
}

// �ٸ� �޼����
void Stock::buy(long num, double price)
{
	if (num < 0)
	{
		std::cout << "���� �ֽ� ���� ������ �� �� �����Ƿ�, "
			<< "�ŷ��� ��ҵǾ����ϴ�.\n";
	}
	else
	{
		shares += num;
		share_val = price;
		set_tot();
	}
}

void Stock::sell(long num, double price)
{
	using std::cout;
	if (num < 0)
	{
		cout << "�ŵ� �ֽ� ���� ������ �� �� �����Ƿ�, "
			<< "�ŷ��� ��ҵǾ����ϴ�.\n";
	}
	else if (num > shares)
	{
		cout << "���� �ֽĺ��� ���� �ֽ��� �ŵ��� �� �����Ƿ�, "
			<< "�ŷ��� ��ҵǾ����ϴ�.\n";
	}
	else
	{
		shares -= num;
		share_val = price;
		set_tot();
	}
}

void Stock::update(double price)
{
	share_val = price;
	set_tot();
}

void Stock::show()
{
	using std::cout;
	using std::ios_base;
	// set format to #.###
	ios_base::fmtflags orig =
		cout.setf(ios_base::fixed, ios_base::floatfield);
	std::streamsize prec = cout.precision(3);

	cout << "ȸ���: " << company
		<< " �ֽ� ��: " << shares << '\n';
	cout << " �ְ�: $" << share_val;
	// set format to #.##
	cout.precision(2);
	cout << " �ֽ� �� ����: $" << total_val << '\n';

	// ���� ������ �����Ѵ�
	cout.setf(orig, ios_base::floatfield);
	cout.precision(prec);
}
