// tempover.cpp -- ���ø� �����ε�
#include <iostream>

template <typename T>				// ���ø� A
void ShowArray(T arr[], int n);

template <typename T>				// ���ø� B
void ShowArray(T* arr[], int n);

struct debts
{
	char name[50];
	double amount;
};

int main()
{
	using namespace std;
	int things[6] = { 13, 31, 103, 301, 310, 130 };
	debts mr_E[3] = 
	{
		{"Ima wolfe", 2400.0},
		{"Ura Foxe", 1300.0},
		{"Iby Stout", 1800.0}
	};
	double* pd[3];

	// �����͵��� �迭 mr_E�� �ִ� ����ü���� amount ����� �����Ѵ�
	for (int i = 0; i < 3; i++)
		pd[i] = &mr_E[i].amount;

	cout << "Mr. E�� ��� ���:\n";
	
	// things�� int���� �迭�̴�
	ShowArray(things, 6);			// ���ø� A�� ����Ѵ�
	cout << "Mr. E�� ä�� ���:\n";

	// pd�� double���� �����ϴ� �����͵��� �迭�̴�
	ShowArray(pd, 3);				// �� Ư��ȭ�� ���ø� B�� ����Ѵ�

	return 0;
}

template <typename T>
void ShowArray(T arr[], int n)
{
	using namespace std;
	cout << "���ø� A\n";
	for (int i = 0; i < n; i++)
		cout << arr[i] << ' ';
	cout << endl;
}

template <typename T>
void ShowArray(T* arr[], int n)
{
	using namespace std;
	cout << "���ø� B\n";
	for (int i = 0; i < n; i++)
		cout << *arr[i] << ' ';
	cout << endl;
}