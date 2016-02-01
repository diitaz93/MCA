#include <stdio.h>

#define T_FINAL 5
#define STEP 0.01
#define INITIAL 0.5

double derivative(double t, double y);

int main ()
{
 /* Step */
 double h=STEP;
 /*Initial time*/
 double t=0;
 /*Final Time*/
 double tf=T_FINAL;
 /*Function Value*/
 double y=INITIAL;
 /*Runge Kutta coefficients*/
 double k1,k2,k3,k4;
 /*Header*/
 printf ("Time\tFunction\n");
 /*counter*/
 int i;
 /*Iterations*/
 int iter=tf/h;
 for (i=0;i<=iter;i++)
 {
  printf("%.4f\t%.4f\n",t,y);
  k1=h*derivative(t,y);
  k2=h*derivative(t+h/2.0,y+k1/2.0);
  k3=h*derivative(t+h/2.0,y+k2/2.0);
  k4=h*derivative(t+h,y+k3);
  t=t+h;
  y=y+(k1+2*k2+2*k3+k4)/6.0;
 }

 return 0;
}

/*
Derivative: Returns the value of the derivative evaluated in
the points y and t
*/
double derivative (double t, double y)
{
 double f=y-t*t+1;
 return f;
}
