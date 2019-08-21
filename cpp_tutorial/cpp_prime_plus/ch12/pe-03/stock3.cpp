#include "stock3.h"

Stock::Stock()
	: Stock("")
{
}

Stock::Stock(const char* co, long n, double pr)
{
	company = new char[strlen(co) + 1];
	memcpy(company, co, strlen(co) + 1);

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

Stock::~Stock()
{
	delete[] company;
}

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
	if (num < 0)
	{
		std::cout << "�ŵ� �ֽ� ���� ������ �� �� �����Ƿ�, "
			<< "�ŷ��� ��ҵǾ����ϴ�.\n";
	}
	else if (num > shares)
	{
		std::cout << "���� �ֽĺ��� ���� �ֽ��� �ŵ��� �� �����Ƿ�, "
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


std::ostream& operator<<(std::ostream& os, const Stock& rhs)
{
	using std::ios_base;
	ios_base::fmtflags orig =
		os.setf(ios_base::fixed, ios_base::floatfield);
	std::streamsize prec = os.precision(3);

	os << "ȸ���: " << rhs.company
		<< " �ֽ� ��: " << rhs.shares << '\n';
	os << " �ְ�: $" << rhs.share_val;
	os.precision(2);
	os << " �ֽ� �� ��ġ: $" << rhs.total_val << '\n';

	// ���� ������ �����Ѵ�
	os.setf(orig, ios_base::floatfield);
	os.precision(prec);

	return os;
}