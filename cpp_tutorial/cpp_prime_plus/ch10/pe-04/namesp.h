#pragma once

namespace SALES
{
	class Sales
	{
	public:
		Sales();
		Sales(const double ar[], int n);

		void ShowSales() const;

	private:
		static const int QUARTERS = 4;
		double mSales[QUARTERS];
		double mAverage;
		double mMax;
		double mMin;
	};
}
