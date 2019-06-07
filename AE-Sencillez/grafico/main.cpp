#include <QtWidgets/QApplication>
#include <QtWidgets/QMainWindow>
#include <QtCharts/QChartView>
#include <QtCharts/QBarSeries>
#include <QtCharts/QBarSet>
#include <QtCharts/QLegend>
#include <QtCharts/QBarCategoryAxis>
#include <QtCharts/QValueAxis>
QT_CHARTS_USE_NAMESPACE
int main(int argc, char *argv[])
{
    int prifev = 0.0;
    int primar = 0.0;
    int priabr = 0.0;
    int primai = 0.0;
    int prijun = 0.0;
    int priago = 0.0;
    int priset = 0.0;
    int priout = 0.0;
    int prinov = 0.0;
    int pridez = 0.0;
    int segfev = 0.0;
    int segmar = 0.0;
    int segabr = 0.0;
    int segmai = 0.0;
    int segjun = 0.0;
    int segago = 0.0;
    int segset = 0.0;
    int segout = 0.0;
    int segnov = 0.0;
    int segdez = 0.0;
    int terfev = 0.0;
    int termar = 0.0;
    int terabr = 0.0;
    int termai = 0.0;
    int terjun = 0.0;
    int terago = 0.0;
    int terset = 0.0;
    int terout = 0.0;
    int ternov = 0.0;
    int terdez = 0.0;

    QApplication a(argc, argv);
    QBarSet *set0 = new QBarSet("1° ano");
    QBarSet *set1 = new QBarSet("2° ano");
    QBarSet *set2 = new QBarSet("3° ano");
    *set0 << prifev << primar << priabr << primai << prijun << priago << priset << priout << prinov << pridez;
    *set1 << segfev << segmar << segabr << segmai << segjun << segago << segset << segout << segnov << segdez;
    *set2 << terfev << termar << terabr << termai << terjun << terago << terset << terout << ternov << terdez;

    QBarSeries *series = new QBarSeries();
    series->append(set0);
    series->append(set1);
    series->append(set2);
    QChart *chart = new QChart();
    chart->addSeries(series);
    chart->setTitle("Seu Desempenho");
    chart->setAnimationOptions(QChart::SeriesAnimations);
    QStringList categories;
    categories << "Fev" << "Mar" << "Abr" << "Mai" << "Jun" << "Ago" << "Set" << "Out" << "Nov" << "Dez";
    QBarCategoryAxis *axisX = new QBarCategoryAxis();
    axisX->append(categories);
    chart->addAxis(axisX, Qt::AlignBottom);
    series->attachAxis(axisX);
    QValueAxis *axisY = new QValueAxis();
    axisY->setRange(0,10);
    chart->addAxis(axisY, Qt::AlignLeft);
    series->attachAxis(axisY);
    chart->legend()->setVisible(true);
    chart->legend()->setAlignment(Qt::AlignBottom);
    QChartView *chartView = new QChartView(chart);
    chartView->setRenderHint(QPainter::Antialiasing);
    QMainWindow window;
    window.setCentralWidget(chartView);
    window.resize(700, 500);
    window.show();
    return a.exec();
}
