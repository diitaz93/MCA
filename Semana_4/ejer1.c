#include <stdio.h>
#include <time.h>

srand(time(NULL));

int main ()
{
  int ran=rand();
  double r=(double)r/(double)RAND_MAX;
  printf("%.5f",r);
  return 1
}
