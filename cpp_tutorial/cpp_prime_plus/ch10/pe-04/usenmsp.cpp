#include "namesp.h"

int main()
{
	using namespace SALES;

	double ar[] = { 3.2, 2.4, 1.1 };
	Sales sales(ar, 3);
	sales.ShowSales();

	Sales sales2;
	sales2.ShowSales();

	return 0;
}