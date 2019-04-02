#include<bits/stdc++.h>

using namespace std;

vector<float> candRaiz(int dep, int ind){
	vector<float> depPosible;
   	vector<float> indPosible;
	vector<float> fin;
	float temp;
	bool existe;
	for(int i = 1; i <= dep/2; i++)
		if(dep%i == 0)
			depPosible.push_back(i);
	depPosible.push_back(dep);
	for(int i = 1; i <= ind/2; i++)
        if(ind%i == 0)
            indPosible.push_back(i);
	indPosible.push_back(ind);
	for(int i = 0; i < indPosible.size(); i++){
		for(int j = 0; j < depPosible.size();j++){
			temp = indPosible[i]/depPosible[j];
			if(find(fin.begin(),fin.end(),temp)==fin.end())
				fin.push_back(temp);
		}
	}
	return fin;
}

int main(){
	vector <int> expresion;
	vector<float> raiz;
	int a= 0;
	expresion.push_back(1);
	expresion.push_back(3);
	expresion.push_back(3);
	expresion.push_back(9);
	raiz = candRaiz(expresion[0],expresion[expresion.size()-1]);
	for(float i:raiz)
		cout << i << ' ';
}
