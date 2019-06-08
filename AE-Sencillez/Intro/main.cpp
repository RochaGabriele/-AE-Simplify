#include "entrada.h"
#include <QApplication>

int main(int argc, char *argv[])
{
    QApplication a(argc, argv);
    Entrada w;
    w.show();

    return a.exec();
}
