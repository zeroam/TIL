// stock20.cpp -- ������
#include <iostream>
#include "stock20.h"

// �����ڵ�
Stock::Stock()		// ����Ʈ ������
	: shares(0)
	, share_val(0.0)
	, total_val(0.0)
{
	company = "no name";
}

Stock::Stock(const std::string& co, long n, double pr)
{
	company = co;

	if (n < 0)
	{
		std::cout << "�ֽ� ���� ������ �� �� �����Ƿ�, "
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
Stock::~Stock()		// �� ���� Ŭ���� �ı���
{
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

void Stock::show() const
{
	using std::cout;
	using std::ios_base;
	// ������ #.###�� �����Ѵ�
	ios_base::fmtflags orig =
		cout.setf(ios_base::fixed, ios_base::floatfield);
	std::streamsize prec = cout.precision(3);

	cout << "ȸ���: " << company
		<< " �ֽ� ��: " << shares << '\n';
	cout << " �ְ�: $" << share_val;
	// ������ #.##�� �����Ѵ�
	cout.precision(2);
	cout << " �ֽ� �� ��ġ: $" << total_val << '\n';

	// ���� ������ �����Ѵ�
	cout.setf(orig, ios_base::floatfield);
	cout.precision(prec);
}

const Stock& Stock::topval(const Stock& s) const
{
	if (s.total_val > total_val)
	{
		return s;
	}
	else
	{
		return *this;
	}
}