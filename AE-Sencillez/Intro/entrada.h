#ifndef ENTRADA_H
#define ENTRADA_H

#include <QMainWindow>

namespace Ui {
class Entrada;
}

class Entrada : public QMainWindow
{
    Q_OBJECT

public:
    explicit Entrada(QWidget *parent = nullptr);
    ~Entrada();

private slots:
    void on_pushButton_clicked();

private:
    Ui::Entrada *ui;
};

#endif // ENTRADA_H
