#include "stack.h"
#include <iostream>

int main()
{
	using namespace std;
	Stack st;
	char ch;
	Item po;
	cout << "주문서를 추가하려면 A, 주문서를 처리하려면 P,\n"
		<< "종료하려면 Q를 입력하십시오.\n";

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
				cout << "스택이 가득 차 있습니다\n";
			}
			else
			{
				cout << "추가할 주문서의 이름을 입력하십시오: ";
				cin >> po.fullname;
				cout << po.fullname << "의 금액을 입력하십시오: ";
				cin >> po.payment;
				st.push(po);
			}
			break;
		case 'P':
		case 'p':
			if (st.IsEmpty())
			{
				cout << "스택이 비어있습니다";
			}
			else
			{
				st.pop(po);
				cout << "#" << po.fullname << "($" << po.payment << ")"
					<< " 주문서를 처리했습니다.\n";
			}
			break;
			
		}
		cout << "주문서를 추가하려면 A, 주문서를 처리하려면 P,\n"
			<< "종료하려면 Q를 입력하십시오.\n";
	}
	cout << "프로그램을 종료합니다.\n";
	return 0;
}