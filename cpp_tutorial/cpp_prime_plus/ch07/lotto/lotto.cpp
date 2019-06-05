// lotto.cpp -- �·� ���ϱ�
#include <iostream>
long double probability(unsigned numbers, unsigned picks);
int main()
{
	using namespace std;
	unsigned total, choices;
	cout << "��ü ���� ������ ���� ���� ������ �Է��Ͻʽÿ�:\n";
	while ((cin >> total >> choices) && choices <= total)
	{
		cout << "����� �̱� Ȯ���� ";
		cout << probability(total, choices);	// �·��� ����Ѵ�
		cout << "�� �߿��� �� �� �Դϴ�.\n";
		cout << "�ٽ� �� ���� �Է��Ͻʽÿ�. (�������� q�� �Է�): ";
	}
	cout << "���α׷��� �����մϴ�.\n";
	return 0;
}

// �� �Լ��� numbers���� �� �߿���
// picks���� ���� ��Ȯ�ϰ� ���� Ȯ���� ����Ѵ�
long double probability(unsigned numbers, unsigned picks)
{
	long double result = 1.0;			// �� �ڸ����� ���� �������� �´�
	long double n;
	unsigned p;

	for (n = numbers, p = picks; p > 0; n--, p--)
		result = result * n / p;
	return result;
}