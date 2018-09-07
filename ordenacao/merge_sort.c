#include<stdio.h>
#include<stdlib.h>
#include <math.h>

void merge_final(int *V,int inicio,int meio,int fim);
void merge_sort(int *V, int inicio, int fim);
void print_vetor(int *v);


int main(){
  int v[12] = {88,54,1,99, 5, 15, 100,89,63,89,29,61};
  merge_sort(v, 0, 11);
  print_vetor(v);

  return 0;
}

void merge_sort(int *V, int inicio, int fim){
  int meio;
  if(inicio < fim){
    meio = floor((inicio + fim)/2);
    printf("meios: %d: %d\n",meio, V[meio]);
    merge_sort(V, inicio, meio);
    merge_sort(V,meio+1, fim);
    merge_final(V, inicio, meio, fim);
  }

  print_vetor(V);
}

void merge_final(int *V,int inicio,int meio,int fim){
    int *temp, p1, p2, tamanho, i, j, k;
    int fim1 = 0, fim2 = 0;
    tamanho = fim - inicio + 1; // definindo tamanho do atual
    p1 = inicio; // ponto1 incial
    p2 = meio + 1;  // ponto 2 final
    temp = (int *) malloc(tamanho*sizeof(int)); // combina num terceiro vetor
    if(temp != NULL){
      for( i = 0; i < tamanho; i++){
        if(!fim1 && !fim2){
          if(V[p1] < V[p2]){
            temp[i] = V[p1];
            p1++;    //verifica quem eh o menor dos dois e coloca na temp
          }
          else{
            temp[i] = V[p2];
            p2++;
          }
          if(p1 > meio) fim1 =1; // se o vetor acabou seta como verdadeiro
          if(p2 > fim) fim2 = 1;
        }
        else{
          if(!fim1)
            temp[i] = V[p1++]; // copia o que sobra
          else
            temp[i] = V[p2++];
        }
      }

      for(j = 0, k = inicio; j < tamanho; j++, k++) //copia os dados do tempo e passa para o V
        V[k] = temp[j];
    }
    free(temp);
}

void print_vetor(int *v){
  int i = 0;
  for(i = 0; i < 12 ; i++)
    printf("%d ", *(v + i));
  printf("\n");
}
