// arrfun3.cpp -- �迭�� ó���ϴ� �Լ��� const
#include <iostream>
const int Max = 5;
// �Լ� ����
int fill_array(double ar[], int limit);
void show_array(const double ar[], int n);		// �����͸� ��ȣ�Ѵ�
void revalue(double r, double ar[], int n);

int main()
{
	using namespace std;
	double properties[Max];

	int size = fill_array(properties, Max);
	show_array(properties, size);
	if (size > 0)
	{
		cout << "�������� �Է��Ͻʽÿ�: ";
		double factor;
		while (!(cin >> factor))	// �߸��� �Է��� ��
		{
			cin.clear();
			while (cin.get() != '\n')
				continue;
			cout << "�߸� �Է��߽��ϴ�, ��ġ�� �Է��ϼ���: ";
		}
		revalue(factor, properties, size);
		show_array(properties, size);
	}
	cout << "���α׷��� �����մϴ�.\n";
	cin.get();
	cin.get();
	return 0;
}

int fill_array(double ar[], int limit)
{
	using namespace std;
	double temp;
	int i;
	for (i = 0; i < limit; i++)
	{
		cout << (i + 1) << "�� �ε����� ����: $";
		cin >> temp;
		if (!cin)
		{
			cin.clear();
			while (cin.get() != '\n')
				continue;
			cout << "�Է� �ҷ�; �Է� ������ �����ڽ��ϴ�.\n";
			break;
		}
		else if (temp < 0)
			break;
		ar[i] = temp;
	}
	return i;
}

// ���� �Լ��� �ּҰ� ar�� �迭��
// ����� ���� ������, ������ ���� ����
void show_array(const double ar[], int n)
{
	using namespace std;
	for (int i = 0; i < n; i++)
	{
		cout << (i + 1) << "�� �ε���: $";
		cout << ar[i] << endl;
	}
}

// ar[]�� �� ���ҿ� ������ r�� ���Ѵ�
void revalue(double r, double ar[], int n)
{
	for (int i = 0; i < n; i++)
		ar[i] *= r;
}