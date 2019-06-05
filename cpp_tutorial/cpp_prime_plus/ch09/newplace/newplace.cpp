// newplace.cpp -- ��ġ ���� new�� ����Ѵ�
#include <iostream>
#include <new>						// ��ġ ���� new�� ����ϱ� ����
const int BUF = 512;
const int N = 5;
char buffer[BUF];					// �޸� chunk
int main()
{
	using namespace std;

	double *pd1, *pd2;
	int i;
	cout << "new�� ��ġ ���� new�� ù ��° ȣ��:\n";
	pd1 = new double[N];			// ���� ����Ѵ�
	pd2 = new (buffer) double[N];	// buffer �迭�� ����Ѵ�
	for (i = 0; i < N; i++)
		pd2[i] = pd1[i] = 1000 + 20.0 * i;
	cout << "�޸� �ּ�:\n" << pd1 << " : ��;    "
		<< (void *)buffer << " : ����" << endl;
	cout << "�޸� ����:\n";
	for (i = 0; i < N; i++)
	{
		cout << &pd1[i] << "�� " << pd1[i] << ";    ";
		cout << &pd2[i] << "�� " << pd2[i] << endl;
	}

	cout << "\nnew�� ��ġ ���� new�� �� ��° ȣ��:\n";
	double *pd3, *pd4;
	pd3 = new double[N];			// ���ο� �ּҸ� ã�Ƽ�
	pd4 = new (buffer) double[N];	// ���� �����͸� �� ���� ����
	for (i = 0; i < N; i++)
		pd4[i] = pd3[i] = 1000 + 40.0 * i;
	cout << "�޸� ����:\n";
	for (i = 0; i < N; i++)
	{
		cout << &pd3[i] << "�� " << pd3[i] << ";    ";
		cout << &pd4[i] << "�� " << pd4[i] << endl;
	}

	cout << "\nnew�� ��ġ ���� new�� �� ��° ȣ��:\n";
	delete[] pd1;
	pd1 = new double[N];
	pd2 = new (buffer + N * sizeof(double)) double[N];
	for (i = 0; i < N; i++)
		pd2[i] = pd1[i] = 1000 + 60.0 * i;
	cout << "�޸� ����:\n";
	for (i = 0; i < N; i++)
	{
		cout << &pd1[i] << "�� " << pd1[i] << ";    ";
		cout << &pd2[i] << "�� " << pd2[i] << endl;
	}
	delete[] pd1;
	delete[] pd3;

	return 0;
}
