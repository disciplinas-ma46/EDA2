#include <stdio.h>
#include<stdlib.h>

void quick_sort(int *V, int inicio, int fim);
int particionar(int *V, int inicio, int fim);
void print_vetor(int *v);

int main(){
  int v[12] = {88,54,1,99, 5, 15, 100,89,63,89,29,61};
  quick_sort(v, 0, 11);
  print_vetor(v);

  return 0;
}

void quick_sort(int *V, int inicio, int fim){
  int pivo;
  if(fim >inicio){
    pivo = particionar(V, inicio, fim);  // separa em dois galho
    quick_sort(V, inicio, pivo - 1 ); // antes do pivo
    quick_sort(V,pivo+1, fim);  // depois do vetor
  }
}

int particionar(int *V, int inicio, int fim){
  int esq, dir, pivo, aux;
  esq = inicio;
  dir = fim;
  pivo = *(V + inicio);

  while( esq < dir ){
    while(V[esq] <= pivo)
      esq++;                //percorre a posição da esquerda ate o pivo vendo se é menor ou igual
    while(V[dir] > pivo)
      dir--;                // vai percorrendo da direita até o pivo vendo se é maio
    if(esq < dir){
      aux = V[esq];
      V[esq] = V[dir];  // troca a posiação com o primeiro que for menor e o primeiro maior depois do pivô
      V[dir] = aux;
    }
  }

  V[inicio] = V[dir];   //o inicio recebe o menor da direita depois dir < esq
  V[dir] = pivo;  // e esse da direita recebe o pivo

  return dir; // o novo pivô

}


void print_vetor(int *v){
  int i = 0;
  for(i = 0; i < 12 ; i++)
    printf("%d ", *(v + i));
  printf("\n");
}
