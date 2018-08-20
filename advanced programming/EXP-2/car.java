import java.applet.Applet;  
import java.awt.Graphics;  
import javax.swing.*;
import java.awt.*;

public class car extends Applet{  
  
public void paint(Graphics g){  
    g.setColor(Color.white);
    g.fillRect(0, 0, getWidth(), getHeight());


    g.setColor(Color.black);

// drawing the car body
    g.fillRect(100,110, 100, 30);

// drawing the wheels
    g.setColor(Color.red);
    g.fillOval(110, 135, 30, 30);     // left wheel
    g.fillOval(160, 135, 30, 30);     // right wheel

    int x[] = {110, 140, 160, 180};   // coordinate arrays for the 
    int y[] = {110, 90, 90, 110};   //   car cabin

    g.setColor(Color.blue);
    g.fillPolygon(x, y, 4);           // drawing the cabin in blue

    g.setColor(Color.white);
    g.fillRect(141,95,15,10);
}  
  
}  
 