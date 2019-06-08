#ifndef REPRO_H
#define REPRO_H

#include <QDialog>

namespace Ui {
class repro;
}

class repro : public QDialog
{
    Q_OBJECT

public:
    explicit repro(QWidget *parent = nullptr);
    ~repro();

private slots:
    void on_pushButton_clicked();

    void on_pushButton_2_clicked();

private:
    Ui::repro *ui;
};

#endif // REPRO_H
