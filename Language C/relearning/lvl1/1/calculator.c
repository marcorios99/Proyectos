#include <stdio.h>

int main(void){
    printf("Calculator - Suma, Resta, Division, Multiplicacion\n");
    
    int a;
    int b;

    printf("Introduzca el primer número: ");
    scanf("%d", &a);

    printf("Introduzca el segundo número: ");
    scanf("%d", &b);

    float sum = a + b;
    float resta = a - b;
    float mult = a * b;
    float div = (float)a/b;

    // Para la potencia se debe multiplicar el mismo número la cantidad de veces indicada
    int num_potencia;
    int potencia;
    
    printf("Introduzca el tercer número para elevarlo a la potencia indicada: ");
    scanf("%d", &num_potencia);

    printf("Introduzca la potencia: ");
    scanf("%d", &potencia);

    int r = 1;

    for(int i=0; i < potencia; i++){
        r = r*num_potencia;
    }
    /*
    2³ = 2*2*2
    0,1,2
    base = 2
    potencia = 3
    2*2*2
    */
    
    printf("El resultado de la suma es %.2f \n",sum);
    printf("El resultado de la resta es %.2f \n",resta);
    printf("El resultado de la multiplicacion es %.2f \n",mult);
    printf("El resultado de la division es %.2f \n",div);

    printf("El resultado de la potencia es %d \n",r);
    return 0;

}