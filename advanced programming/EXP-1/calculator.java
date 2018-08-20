import java.applet.*;  
import java.awt.*;
import java.awt.event.*;  
public class calculator extends Applet implements ActionListener{  

Button addition,sub,mul,div,enter,clear;
Button b1,b2,b3,b4,b5,b6,b7,b8,b9,b0;
TextField tf;  
TextField tf2;  
TextField tf3;  
static int a=-1,b=-1,res;

public void init()
{
tf = new TextField();
tf.setBounds(50,50,150,20);



tf2 = new TextField();
tf2.setBounds(50,100,150,20);


tf3 = new TextField();
tf3.setBounds(50,150,150,20);
tf3.setEditable(false);

addition = new Button("+");
addition.setBounds(50,200,60,50);

sub = new Button("-");
sub.setBounds(150,200,60,50);

mul = new Button("*");
mul.setBounds(50,250,60,50);

div = new Button("/");
div.setBounds(150,250,60,50);

b0=new Button("0");
b0.setBounds(220,50,20,20);
add(b0);
b0.addActionListener(this);



b1=new Button("1");
b1.setBounds(220,70,20,20);
add(b1);
b1.addActionListener(this);


b2=new Button("2");
b2.setBounds(220,90,20,20);
add(b2);
b2.addActionListener(this);


b3=new Button("3");
b3.setBounds(220,110,20,20);
add(b3);
b3.addActionListener(this);



b4=new Button("4");
b4.setBounds(220,130,20,20);
add(b4);
b4.addActionListener(this);


b5=new Button("5");
b5.setBounds(250,50,20,20);
add(b5);
b5.addActionListener(this);


b6=new Button("6");
b6.setBounds(250,70,20,20);
add(b6);
b6.addActionListener(this);


b7=new Button("7");
b7.setBounds(250,90,20,20);
add(b7);
b7.addActionListener(this);


b8=new Button("8");
b8.setBounds(250,110,20,20);
add(b8);
b8.addActionListener(this);


b9=new Button("9");
b9.setBounds(250,130,20,20);
add(b9);
b9.addActionListener(this);


enter=new Button("enter");
enter.setBounds(270,90,40,40);
add(enter);
enter.addActionListener(this);


clear=new Button("clear");
clear.setBounds(270,140,40,40);
add(clear);
clear.addActionListener(this);


add(addition);add(sub);add(mul);add(div);
add(tf);
add(tf2);
add(tf3);

addition.addActionListener(this);
sub.addActionListener(this);
mul.addActionListener(this);
div.addActionListener(this);

setSize(500,500);
setLayout(null);
setVisible(true);
}


public void actionPerformed(ActionEvent e)
{
String s1=tf.getText();
String s2=tf2.getText();

/*
int a=Integer.parseInt(s1);
int b=Integer.parseInt(s2);
int res=0;

*/

if(e.getSource()==b0)
{
if(b==-1)
{
b=0;
}
else
{
b=b*10;
}

}


if(e.getSource()==b1)
{
if(b==-1)
b=1;
else
b=b*10+1;
}


if(e.getSource()==b2)
{
if(b==-1)
b=2;
else
b=b*10+2;
}


if(e.getSource()==b3)
{
if(b==-1)
b=3;
else
b=b*10+3;
}


if(e.getSource()==b4)
{
if(b==-1)
b=4;
else
b=b*10+4;
}


if(e.getSource()==b5)
{
if(b==-1)
b=5;
else
b=b*10+5;
}


if(e.getSource()==b6)
{
if(b==-1)
b=6;
else
b=b*10+6;
}


if(e.getSource()==b7)
{
if(b==-1)
b=7;
else
b=b*10+7;
}



if(e.getSource()==b8)
{
if(b==-1)
b=8;
else
b=b*10+8;
}


if(e.getSource()==b9)
{
if(b==-1)
b=9;
else
b=b*10+9;
}
if(e.getSource()==addition)
{
res=a+b;
}else if(e.getSource()==sub)
{
res=a-b;
}else if(e.getSource()==mul)
{
res=a*b;
}else if(e.getSource()==div)
{
res=a/b;
}
else if(e.getSource()==enter)
{
if(a==-1)
{
a=b;
b=-1;
}
}
if(a!=-1)
tf.setText(String.valueOf(a));

if(b!=-1)
tf2.setText(String.valueOf(b));



String result = String.valueOf(res);
tf3.setText(result);

if(e.getSource()==clear)
{
a=-1;
b=-1;
res=0;
tf.setText("");
tf2.setText("");
tf3.setText("");
}
}

public static void main(String[] args)
{
new calculator();
}
}	
