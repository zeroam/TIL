// placenew2.cpp -- new, ��ġ ���� new�� ����Ѵ�(delete ����)
#include <iostream>
#include <string>
#include <new>

using namespace std;

const int BUF = 512;

class JustTesting
{
public:
	JustTesting(const string& s = "Just Testing", int n = 0)
		: words(s)
		, number(n)
	{
		cout << words << " ����\n";
	}
	~JustTesting()
	{
		cout << words << " �ı�\n";
	}
	void Show() const
	{
		cout << words << ", " << number << endl;
	}

private:
	string words;
	int number;
};

int main()
{
	char* buffer = new char[BUF];		// �޸� ����� ��´�

	JustTesting *pc1, *pc2;

	pc1 = new(buffer) JustTesting;		// ��ü�� buffer�� �ִ´�
	pc2 = new JustTesting("Heap1", 20);	// ��ü�� heap�� �ִ´�

	cout << "�޸� ��� �ּ�:\n" << "buffer: "
		<< (void*)buffer << "    heap: " << pc2 << endl;
	cout << "�޸� ����:\n";
	cout << pc1 << ": ";
	pc1->Show();
	cout << pc2 << ": ";
	pc2->Show();

	JustTesting *pc3, *pc4;
	// ��ġ���� new ��ġ ����
	pc3 = new (buffer + sizeof(JustTesting)) JustTesting("Bad Idea", 6);
	pc4 = new JustTesting("Heap2", 10);

	cout << "�޸� ����:\n";
	cout << pc3 << ": ";
	pc3->Show();
	cout << pc4 << ": ";
	pc4->Show();

	delete pc2;				// Heap1 ����
	delete pc4;				// Heap2 ����

	// ��ġ ���� new ��ü���� ��������� �ı��Ѵ�
	pc3->~JustTesting();	// pc3�� �����ϴ� ��ü�� �ı��Ѵ�
	pc1->~JustTesting();	// pc1�� �����ϴ� ��ü�� �ı��Ѵ�
	delete[] buffer;		// buffer ����
	cout << "����\n";
	
	return 0;
}