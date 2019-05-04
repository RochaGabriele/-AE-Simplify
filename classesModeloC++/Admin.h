#ifndef ADMIN_H_
#define ADMIN_H_
#include <string>
#include "Aluno.h"
using namespace std;
class Admin {
	//privados por padrao
	string nome;
	string cargo;
public:
	virtual ~Admin(); // sera executado caso haja uma troca no coordenador do projeto
	Aluno discente(); // composição necessaria para acessar/modificar os atributos da classe Aluno
	string getNome();
	string getCargo();
	void setNome(string nome);
	void setCargo(string cargo);
};

#endif
