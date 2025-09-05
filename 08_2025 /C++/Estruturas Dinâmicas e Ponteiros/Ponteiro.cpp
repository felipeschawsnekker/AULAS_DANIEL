#include <iostream>
using namespace std;

int main(){
	int x=4; 
	int y=7;
	
	cout<<"Endereço(&x): "<<&x<<"\t x="<<x<<endl;
	cout<<"Endereço(&y): "<<&y<<"\t y="<<y<<endl;
	
	int *px,*py;
	px=&x;
	py=&y;
	
	cout<<"Endereço(px): "<<px<<endl;
	cout<<"Endereço(py): "<<py<<endl;
	cout << "Valor (*px): " << *px << endl;
	cout << "Valor (*py): " << *py << endl;

	
	return 0;
}
