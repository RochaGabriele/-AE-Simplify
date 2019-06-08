#include "media.h"
#include "ui_media.h"
#include "repro.h"
#include "apro.h"
media::media(QWidget *parent) :
    QDialog(parent),
    ui(new Ui::media)
{
    ui->setupUi(this);
}

media::~media()
{
    delete ui;
}

void media::on_pushButton_clicked()
{
    QString atraso = ui->comboBox->currentText();
    QString assiduo = ui->comboBox_2->currentText();
    QString ocorrencia = ui->comboBox_3->currentText();
    QString postura = ui->comboBox_4->currentText();
    QString desempenho = ui->comboBox_5->currentText();
    int m;
    m = (atraso.toInt())+(assiduo.toInt())+(ocorrencia.toInt())+(postura.toInt())+(desempenho.toInt());
    if(m<35){
        close();
        repro g;
        g.exec();
    }else {
        close();
        apro h;
        h.exec();
    }
}
