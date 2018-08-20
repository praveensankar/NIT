import java.util.Scanner;

class CustomException extends Exception
{
    CustomException()
    {
        System.out.println("This is a custom exception and handled by praveen");
    }
}


class ExceptionHandling
{
    
    public static void test(int a) 
    {
        if(a==5)
        {
            throw new IndexOutOfBoundsException();
        }
    }
   
    public static void StackOverflowExceptionChecker() throws StackOverflowError
    {
      throw new StackOverflowError();
    }
    public static void CustomExceptionChecker() throws CustomException
    {
        throw new CustomException();
    }
    public static void main(String[] args)
    {
        Scanner scanner = new Scanner(System.in);
        int data;
        String str=null;
        int array[]=new int[10];
        String string="test";
        int a=5;
        try{
            data=10/0;
        }
        catch(ArithmeticException e)
        {
            System.out.println(e);
        }
       
        finally
        {
            System.out.println("divide by zero exception is handled perfectly\n");
        }

        try{
           
            str.chars();
        } catch(NullPointerException e)
        {
            System.out.println(e);
        } finally
        {
            System.out.println("null pointer exception is handled perfectly\n");
        }

        try{
           System.out.print("please enter the string to convert it to int : "); 
            str=scanner.next();
            Integer.parseInt(str);
        } catch(NumberFormatException e)
        {
            System.out.println(e);
        } finally
        {
            System.out.println("number format exception is handled perfectly\n");
        }

        try{
            array[20]=20;
        } catch(ArrayIndexOutOfBoundsException e)
        {
            System.out.println(e);
        } finally
        {
            System.out.println("array index out of bound exception is handled perfectly\n");
        }

        try{
            string.charAt(20);
        } catch(StringIndexOutOfBoundsException e)
        {
            System.out.println(e);
        } finally
        {
            System.out.println("string index out of bound exception is handled perfectly\n");
        }

        try{
           test(a);
        }catch(IndexOutOfBoundsException e)
        {
            System.out.println(e+"\n");
        }
        try{
            StackOverflowExceptionChecker();
         }catch(StackOverflowError e)
         {
             System.out.println(e+"\n");
         }

        try{
            CustomExceptionChecker();
         }catch(CustomException e)
         {
             System.out.println("\n");
         }
    }
}