#include "Aluno.h"
//getters/acesso
int Aluno::getAtraso(){
	return this->atraso;
}
int Aluno::getAssiduo(){
	return this->assiduo;
}
int Aluno::getOcorrencia(){
	return this->ocorrencia;
}
int Aluno::getPostura(){
	return this->postura;
}
int Aluno::getDesempenho(){
	return this->desempenho;
}
int Aluno::getMatricula(){
	return this->matricula;
}
int Aluno::getDataNasc(){
	return this->dataNasc;
}
int Aluno::getNome(){
	return this->nome;
}
//setters/modificacao
void Aluno::setAtraso(int atraso){
	this->atraso=atraso;
}
void Aluno::setAssiduo(int assiduo){
	this->assiduo=assiduo;

}
void Aluno::setOcorrencia(int ocorrencia){
	this->ocorrencia=ocorrencia;
}
void Aluno::setPostura(int postura){
	this->postura=postura;
}
void Aluno::setDesempenho(int Desempenho){
	this->desempenho=desempenho;
}
void Aluno::setMatricula(int matricula){
	this->matricula=matricula;
}
void Aluno::setDataNasc(string dataNasc){
	this->dataNasc=dataNasc;
}
void Aluno::setNome(string nome){
	this->nome=nome;
}

