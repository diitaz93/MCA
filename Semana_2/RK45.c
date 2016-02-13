#include <stdio.h>
#include <stdlib.h>
#include <math.h>

#define T_FINAL 2
#define STEP 0.02
#define INITIAL 0.5
#define ERROR 0.001
double derivative (double t, double y);
/*double pow(double x, double y);*/
int main()
{
 /*Step*/
 double h=STEP;
 /*Initial time*/
 double t=0;
 /*Initial Condition*/
 double y=INITIAL; 
 /*Runge Kutta Coeficients*/
 double y1,y2,R,delta,k1,k2,k3,k4,k5,k6;
 /*Header*/
 printf("Time\tFunction\n");
 while (t<T_FINAL)
 {
  k1=h*derivative(t,y);
  k2=h*derivative(t+h/4.0,y+k1/4.0);
  k3=h*derivative(t+3.0*h/8.0,y+3.0*k1/32.0+9.0*k2/32.0);
  k4=h*derivative(t+12.0*h/13.0,y+1932.0*k1/2197.0-7200.0*k2/2197.0+7296.0*k3/2197.0);
  k5=h*derivative(t+h,y+439.0*k1/216.0-8*k2+3680.0*k3/513.0-845.0*k4/4104.0);
  k6=h*derivative(t+h/2.0,y-8.0*k1/27.0+2*k2-3544.0*k3/2565.0+1859.0*k4/4104.0-11.0*k5/40.0);
  y1=y+25.0*k1/216.0+1408.0*k3/2565.0+2197.0*k4/4104.0-k5/5.0;
  y2=y+16.0*k1/135.0+6656.0*k3/12825.0+28561.0*k4/56430.0-9.0*k5/50.0+2.0*k6/55.0;
  R=abs(y2-y1)/h;
  delta=0.84*pow((ERROR/R),0.25);

  if(R<=ERROR)
  {
   y=y1;
   t=t+h;
   printf("%.4f\t%.4f\n",t,y);
  }
  else
  {
   h=delta*h;
  }
 }
 return 0;
}

/* Derivative returns the value of the derivative
evaluated in t and y*/
double derivative(double t, double y)
{
 double f;
 f=y-t*t+1;
 return f;
}
