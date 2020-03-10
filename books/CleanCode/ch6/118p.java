// 구체적인 Point 클래스
public class Point {
    public double x;
    public double y;
}

// 추상적인 Point 클래스
public interface Point {
    double getX();
    double getY();
    void setCartesian(double x, double y);
    double getR();
    double getTheta();
    void setPolar(double r, double theta);
}

// 구체적인 Vehicle 클래스
public interface Vehicle {
    double getFuelTankCapacityInGallons();
    double getGallonsOfGasoline();
}

// 추상적인 Vehicle 클래스
public interface Vehicle {
    double getPercentFuelRemaining();
}