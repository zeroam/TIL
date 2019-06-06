// waiting.cpp -- clock()�� �ð� ���� ������ ����Ѵ�
#include <iostream>
#include <ctime>		// clock() �Լ��� clock_t���� ���ǵǾ� �ִ�

int main()
{
	using namespace std;
	cout << "���� �ð��� �� ������ �Է��Ͻʽÿ�: ";
	float secs;
	cin >> secs;
	clock_t delay = secs * CLOCKS_PER_SEC;	// ���� �ð��� �ý��� ���� Ŭ�� ���� ��ȯ

	cout << "ī��Ʈ�� �����մϴ�.\a\n";
	clock_t start = clock();
	while (clock() - start < delay)		// �ð��� ����� ������ ���
		;								// ���� �ݷп� ����
	cout << "����\a\n";

	return 0;
}
