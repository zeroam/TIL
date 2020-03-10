/* 다형적인 도형 -> 객체 지향 코드
  - 장점 : 기존 함수를 변경하지 않으면서 새 클래스를 추가하기 쉽다.
  - 단점 : 새로운 함수를 추가하기 어렵다. 그러려면 모든 클래스를 고쳐야 한다.
*/
public class Square implements Shape {
    private Point topLeft;
    private double side;

    public double area() {
        return side * side;
    }
}

public class Rectangle implements Shape {
    private Point topLeft;
    private double height;
    private double width;

    public double area() {
        return height * width;
    }
}

public class Circle implements Shape {
    private Point center;
    private double radius;
    public final double PI = 3.141592653589793;

    public double area() {
        return PI * radius * radius;
    }
}