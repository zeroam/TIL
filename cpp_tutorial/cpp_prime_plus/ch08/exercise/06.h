#pragma once

namespace num6
{
	void program();

	template <typename T>
	T maxn(T arr[], int size);

	template<> const char* maxn<const char*>(const char* parr[], int size);
}
