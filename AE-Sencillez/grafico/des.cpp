#include "des.h"
#include "ui_des.h"
#include <QtWidgets/QApplication>
#include <QtWidgets/QMainWindow>
#include <QtCharts/QChartView>
#include <QtCharts/QBarSeries>
#include <QtCharts/QBarSet>
#include <QtCharts/QLegend>
#include <QtCharts/QBarCategoryAxis>
#include <QtCharts/QValueAxis>
QT_CHARTS_USE_NAMESPACE

des::des(QWidget *parent) :
    QDialog(parent),
    ui(new Ui::des)
{
    ui->setupUi(this);
}

des::~des()
{
    delete ui;
}

void des::on_pushButton_clicked()
{
    QString atraso = ui->comboBox->currentText();
    QString assiduo = ui->comboBox_2->currentText();
    QString ocorrencia = ui->comboBox_3->currentText();
    QString postura = ui->comboBox_4->currentText();
    QString desempenho = ui->comboBox_5->currentText();
    QString serie = ui->comboBox_6->currentText();
    QString mes = ui->comboBox_7->currentText();
    int m;
    m = (atraso.toInt())+(assiduo.toInt())+(ocorrencia.toInt())+(postura.toInt())+(desempenho.toInt());

    if(serie == "1° ano"){
        if(mes == "Fevereiro"){
            prifev = m/5;
        }
        else if (mes == "Março") {
            primar = m/5;
        }
        else if (mes == "Abril") {
            priabr = m/5;
        }
        else if (mes == "Maio") {
            primai = m/5;
        }
        else if (mes == "Junho") {
            prijun = m/5;
        }
        else if (mes == "Agosto") {
            priago = m/5;
        }
        else if (mes == "Setembro") {
            priset = m/5;
        }
        else if (mes == "Outubro") {
            priout = m/5;
        }
        else if (mes == "Novembro") {
            prinov = m/5;
        }
        else if (mes == "Dezembro") {
            pridez = m/5;
        }
    }else if (serie == "2° ano") {
        if(mes == "Fevereiro"){
            segfev = m/5;
        }
        else if (mes == "Março") {
            segmar = m/5;
        }
        else if (mes == "Abril") {
            segabr = m/5;
        }
        else if (mes == "Maio") {
            segmai = m/5;
        }
        else if (mes == "Junho") {
            segjun = m/5;
        }
        else if (mes == "Agosto") {
            segago = m/5;
        }
        else if (mes == "Setembro") {
            segset = m/5;
        }
        else if (mes == "Outubro") {
            segout = m/5;
        }
        else if (mes == "Novembro") {
            segnov = m/5;
        }
        else if (mes == "Dezembro") {
            segdez = m/5;
        }

    }else if (serie == "3° ano") {
        if(mes == "Fevereiro"){
            terfev = m/5;
        }
        else if (mes == "Março") {
            termar = m/5;
        }
        else if (mes == "Abril") {
            terabr = m/5;
        }
        else if (mes == "Maio") {
            termai = m/5;
        }
        else if (mes == "Junho") {
            terjun = m/5;
        }
        else if (mes == "Agosto") {
            terago = m/5;
        }
        else if (mes == "Setembro") {
            terset = m/5;
        }
        else if (mes == "Outubro") {
            terout = m/5;
        }
        else if (mes == "Novembro") {
            ternov = m/5;
        }
        else if (mes == "Dezembro") {
            terdez = m/5;
        }
    }
}
void des::on_pushButton_2_clicked()
{

}
