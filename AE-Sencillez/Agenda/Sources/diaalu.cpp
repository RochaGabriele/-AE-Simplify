#include "diaalu.h"
#include "ui_diaalu.h"
diaalu::diaalu(QWidget *parent) :
    QDialog(parent),
    ui(new Ui::diaalu)
{
    ui->setupUi(this);
}

diaalu::~diaalu()
{
    delete ui;
}
