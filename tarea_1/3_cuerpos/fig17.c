#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int main ()
{
  long seed;
  int tg=800;
  int i;
  seed=tg;
  srand48( seed );
  for (i=0;i<tg;i++)
    {
      printf("%.4f %.4f %.4f %.4f %.4f %.4f\n",(double)i*50.0/tg,(double)i,drand48(),drand48(),drand48(),drand48());
    }
  return 0;
}
