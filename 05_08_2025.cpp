#include<iostream>
#include <locale.h>
using namespacestd;
#include <locale.h>

void nomeFuncao(){
cout<<" \n Teste de acentuação...:é í ó á à â ô";
setlocale(LC_ALL , "Portuguese");
cout<<" \n Teste de acentuação...:é í ó á à â ô";
}

int main (){
nomeFuncao();
return 0;
}
