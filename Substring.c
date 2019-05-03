#include<stdio.h>
#include<string.h>

int i,j,m,n,c[20][20];
char string_1[20],string_2[20],b[20][20];

void print(int i,int j)
{
                if(i==0 || j==0)
                                return;
                if(b[i][j]=='c')
                {
                                print(i-1,j-1);
                                printf("%c",string_1[i-1]);
                }
                else if(b[i][j]=='u')
                                print(i-1,j);
                else
                                print(i,j-1);
}

void lcs()
{
                m=strlen(string_1);
                n=strlen(string_2);
                for(i=0;i<=m;i++)
                                c[i][0]=0;
                for(i=0;i<=n;i++)
                                c[0][i]=0;

                
                for(i=1;i<=m;i++)
                                for(j=1;j<=n;j++)
                                {
                                                if(string_1[i-1]==string_2[j-1])
                                                {
                                                                c[i][j]=c[i-1][j-1]+1;
                                                                b[i][j]='c';
                                                }
                                                else if(c[i-1][j]>=c[i][j-1])
                                                {
                                                                c[i][j]=c[i-1][j];
                                                                b[i][j]='u';
                                                }
                                                else
                                                {
                                                                c[i][j]=c[i][j-1];
                                                                b[i][j]='l';
                                                }
                                }
}
int main()
{
                printf("Enter 1st sequence:");
                scanf("%s",string_1);
                printf("Enter 2nd sequence:");
                scanf("%s",string_2);
                printf("\nThe output is ");
                lcs();
                print(m,n);
                printf("\n");
                return 0;


}
