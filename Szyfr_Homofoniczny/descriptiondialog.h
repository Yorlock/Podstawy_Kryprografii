#ifndef DESCRIPTIONDIALOG_H
#define DESCRIPTIONDIALOG_H

#include <QDialog>

namespace Ui {
class descriptionDialog;
}

class descriptionDialog : public QDialog
{
    Q_OBJECT

public:
    explicit descriptionDialog(QWidget *parent = nullptr);
    ~descriptionDialog();

private:
    Ui::descriptionDialog *ui;
};

#endif // DESCRIPTIONDIALOG_H
