# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'update_zakaz_tovar.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog_zakaz_tovar(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(391, 228)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_id = QtWidgets.QLabel(self.groupBox)
        self.label_id.setObjectName("label_id")
        self.horizontalLayout.addWidget(self.label_id)
        self.label_id_2 = QtWidgets.QLabel(self.groupBox)
        self.label_id_2.setText("")
        self.label_id_2.setObjectName("label_id_2")
        self.horizontalLayout.addWidget(self.label_id_2)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_id_3 = QtWidgets.QLabel(self.groupBox)
        self.label_id_3.setObjectName("label_id_3")
        self.horizontalLayout_5.addWidget(self.label_id_3)
        self.label_id_4 = QtWidgets.QLabel(self.groupBox)
        self.label_id_4.setText("")
        self.label_id_4.setObjectName("label_id_4")
        self.horizontalLayout_5.addWidget(self.label_id_4)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem1)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_ZakazTovarKolvo = QtWidgets.QLabel(self.groupBox)
        self.label_ZakazTovarKolvo.setObjectName("label_ZakazTovarKolvo")
        self.horizontalLayout_2.addWidget(self.label_ZakazTovarKolvo)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.lineEdit_name = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_name.setObjectName("lineEdit_name")
        self.horizontalLayout_2.addWidget(self.lineEdit_name)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_ZakazTovarPrice = QtWidgets.QLabel(self.groupBox)
        self.label_ZakazTovarPrice.setObjectName("label_ZakazTovarPrice")
        self.horizontalLayout_3.addWidget(self.label_ZakazTovarPrice)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem3)
        self.lineEdit_bdate = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_bdate.setObjectName("lineEdit_bdate")
        self.horizontalLayout_3.addWidget(self.lineEdit_bdate)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.pushButtonProd = QtWidgets.QPushButton(self.groupBox)
        self.pushButtonProd.setObjectName("pushButtonProd")
        self.verticalLayout_2.addWidget(self.pushButtonProd)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem4)
        self.verticalLayout.addWidget(self.groupBox)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.groupBox.setTitle(_translate("Dialog", "Изменение заказ-товар"))
        self.label_id.setText(_translate("Dialog", "id"))
        self.label_id_3.setText(_translate("Dialog", "order_id"))
        self.label_ZakazTovarKolvo.setText(_translate("Dialog", "Количество товаров"))
        self.label_ZakazTovarPrice.setText(_translate("Dialog", "Цена товара"))
        self.pushButtonProd.setText(_translate("Dialog", "Сохранить"))