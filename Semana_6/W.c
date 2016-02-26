#include <stdio.h>
#include <math.h>
#include <stdlib.h>

#define LENGTH 100

double rand_norm(double x, double m, double sig);

int main(void)
{
  double W[LENGTH];
  W[0]=0;
  double dt=0.01;
  double mean=0.0;
  double sigma=1.0;
  int i;
  double x;
  printf("%.4f\n",W[0]);
  for(i=1;i<LENGTH;i++)
    {
      x=2*((double)rand()/(double)RAND_MAX)-1;
      W[i]=W[i-1]+sqrt(dt)*rand_norm(x,mean,sigma);
      printf("%.4f\t%.4f\n",x,W[i]);
    }
  return 0;
}

double rand_norm(double x, double m, double sig)
{
  return 1/(2*M_PI)*exp(-pow(x-m,2)/(2*pow(sig,2)));
  
}
