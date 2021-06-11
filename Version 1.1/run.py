import sys
from decimal import *
from functools import partial

from PyQt5.QtWidgets import QApplication, QMainWindow
import main


# python -m PyQt5.uic.pyuic asds.ui -o asds.py


def area_convert(ui):
    Squ_met = 0
    squ_mile_to_squ_meter = Decimal(2589988.1103)
    squ_yard_to_squ_meter = Decimal(0.836127)
    squ_feet_to_squ_meter = Decimal(0.09290304)
    squ_inch_to_squ_meter = Decimal(0.00064516)
    hectra_to_squ_meter = 10000
    acre_to_squ_meter = Decimal(4046.85642)

    if ui.lineEdit_square_meter.text().isdecimal():
        Squ_met = Decimal(ui.lineEdit_square_meter.text())
    elif ui.lineEdit_squar_mile.text().isdecimal():
        Squ_met = Decimal(ui.lineEdit_squar_mile.text()) * squ_mile_to_squ_meter
    elif ui.lineEdit_square_yard.text().isdecimal():
        Squ_met = Decimal(ui.lineEdit_square_yard.text()) * squ_yard_to_squ_meter
    elif ui.lineEdit_square_foot.text().isdecimal():
        Squ_met = Decimal(ui.lineEdit_square_foot.text()) *squ_feet_to_squ_meter
    elif ui.lineEdit__square_inch.text().isdecimal():
        Squ_met = Decimal(ui.lineEdit__square_inch.text()) * squ_inch_to_squ_meter
    elif ui.lineEdit_hectra.text().isdecimal():
        Squ_met = Decimal(ui.lineEdit_hectra.text()) * hectra_to_squ_meter
    elif ui.lineEdit_Acre.text().isdecimal():
        Squ_met = Decimal(ui.lineEdit_Acre.text()) * acre_to_squ_meter

    ui.lineEdit_square_meter.setText(str(Squ_met))
    ui.lineEdit_squar_mile.setText(str("{:.10f}".format((Squ_met) / squ_mile_to_squ_meter)))
    ui.lineEdit_square_yard.setText(str("{:.10f}".format((Squ_met) / squ_yard_to_squ_meter)))
    ui.lineEdit_square_foot.setText(str("{:.10f}".format((Squ_met) / squ_feet_to_squ_meter)))
    ui.lineEdit__square_inch.setText(str("{:.10f}".format((Squ_met) / squ_inch_to_squ_meter)))
    ui.lineEdit_hectra.setText(str("{:.10f}".format((Squ_met) / hectra_to_squ_meter)))
    ui.lineEdit_Acre.setText(str("{:.10f}".format((Squ_met) / acre_to_squ_meter)))


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
    yard_to_meter = Decimal(0.9144)
    micrometre_to_meter = Decimal(0.000001)
    mile_to_meter = Decimal(1609.34)
    nanometre_to_meter = Decimal(0.000000001)
    millimeter_to_meter = Decimal(0.001)
    centimeter_to_meter = Decimal(0.01)
    inch_to_meter = Decimal(0.0254)
    foot_to_meter = Decimal(0.3048)
    if ui.lineEdit_meter.text().isdecimal():
        met = Decimal(ui.lineEdit_meter.text())
    elif ui.lineEdit_yard.text().isdecimal():
        met = Decimal(ui.lineEdit_yard.text()) * yard_to_meter
    elif ui.lineEdit_micrometre.text().isdecimal():
        met = Decimal(ui.lineEdit_micrometre.text()) * micrometre_to_meter
    elif ui.lineEdit_mile.text().isdecimal():
        met = Decimal(ui.lineEdit_mile.text()) * mile_to_meter
    elif ui.lineEdit_nanometre.text().isdecimal():
        met = Decimal(ui.lineEdit_nanometre.text()) *nanometre_to_meter
    elif ui.lineEdit_millimeter.text().isdecimal():
        met = Decimal(ui.lineEdit_millimeter.text()) * millimeter_to_meter
    elif ui.lineEdit_centimeter.text().isdecimal():
        met = Decimal(ui.lineEdit_centimeter.text()) * centimeter_to_meter
    elif ui.lineEdit_inch.text().isdecimal():
        met = Decimal(ui.lineEdit_inch.text()) * inch_to_meter
    elif ui.lineEdit_foot.text().isdecimal():
        met = Decimal(ui.lineEdit_foot.text()) * foot_to_meter

    ui.lineEdit_meter.setText(str("{:.10f}".format(met)))
    ui.lineEdit_yard.setText(str("{:.10f}".format(met/yard_to_meter)))
    ui.lineEdit_micrometre.setText(str("{:.10f}".format(met/micrometre_to_meter)))
    ui.lineEdit_mile.setText(str("{:.10f}".format(met/mile_to_meter)))
    ui.lineEdit_nanometre.setText(str("{:.10f}".format(met/nanometre_to_meter)))
    ui.lineEdit_millimeter.setText(str("{:.10f}".format(met/millimeter_to_meter)))
    ui.lineEdit_centimeter.setText(str("{:.10f}".format(met/centimeter_to_meter)))
    ui.lineEdit_inch.setText(str("{:.10f}".format(met/inch_to_meter)))
    ui.lineEdit_foot.setText(str("{:.10f}".format(met/foot_to_meter)))


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
    pound_to_kg=Decimal(0.453592)
    gram_to_kg=Decimal(0.001)
    imp_ton_to_kg = Decimal(1016.05)
    us_ton_to_kg = Decimal(907.185)
    tonne_to_kg = 1000
    ounce_to_kg = Decimal(0.0283495)
    if ui.lineEdit_kilogram.text().isdecimal():
        kg = Decimal(ui.lineEdit_kilogram.text())
    elif ui.lineEdit_pound.text().isdecimal():
        kg =Decimal(ui.lineEdit_pound.text())*pound_to_kg
    elif ui.lineEdit_gram.text().isdecimal():
        kg = Decimal(ui.lineEdit_gram.text())*gram_to_kg
    elif ui.lineEdit_imp_ton.text().isdecimal():
        kg = Decimal(ui.lineEdit_imp_ton.text())*imp_ton_to_kg
    elif ui.lineEdit_us_ton.text().isdecimal():
        kg = Decimal(ui.lineEdit_us_ton.text())*us_ton_to_kg
    elif ui.lineEdit_tonne.text().isdecimal():
        kg = Decimal(ui.lineEdit_tonne.text())*tonne_to_kg
    elif ui.lineEdit_ounce.text().isdecimal():
        kg = Decimal(ui.lineEdit_ounce.text())*ounce_to_kg

    ui.lineEdit_kilogram.setText(str("{:.10f}".format(kg)))
    ui.lineEdit_pound.setText(str("{:.10f}".format(kg/pound_to_kg)))
    ui.lineEdit_gram.setText(str("{:.10f}".format(kg/gram_to_kg)))
    ui.lineEdit_imp_ton.setText(str("{:.10f}".format(kg/imp_ton_to_kg)))
    ui.lineEdit_us_ton.setText(str("{:.10f}".format(kg/us_ton_to_kg)))
    ui.lineEdit_tonne.setText(str("{:.10f}".format(kg/tonne_to_kg)))
    ui.lineEdit_ounce.setText(str("{:.10f}".format(kg/ounce_to_kg)))


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
        "Meter":Decimal(1),
        "Kilometer":Decimal(1000),
        "Mile":Decimal(1609.34),
        "Yard":Decimal(0.9144),
        "Inch":Decimal(0.0254),
        "Foot":Decimal(0.3048)
    }
    getcontext().prec = 6
    if ui.lineEdit_input_speed.text().isdecimal():
        input_num = float(ui.lineEdit_input_speed.text())
        input_time = time_dict[ui.comboBox_in_time.currentText()]
        input_length = length_dict[ui.comboBox_in_length.currentText()]

        out_time = time_dict[ui.comboBox_out_time.currentText()]
        out_length = length_dict[ui.comboBox_out_length.currentText()]

        out_num = input_num*float(input_length/out_length)*(out_time/input_time)
        ui.lineEdit_out_speed.setText(str(out_num))
    else:
        input_num = float(ui.lineEdit_out_speed.text())
        input_time = time_dict[ui.comboBox_in_time.currentText()]
        input_length = length_dict[ui.comboBox_in_length.currentText()]

        out_time = time_dict[ui.comboBox_out_time.currentText()]
        out_length = length_dict[ui.comboBox_out_length.currentText()]

        out_num = input_num*float(input_length/out_length)*(out_time/input_time)
        ui.lineEdit_input_speed.setText(str(out_num))


def speed_clean(ui):
    ui.lineEdit_out_speed.setText("")
    ui.lineEdit_input_speed.setText("")


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
