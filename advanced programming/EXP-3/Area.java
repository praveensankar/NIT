import java.util.Scanner;

interface Shape1
{
void Area();
}

interface Shape2
{
void Area();
void Perimeter();
}

interface DisplayManager
{
void Display();
}
 class Square implements Shape1,DisplayManager
{
  int a;
 int area;
  Square(int b)
{
 a=b;
area = 0;
}
  public void Area()
{
  area = a*a;
}

public void Display()
{
System.out.println("area = "+area);
}
}


class Rectangle implements Shape1,Shape2,DisplayManager
{
int length,width;
int area,perimeter;
Rectangle(int l,int w)
{
length=l;
width=w;
area=0;
perimeter=0;
}

public void Area()
{
area=length*width;
}
public void Perimeter()
{
perimeter=2*(length+width);
}

public void Display()
{
System.out.println("area = "+area+"\tPerimeter ="+perimeter);
}


}
public class Area
{

public static void main(String[] args)
{
Scanner scanner = new Scanner(System.in);
int a,l,b;
System.out.print("enter the side value of square : ");
a=scanner.nextInt();
System.out.print("enter the lendth of rectangle : ");
l=scanner.nextInt();
System.out.print("enter the width  of rectangle : ");
b=scanner.nextInt();
Square square = new Square(a);
square.Area();
System.out.println("square a = "+a+"\t");
square.Display();
Rectangle rectangle = new Rectangle(l,b);
rectangle.Area();
rectangle.Perimeter();
System.out.println("rectangle length = "+l+"  width = "+b);rectangle.Display();

}
}
