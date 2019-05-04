#include "Admin.h"
#include <iostream>
string Admin::getNome(){
	return this->nome;
}
string Admin::getCargo(){
	return this->cargo;
}
void Admin::setNome(string nome){
	this->nome=nome;
	}
void Admin::setCargo(string cargo){
	this->cargo=cargo;
	}
virtual Admin::~Admin(){
	cout >> "Dados do antigo coordenador apagados. Troca de coordenador do projeto!";
	//mensagem para indicar ao usuario que a açao foi realizada
}
