nclude <stdio.h>
#include <stdlib.h>
int main()
{
    int row;
    int col ;
    scanf ("%d %d",&row,&col);
    int *vis = malloc(100000 * sizeof(int));
    int *arr = (int *)malloc(row * col * sizeof(int));
    int *arr2 = (int *)malloc(row * col * sizeof(int));
    int i, j;
    for (i = 0; i < row; i++)
        for (j = 0; j < col; j++)
        {
            scanf("%d",&*(arr + i*col + j));
 
        }
 
    printf("The Duplicate Values are:-\n");
    for (i = 0; i < row; i++)
    {
        for (j = 0; j < col; j++)
        {
 
            int x =*(arr + i*col + j);
            *(arr2+i*col+j) = x;
 
        }
 
    }
    for (int i=0 ;i<row ;i++){
        for (int j =0 ;j<col ; j++){
            int x= *(arr+i*col+ j);
            if (vis[x]) continue;
            vis[x]=1;
            printf("%d in positions {",x);
            for (int l=0 ;l<row ; l++){
                for (int k =0 ; k<col ; k++){
                    int tmp = *(arr2+l*col+ k);
                    if (tmp==x){
                        printf ("(%d , %d) ",l+1,k+1 );
                    }
                }
            }
            printf ("}\n");
        }
    }
    free(arr);
    free(arr2);
    free(vis);
    return 0;
}
