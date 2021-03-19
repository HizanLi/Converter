import sys
import main
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from functools import partial


# python -m PyQt5.uic.pyuic asds.ui -o asds.py


def area_convert(ui):
    Squ_met = 0
    if ui.lineEdit_square_meter.text().isdecimal():
        Squ_met = ui.lineEdit_square_meter.text()
    elif ui.lineEdit_squar_mile.text().isdecimal():
        Squ_met = float(ui.lineEdit_squar_mile.text()) * 2.59e+6
    elif ui.lineEdit_square_yard.text().isdecimal():
        Squ_met = float(ui.lineEdit_square_yard.text()) / 1.196
    elif ui.lineEdit_square_foot.text().isdecimal():
        Squ_met = float(ui.lineEdit_square_foot.text()) / 10.764
    elif ui.lineEdit__square_inch.text().isdecimal():
        Squ_met = float(ui.lineEdit__square_inch.text()) / 1550
    elif ui.lineEdit_hectra.text().isdecimal():
        Squ_met = float(ui.lineEdit_hectra.text()) * 10000
    elif ui.lineEdit_Acre.text().isdecimal():
        Squ_met = float(ui.lineEdit_Acre.text()) * 4047

    ui.lineEdit_square_meter.setText(str(Squ_met))
    ui.lineEdit_squar_mile.setText(str(float(Squ_met) / 2.59e+6))
    ui.lineEdit_square_yard.setText(str(float(Squ_met) * 1.196))
    ui.lineEdit_square_foot.setText(str(float(Squ_met) * 10.7639))
    ui.lineEdit__square_inch.setText(str(float(Squ_met) * 1550))
    ui.lineEdit_hectra.setText(str(float(Squ_met) / 10000))
    ui.lineEdit_Acre.setText(str(float(Squ_met) / 4047))


def area_clean(ui):
    ui.lineEdit_square_meter.setText("")
    ui.lineEdit_squar_mile.setText("")
    ui.lineEdit_square_yard.setText("")
    ui.lineEdit_square_foot.setText("")
    ui.lineEdit__square_inch.setText("")
    ui.lineEdit_hectra.setText("")
    ui.lineEdit_Acre.setText("")


def length_convert(ui):
    met = 0
    if ui.lineEdit_meter.text().isdecimal():
        met = float(ui.lineEdit_meter.text())
    elif ui.lineEdit_yard.text().isdecimal():
        met = float(ui.lineEdit_yard.text()) / 1.094
    elif ui.lineEdit_micrometre.text().isdecimal():
        met = float(ui.lineEdit_micrometre.text()) / 1e+6
    elif ui.lineEdit_mile.text().isdecimal():
        met = float(ui.lineEdit_mile.text()) * 1609.34
    elif ui.lineEdit_nanometre.text().isdecimal():
        met = float(ui.lineEdit_nanometre.text()) / 1e+9
    elif ui.lineEdit_millimeter.text().isdecimal():
        met = float(ui.lineEdit_millimeter.text()) / 1000
    elif ui.lineEdit_centimeter.text().isdecimal():
        met = float(ui.lineEdit_centimeter.text()) / 100
    elif ui.lineEdit_inch.text().isdecimal():
        met = float(ui.lineEdit_inch.text()) / 39.37
    elif ui.lineEdit_foot.text().isdecimal():
        met = float(ui.lineEdit_foot.text()) / 3.281
    ui.lineEdit_meter.setText(str(met))
    ui.lineEdit_yard.setText(str(met*1.094))
    ui.lineEdit_micrometre.setText(str(met*1e+6))
    ui.lineEdit_mile.setText(str(met/1609.34))
    ui.lineEdit_nanometre.setText(str(met*1e+9))
    ui.lineEdit_millimeter.setText(str(met*1000))
    ui.lineEdit_centimeter.setText(str(met*100))
    ui.lineEdit_inch.setText(str(met*39.37))
    ui.lineEdit_foot.setText(str(met*3.281))


def length_clean(ui):
    ui.lineEdit_meter.setText("")
    ui.lineEdit_yard.setText("")
    ui.lineEdit_micrometre.setText("")
    ui.lineEdit_mile.setText("")
    ui.lineEdit_nanometre.setText("")
    ui.lineEdit_millimeter.setText("")
    ui.lineEdit_centimeter.setText("")
    ui.lineEdit_inch.setText("")
    ui.lineEdit_foot.setText("")


