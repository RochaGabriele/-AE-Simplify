#include "apro.h"
#include "ui_apro.h"
#include "novtre.h"

apro::apro(QWidget *parent) :
    QDialog(parent),
    ui(new Ui::apro)
{
    ui->setupUi(this);
}

apro::~apro()
{
    delete ui;
}

void apro::on_pushButton_clicked()
{
    close();
    novTre e;
    e.exec();
}
void apro::on_pushButton_2_clicked()
{
    close();
}
