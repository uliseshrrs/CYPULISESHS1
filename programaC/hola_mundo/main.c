#include <stdio.h> /*stanaar input */
#include <stdlib.h>

/* run this program using the console pauser or add your own getch, system("pause") or input loop */

int main(int argc, char *argv[]) {
	int x;
	x= 10;
	int y = 20;
	printf("Hola mundo de programacion en C\n");
	printf("Introduce un numero entrero:");
	scanf("%d",&y);
	printf("\t X vale : %d y Y vale :%d\a",x,y);	
	if (y > 10){
		printf("\n%d es mayor que 10",y);
	}
	if ( y <10){
		printf("\n%d es menor que 10",y);
	}
	printf("\n%d Con if -else");
	if (y> 10){
		printf("\n% es mayor que 10",y);	
	}
	else{
		printf("\n%d es mayor que 10",y);
	}
	printf("Algo mas");
	printf("Introduce un valor entero entre 1 y 5:");
	scanf("%d",8x);
	switch(x){
	case 1:
		printf("Hola\n");
		break;
	case 2:
		printf("Adios");
		break;
	case 3:
	    printf("Hello");
	    break;
	case 4:
	printf("bye");
	    break;
	case 5:    
	    printf("Guten tag");
	    break:
	case 6:    	
	printf("Boongiogiorno"):
	    break:	
	default:
		printf("Opsion no valida");
			
		
}
