//Struct Conta com nome do cliente, saldo e número da conta. Crie funções para depositar e sacar.

#include <string>
#include <iomanip>
#include <iostream>
using namespace std;



struct Cliente{
    string nome;
    double saldo;
    int numero;
};
double valor_deposito=0;
double valor_saque=0;
double Depositar(double deposito){
    return valor_deposito+=deposito;
}

double Sacar(double saque){
    return valor_saque-=saque;
}

int main(){
    Cliente cliente;
    cout<<"\n =====================BANCO====================== \n";
    cout<<"Digite seu nome: "; getline(cin,cliente.nome);
    cout<<"Digite seu saldo: "; cin>>cliente.saldo;
    cout<<"Digite o número de sua conta: "; cin>>cliente.numero;
    
    int i;
    cout<<"\nDigite um valor dentre as opções a seguir: \n (1)-SAQUE \n (2)-DEPOSITO \n (3)-SAIR"<<endl;
    cin>>i;
    
    if(i==1){
        cout<<"DIGITE O VALOR A SER SACADO: ";
        cin>>
    }
}
