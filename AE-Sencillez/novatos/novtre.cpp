#include "novtre.h"
#include "ui_novtre.h"
#include "media.h"
#include "repro.h"
novTre::novTre(QWidget *parent) :
    QDialog(parent),
    ui(new Ui::novTre)
{
    ui->setupUi(this);
}

novTre::~novTre()
{
    delete ui;
}

void novTre::on_pushButton_clicked()
{
    close();
    repro c;
    c.exec();
}

void novTre::on_pushButton_2_clicked()
{
    close();
    media d;
    d.exec();
}
