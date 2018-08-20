class Sorting{
    public static void main(String[] args)
    {
        int a[] = {  8,5,6,7,3,2,4,1};
	    int b[] = { 8,5,6,7,3,2,4,1 };
	    int c[] = { 8,5,6,7,3,2,4,1};
	    int d[] = { 8,5,6,7,3,2,4,1 };
        int temp[]=new int[8];
        BubbleSort(a, a.length);
	SelectionSort(b, b.length);
	 InsertionSort(c,c.length);
     System.out.println("\nquick sort");
	
    QuickSort(d, 0,d.length-1,d.length);
}
private  static void BubbleSort(int a[], int n)
{
    System.out.println("\nbubble sort");
	int pass, i,temp, swapped = 1;
	for (pass = n - 1; pass >= 0 && swapped==1; pass--)
	{
		swapped = 0;
		for (i = 0; i < pass; i++)
		{
			if (a[i] > a[i + 1])
			{
				temp = a[i];
				a[i] = a[i + 1];
				a[i + 1] = temp;
				swapped = 1;
			}
		}
        Display(a, n);
	}
	Display(a,n);
}
private static void SelectionSort(int a[], int n)
{
    System.out.println("\nselection sort");
	
	int i, j, min, temp;
	for (i = 0; i < n - 1; i++)
	{
		min = i;
		for (j = i + 1; j < n; j++)
		{
			if (a[j] < a[min])
				min = j;
		}
		temp = a[min];
		a[min] = a[i];
		a[i] = temp;
        Display(a,n);
	}
	Display(a, n);
}

private static void InsertionSort(int a[], int n)
{
    System.out.println("\ninsertion sort");
	
	int i, j, value;
	for (i = 1; i < n ; i++)
	{
		j = i;
		value = a[j];
		while((j>=1)&&(a[j-1] > value))
		{
			a[j] = a[j - 1];
			j--;
		}

		a[j] = value;
        Display(a, n);
    }
	Display(a, n);
}

public static void QuickSort(int A[], int low, int high,int n)
{
	int pivot;
	if (high > low)
	{
		pivot = Partition(A, low, high);
        System.out.println("pivot : "+A[pivot]);
        Display(A,n);
        QuickSort(A, low, pivot - 1,n);
		QuickSort(A, pivot + 1, high,n);
	}
//	if (low == 0 && high == n-1)
		//Display(A, n);
}

public static int Partition(int A[], int low, int high)
{
	int left, right, pivot,temp;
	left = low;
	right = high;
	pivot = A[low];
	while (left <= right)
	{
		if (left <= high && A[left] <= pivot)
			left++;
		if (right >= low && A[right] >= pivot)
			right--;
		if (left < right)
		{
			temp = A[left];
			A[left] = A[right];
			A[right] = temp;
		}
	}
	A[low] = A[right];
	A[right] = pivot;
	return right;
}

private static void Display(int a[],int length)
{
	int i;
    for(i=0;i<length;i++)
    System.out.print(a[i]+" ");
    System.out.print("\n");
}

}