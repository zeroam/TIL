// vect.cpp -- Vector Ŭ������ ���� ���޼���
#include <cmath>
#include "vect.h"	// <iostream>�� ����

using std::sqrt;
using std::sin;
using std::cos;
using std::atan;
using std::atan2;
using std::cout;

namespace VECTOR
{
	// 1 ���� ���� ������ ����Ͽ���(1 ���ȿ� ���� degree ���� ���)
	const double Rad_to_deg = 45.0 / atan(1.0);
	// �ݵ�� �� 57.2957795130823 ���� �Ǿ�� ��

	// private �޼����
	// x���� y������ ũ�⸦ ����Ѵ�
	void Vector::set_mag()
	{
		mag = sqrt(x * x + y * y);
	}

	void Vector::set_ang()
	{
		if (x == 0.0 && y == 0.0)
		{
			ang = 0.0;
		}
		else
		{
			ang = atan2(y, x);
		}
	}

	// �� ��ǥ�� ����Ͽ� x�� �����Ѵ�
	void Vector::set_x()
	{
		x = mag * cos(ang);
	}

	// �� ��ǥ�� ����Ͽ� y�� �����Ѵ�
	void Vector::set_y()
	{
		y = mag * sin(ang);
	}

	// public �޼����
	Vector::Vector()	// ����Ʈ ������
		: x(0.0)
		, y(0.0)
		, mag(0.0)
		, ang(0.0)
	{
		mode = RECT;
	}

	// form�� r�̸� ���� ��ǥ�κ��� ���͸� �����Ѵ�
	// form�� p�̸� �� ��ǥ�κ��� ���͸� �����Ѵ�
	Vector::Vector(double n1, double n2, Mode form)
	{
		mode = form;
		if (form == RECT)
		{
			x = n1;
			y = n2;
			set_mag();
			set_ang();
		}
		else if (form == POL)
		{
			mag = n1;
			ang = n2 / Rad_to_deg;
			set_x();
			set_y();
		}
		else
		{
			cout << "Vector()�� ���޵� ��3�� �Ű������� �߸��Ǿ���.\n";
			cout << "�׷��� ���͸� 0���� �����Ͽ���.\n";
			x = y = mag = ang = 0.0;
			mode = RECT;
		}
	}

	// form�� RECT�̸� ���� ��ǥ�κ��� ���͸� �����Ѵ�(����Ʈ)
	// form�� POL�̸� �� ��ǥ�κ��� ���͸� �����Ѵ�
	void Vector::reset(double n1, double n2, Mode form)
	{
		mode = form;
		if (form == RECT)
		{
			x = n1;
			y = n2;
			set_mag();
			set_ang();
		}
		else if (form == POL)
		{
			mag = n1;
			ang = n2 / Rad_to_deg;
			set_x();
			set_y();
		}
		else
		{
			cout << "Vector()�� ���޵� ��3�� �Ű������� �߸��Ǿ���.\n";
			cout << "�׷��� ���͸� 0���� �����Ͽ���.\n";
			x = y = mag = ang = 0.0;
			mode = RECT;
		}
	}

	Vector::~Vector()		// �ı���
	{
	}

	void Vector::polar_mode()	// �� ��ǥ ���� �����Ѵ�
	{
		mode = POL;
	}

	void Vector::rect_mode()	// ���� ��ǥ ���� �����Ѵ�
	{
		mode = RECT;
	}

	// ������ �����ε�
	// �� Vector ��ü�� ���Ѵ�
	Vector Vector::operator+(const Vector& b) const
	{
		return Vector(x + b.x, y + b.y);
	}

	// Vector ��ü a���� Vector ��ü b�� ����
	Vector Vector::operator-(const Vector& b) const
	{
		return Vector(x - b.x, y - b.y);
	}

	// Vector ��ü�� ��ȣ�� �ٲ۴�
	Vector Vector::operator-() const
	{
		return Vector(-x, -y);
	}

	// Vector ��ü�� n�� ���Ѵ�
	Vector Vector::operator*(double n) const
	{
		return Vector(n * x, n * y);
	}

	// ������ �޼����
	// n�� Vector ��ü a�� ���Ѵ�
	Vector operator*(double n, const Vector& a)
	{
		return a * n;
	}

	// mode�� RECT�̸� ���� ��ǥ�� ����Ѵ�
	// mode�� POL�̸� �� ��ǥ�� ����Ѵ�
	std::ostream& operator<<(std::ostream& os, const Vector& v)
	{
		if (v.mode == Vector::RECT)
		{
			os << "(x,y) = (" << v.x << ", " << v.y << ")";
		}
		else if (v.mode == Vector::POL)
		{
			os << "(m,a) = (" << v.mag << ", " << v.ang * Rad_to_deg << ")";
		}
		else
		{
			os << "Vector ��ü�� ��� ������ Ʋ�Ƚ��ϴ�.\n";
		}
		
		return os;
	}
}