def mass_convert(ui):
    kg=0
    if ui.lineEdit_kilogram.text().isdecimal():
        kg = float(ui.lineEdit_kilogram.text())
    elif ui.lineEdit_pound.text().isdecimal():
        kg =float(ui.lineEdit_pound.text())/2.205
    elif ui.lineEdit_gram.text().isdecimal():
        kg = float(ui.lineEdit_gram.text())/1000
    elif ui.lineEdit_imp_ton.text().isdecimal():
        kg = float(ui.lineEdit_imp_ton.text())*1016
    elif ui.lineEdit_us_ton.text().isdecimal():
        kg = float(ui.lineEdit_us_ton.text())*907
    elif ui.lineEdit_tonne.text().isdecimal():
        kg = float(ui.lineEdit_tonne.text())*1000
    elif ui.lineEdit_ounce.text().isdecimal():
        kg = float(ui.lineEdit_ounce.text())/35.274

    ui.lineEdit_kilogram.setText(str(kg))
    ui.lineEdit_pound.setText(str(kg*2.205))
    ui.lineEdit_gram.setText(str(kg*1000))
    ui.lineEdit_imp_ton.setText(str(kg/1016))
    ui.lineEdit_us_ton.setText(str(kg*907))
    ui.lineEdit_tonne.setText(str(kg/1000))
    ui.lineEdit_ounce.setText(str(kg*35.274))


def mass_clean(ui):
    ui.lineEdit_kilogram.setText("")
    ui.lineEdit_pound.setText("")
    ui.lineEdit_gram.setText("")
    ui.lineEdit_imp_ton.setText("")
    ui.lineEdit_tonne.setText("")
    ui.lineEdit_us_ton.setText("")
    ui.lineEdit_ounce.setText("")


def speed_convert(ui):
    time_dict = {
        "second":1,
        "minute":60,
        "hour":3600

    }
    length_dict={
        "Meter":1,
        "Kilometer":1000,
        "Mile":1609.34,
        "Yard":0.9144,
        "Inch":0.0254,
        "Foot":0.3048
    }
    if ui.lineEdit_input_speed.text().isdecimal():
        input_num = float(ui.lineEdit_input_speed.text())
        input_time = time_dict[ui.comboBox_in_time.currentText()]
        input_length = length_dict[ui.comboBox_in_length.currentText()]

        out_time = time_dict[ui.comboBox_out_time.currentText()]
        out_length = length_dict[ui.comboBox_out_length.currentText()]

        out_num = input_num*(input_length/out_length)*(out_time/input_time)
        ui.lineEdit_out_speed.setText(str(out_num))


def speed_clean(ui):
    ui.lineEdit_out_speed.setText("")
    ui.lineEdit_input_speed.setText("")
    print("hrer")


def temperature_convert(ui):
    cel=0
    if ui.lineEdit_celsius.text().isdecimal():
        cel = float(ui.lineEdit_celsius.text())
    elif ui.lineEdit_kelvin.text().isdecimal():
        cel = float(ui.lineEdit_kelvin.text())-273.15
    elif ui.lineEdit_fahrenheit.text().isdecimal():
        cel = (float(ui.lineEdit_fahrenheit.text())-32)*5/9

    ui.lineEdit_celsius.setText(str(cel))
    ui.lineEdit_kelvin.setText(str(cel+273.15))
    ui.lineEdit_fahrenheit.setText(str(cel*9/5+32))


def temperature_clean(ui):
    ui.lineEdit_celsius.setText("")
    ui.lineEdit_kelvin.setText("")
    ui.lineEdit_fahrenheit.setText("")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = QMainWindow()
    ui = main.Ui_MainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()

    ui.pushButton_area.clicked.connect(partial(area_convert, ui))
    ui.pushButton_area_clean.clicked.connect(partial(area_clean, ui))

    ui.pushButton_length.clicked.connect(partial(length_convert,ui))
    ui.pushButton_length_clean.clicked.connect(partial(length_clean,ui))

    ui.pushButton_mass.clicked.connect(partial(mass_convert, ui))
    ui.pushButton_mass_clean.clicked.connect(partial(mass_clean, ui))

    ui.pushButton_speed.clicked.connect(partial(speed_convert, ui))
    ui.pushButton_speed_clean.clicked.connect(partial(speed_clean, ui))

    ui.pushButton_temperature.clicked.connect(partial(temperature_convert, ui))
    ui.pushButton_temperature_clean.clicked.connect(partial(temperature_clean, ui))

    sys.exit(app.exec_())
