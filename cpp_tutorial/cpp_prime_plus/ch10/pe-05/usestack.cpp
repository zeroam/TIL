#include "stack.h"
#include <iostream>

int main()
{
	using namespace std;
	Stack st;
	char ch;
	Item po;
	cout << "�ֹ����� �߰��Ϸ��� A, �ֹ����� ó���Ϸ��� P,\n"
		<< "�����Ϸ��� Q�� �Է��Ͻʽÿ�.\n";

	while (cin >> ch && toupper(ch) != 'Q')
	{
		while (cin.get() != '\n')
		{
			continue;
		}
		if (!isalpha(ch))
		{
			cout << '\a';
			continue;
		}
		switch (ch)
		{
		case 'A':
		case 'a':
			if (st.IsFull())
			{
				cout << "������ ���� �� �ֽ��ϴ�\n";
			}
			else
			{
				cout << "�߰��� �ֹ����� �̸��� �Է��Ͻʽÿ�: ";
				cin >> po.fullname;
				cout << po.fullname << "�� �ݾ��� �Է��Ͻʽÿ�: ";
				cin >> po.payment;
				st.push(po);
			}
			break;
		case 'P':
		case 'p':
			if (st.IsEmpty())
			{
				cout << "������ ����ֽ��ϴ�";
			}
			else
			{
				st.pop(po);
				cout << "#" << po.fullname << "($" << po.payment << ")"
					<< " �ֹ����� ó���߽��ϴ�.\n";
			}
			break;
			
		}
		cout << "�ֹ����� �߰��Ϸ��� A, �ֹ����� ó���Ϸ��� P,\n"
			<< "�����Ϸ��� Q�� �Է��Ͻʽÿ�.\n";
	}
	cout << "���α׷��� �����մϴ�.\n";
	return 0;
}