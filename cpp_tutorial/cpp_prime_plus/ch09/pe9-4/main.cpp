#include "sales.h"

int main()
{
	SALES::Sales sales;

	double ar[] = { 3.2, 2.4, 1.1 };
	SALES::setSales(sales, ar, 3);
	SALES::showSales(sales);

	SALES::setSales(sales);
	SALES::showSales(sales);

	return 0;
}