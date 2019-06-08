#ifndef NOVDOI_H
#define NOVDOI_H

#include <QDialog>

namespace Ui {
class novDoi;
}

class novDoi : public QDialog
{
    Q_OBJECT

public:
    explicit novDoi(QWidget *parent = nullptr);
    ~novDoi();

private slots:
    void on_pushButton_clicked();

private:
    Ui::novDoi *ui;
};

#endif // NOVDOI_H
