
class Display{
    public void Show()
    {
        System.out.println("this is base class");
    }
}

class DisplayAdapter extends Display
{
    public void Show()
    {
        System.out.println("this is DisplayManager class");
    }
}

class MethodOveriding
{
public static void main(String[] args){
    DisplayAdapter display = new DisplayAdapter();
    display.Show();
}
}