import java.util.Random;



class MyThread extends Thread
{
   static  Random rand= new Random();
    public void run()
    {
        int i=0;
      for(i=0;i<5;i++)
        {
           
            try{
                Thread.sleep(rand.nextInt(2000));

            }catch(InterruptedException e){
                System.out.println(e);
            }
            System.out.println(Thread.currentThread().getName()+"\t"+i);
        }
    }

    public static void main(String[] args)
    {
        MyThread t1 = new MyThread();
        t1.setName("star thread");
        MyThread t2 = new MyThread();
        t2.setPriority(Thread.MAX_PRIORITY);
        MyThread t3 = new MyThread();
        t3.setPriority(8);
        t1.start(); 
        try{  
            // join method waits for 3000 ms for t1 thread to finish after that only t2 and t3 will be started
            t1.join(3000);  
           }catch(Exception e){
               System.out.println(e);
        }
       
        t2.start();
        t3.start();  
        
    }

}