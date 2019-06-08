#ifndef DIAVER_H
#define DIAVER_H

#include <QWidget>

namespace Ui {
class diaver;
}

class diaver : public QWidget
{
    Q_OBJECT

public:
    explicit diaver(QWidget *parent = nullptr);
    ~diaver();

private:
    Ui::diaver *ui;
};

#endif // DIAVER_H
