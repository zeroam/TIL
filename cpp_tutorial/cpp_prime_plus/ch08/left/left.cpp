// left.cpp -- ����Ʈ �Ű������� ����ϴ� ���ڿ� ó�� �Լ�
#include <iostream>
const int ArSize = 80;
char* left(const char* str, int n = 1);
int main()
{
	using namespace std;
	char sample[ArSize];
	cout << "���ڿ��� �Է��Ͻʽÿ�:\n";
	cin.get(sample, ArSize);
	char* ps = left(sample, 4);
	cout << ps << endl;
	delete[] ps;		// �� ���ڿ��� �޸𸮿��� �����Ѵ�
	ps = left(sample);
	cout << ps << endl;
	delete[] ps;		// �� ���ڿ��� �޸𸮿��� �����Ѵ�
	return 0;
}

// �� �Լ��� str ���ڿ��� �տ������� n���� ���ڸ� ���Ͽ�
// ���ο� ���ڿ��� �����ϰ�, �װ��� �����ϴ� �����͸� �����Ѵ�
char* left(const char* str, int n)
{
	if (n < 0)
		n = 0;
	char* p = new char[n + 1];
	int i;
	for (i = 0; i < n && str[i]; i++)
		p[i] = str[i];		// ���ڵ��� �����Ѵ�
	while (i <= n)
		p[i++] = '\0';		// ���ڿ��� �������� '\0'���� �����Ѵ�
	return p;
}
