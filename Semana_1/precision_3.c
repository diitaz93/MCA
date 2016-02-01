#include <stdio.h>

int main()
{
double a=1e16;
double d1=1e6;
double d2=1e7;
double d3=1e8;
double d4=1e9;

double s1=a+d1;
double s2=a+d2;
double s3=a+d3;
double s4=a+d4;
printf("%.20f\n",a);
printf("%.20f\n",d1);
printf("%.20f\n",s1);
printf("%.20f\n",d2);
printf("%.20f\n",s2);
printf("%.20f\n",d3);
printf("%.20f\n",s3);
printf("%.20f\n",d4);
printf("%.20f\n",s4);
return 0;
}
