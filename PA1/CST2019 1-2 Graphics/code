#include <iostream>
using namespace std;

int N, Q;
long long int X[2000000];
long long int Y[2000000];
long long int ANS[2000000];

void swap(long long int* a, long long int* b)
{
    long long int t = *a;
    *a = *b;
    *b = t;
}
int partition (long long int arr[], int low, int high)
{
    int pivot = arr[high];  
    int i = (low - 1);  
    for (int j = low; j <= high - 1; j++)  
    {  
        if (arr[j] < pivot)  
        {  
            i++; 
            swap(&arr[i], &arr[j]);  
        }  
    }  
    swap(&arr[i + 1], &arr[high]);  
    return (i + 1);  
}

void quickSort(long long int arr[], int low, int high)  
{  
    if (low < high)  
    {  
        int pi = partition(arr, low, high);  
        quickSort(arr, low, pi - 1);  
        quickSort(arr, pi + 1, high);  
    }  
}  

int erfen(int l,int r, long long int x, long long int y)
{
    if(l>r) return r;
    int mid=(l+r)/2;
    if(X[mid]*y + x*Y[mid] >= X[mid]*Y[mid]) 
    {
        return erfen(mid+1,r, x, y);
    }
    else 
    {
        return erfen(l,mid-1, x, y);
    }
}

int main()
{
    cin >> N;
    for(int i = 1; i <= N; ++i) scanf("%lld", &X[i]);
    for(int i = 1; i <= N; ++i) scanf("%lld", &Y[i]);
    quickSort(X + 1, 0, N-1);
    quickSort(Y + 1, 0, N-1);

    cin >> Q;
    long long int x, y;
    for(int i = 1; i <= Q; ++i)
    {
        scanf("%lld%lld",&x,&y);
        ANS[i] = erfen(1,N, x, y);     }
    
    for( int i = 1; i <= Q; ++i)
    {
        printf("%d\n", ANS[i]);
    }
}
