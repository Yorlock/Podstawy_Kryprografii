#include "descriptiondialog.h"
#include "ui_descriptiondialog.h"

descriptionDialog::descriptionDialog(QWidget *parent) :
    QDialog(parent),
    ui(new Ui::descriptionDialog)
{
    ui->setupUi(this);
    setWindowFlags(windowFlags() & ~Qt::WindowContextHelpButtonHint);
}

descriptionDialog::~descriptionDialog()
{
    delete ui;
}
