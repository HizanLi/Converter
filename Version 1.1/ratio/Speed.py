from decimal import *

def speed_convert(ui):
    time_dict = {
        "second":1,
        "minute":60,
        "hour":3600

    }
    length_dict={
        "Meter":(1),
        "Kilometer":(1000),
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