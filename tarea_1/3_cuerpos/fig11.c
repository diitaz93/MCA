/*Este codigo imprime 4 columnas*/
#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int main ()
{
  long seed;
  int n=400;
  int i;
  seed=n;
  srand48( seed );
  for (i=0;i<n;i++)
    {
      printf("%.4f %.4f %.4f %.4f\n",drand48(),drand48(),drand48(),drand48());
    }
  return 0;
}
