#include "mainwindow.h"
#include "ui_mainwindow.h"
#include <QMessageBox>

extern "C" {
#include "sbus.h"
}

MainWindow::MainWindow(QWidget *parent)
    : QMainWindow(parent)
    , ui(new Ui::MainWindow)
{
    ui->setupUi(this);

    serialPort.setPortName("COM8");
    if(!serialPort.open(QIODevice::ReadOnly)) {
        QMessageBox::critical(this, "Error", "Serial port open failed!");
        exit(0);
    }

    serialPort.setBaudRate(100000);
    serialPort.setDataBits(QSerialPort::Data8);
    serialPort.setParity(QSerialPort::EvenParity);
    serialPort.setStopBits(QSerialPort::TwoStop);
    serialPort.setFlowControl(QSerialPort::NoFlowControl);

    connect(&serialPort, &QSerialPort::readyRead, this, &MainWindow::dataRead);
}

MainWindow::~MainWindow()
{
    delete ui;
}

extern int32_t channelData[];
extern uint8_t loseFlag;
extern uint8_t dataFlag;

void MainWindow::dataRead()
{
    QByteArray data = serialPort.readAll();

    sbusDataHandler((uint8_t*)data.data(), data.size());

    ui->channel1SpinBox->setValue(channelData[0]);
    ui->channel2SpinBox->setValue(channelData[1]);
    ui->channel3SpinBox->setValue(channelData[2]);
    ui->channel4SpinBox->setValue(channelData[3]);
    ui->channel5SpinBox->setValue(channelData[4]);
    ui->channel6SpinBox->setValue(channelData[5]);
    ui->channel7SpinBox->setValue(channelData[6]);
    ui->loseFlagCheckBox->setChecked(loseFlag);
    ui->dataFlagCheckBox->setChecked(dataFlag);
}

