from ..Exception import inputUnitError,outPutUnitError
from decimal import Decimal
# this is the ratio between kilometer and other length unit
lengthKilometer = {"Kilometer": 1,
                   "Meter": 1000,
                   "Decimetre": 10000,
                   "Centimeter": 100000,
                   "Millimeter": 1000000,
                   "Nanometer": 1000000000000,
                   "Picometer": 1e+15,
                   "LightYear": 1.0570e-13,
                   "AstronomicalUnit": 6.6846e-9,
                   "Inch": 39370.0787402,
                   "Foot": 3280.839895,
                   "Yard": 1093.6132983,
                   "Mile": 0.6213712,
                   "SeaMile": 0.539956,
                   "Furlong": 4.9709695,
                   "Fathom": 546.8066492
                   }
# this is the ratio between meter and other length unit
lengthMeter = {"Kilometer": 0.001,
               "Meter": 1,
               "Decimetre": 10,
               "Centimeter": 100,
               "Millimeter": 1000,
               "Nanometer": 1000000000,
               "Picometer": 1000000000000,
               "LightYear": 1.057e-16,
               "AstronomicalUnit": 6.6846e-12,
               "Inch": 39.3700787,
               "Foot": 3.2908,
               "Yard": 1.0936,
               "Mile": 0.0006214,
               "SeaMile": 0.00054,
               "Furlong": 0.004971,
               "Fathom": 0.5469
               }
# this is the ratio between Decimetre and other length unit
lengthDecimetre = {"Kilometer": 0.0001,
                   "Meter": 0.1,
                   "Decimetre": 1,
                   "Centimeter": 10,
                   "Millimeter": 100,
                   "Nanometer": 100000000,
                   "Picometer": 100000000000,
                   "LightYear": 1.0570e-17,
                   "AstronomicalUnit": 6.6846e-13,
                   "Inch": 3.9370079,
                   "Foot": 0.328084,
                   "Yard": 0.1093613,
                   "Mile": 0.0000621,
                   "SeaMile": 0.000054,
                   "Furlong": 0.0004971,
                   "Fathom": 0.0546807
                   }
# this is the ratio between Centimeter and other length unit
lengthCentimeter = {"Kilometer": 0.00001,
                    "Meter": 0.01,
                    "Decimetre": 0.1,
                    "Centimeter": 1,
                    "Millimeter": 10,
                    "Nanometer": 10000000,
                    "Picometer": 10000000000,
                    "LightYear": 1.0570e-18,
                    "AstronomicalUnit": 6.6846e-14,
                    "Inch": 0.39370079,
                    "Foot": 0.0328084,
                    "Yard": 0.01093613,
                    "Mile": 0.00000621,
                    "SeaMile": 0.0000054,
                    "Furlong": 0.00004971,
                    "Fathom": 0.00546807
                    }
# this is the ratio between Millimeter and other length unit
lengthMillimeter = {"Kilometer": 1e-6,
                    "Meter": 0.001,
                    "Decimetre": 0.01,
                    "Centimeter": 0.1,
                    "Millimeter": 1,
                    "Nanometer": 1000000,
                    "Picometer": 1000000000,
                    "LightYear": 1.0570e-19,
                    "AstronomicalUnit": 6.6846e-15,
                    "Inch": 0.0393701,
                    "Foot": 0.0032808,
                    "Yard": 0.0010936,
                    "Mile": 6.2137e-7,
                    "SeaMile": 5.3996e-7,
                    "Furlong": 4.9710e-6,
                    "Fathom": 0.0005468
                    }
# this is the ratio between Nanometer and other length unit
lengthNanometer = {"Kilometer": 1e-12,
                   "Meter": 1e-9,
                   "Decimetre": 1e-8,
                   "Centimeter": 1e-7,
                   "Millimeter": 1e-6,
                   "Nanometer": 0,
                   "Picometer": 1000,
                   "LightYear": 1.0570e-25,
                   "AstronomicalUnit": 6.6846e-21,
                   "Inch": 3.9370e-8,
                   "Foot": 3.2808e-9,
                   "Yard": 1.0936e-9,
                   "Mile": 6.2137e-13,
                   "SeaMile": 5.3996e-13,
                   "Furlong": 4.9710e-12,
                   "Fathom": 5.468e-10
                   }
# this is the ratio between Picometer and other length unit
lengthPicometer = {"Kilometer": 1e-15,
                   "Meter": 1e-12,
                   "Decimetre": 1e-11,
                   "Centimeter": 1e-10,
                   "Millimeter": 1e-9,
                   "Nanometer": 0.001,
                   "Picometer": 1,
                   "LightYear": 1.0570e-8,
                   "AstronomicalUnit": 6.6846e-24,
                   "Inch": 3.9370e-11,
                   "Foot": 3.2808e-12,
                   "Yard": 1.0936e-12,
                   "Mile": 6.2137e-16,
                   "SeaMile": 5.3996e-16,
                   "Furlong": 4.9710e-15,
                   "Fathom": 5.468e-1036
                   }
# this is the ratio between LightYear and other length unit
lengthLightYear = {"Kilometer": 9460730472581,
                   "Meter": 9.4506e+15,
                   "Decimetre": 9.4506e+16,
                   "Centimeter": 9.4506e+17,
                   "Millimeter": 9.4506e+18,
                   "Nanometer": 9.4506e+24,
                   "Picometer": 9.4506e+27,
                   "LightYear": 1,
                   "AstronomicalUnit": 63241.077,
                   "Inch": 3.7247e+17,
                   "Foot": 3.1039e+16,
                   "Yard": 1.0346e+16,
                   "Mile": 5878625373184,
                   "SeaMile": 5108385784331,
                   "Furlong": 4.7029e+13000,
                   "Fathom": 5.1732e+15
                   }
# this is the ratio between AstronomicalUnit and other length unit
lengthAstronomicalUnit = {"Kilometer": 149600000,
                          "Meter": 149600000000,
                          "Decimetre": 1496000000000,
                          "Centimeter": 14960000000000,
                          "Millimeter": 1.4960e+14,
                          "Nanometer": 1.4960e+17,
                          "Picometer": 1.4960e+23,
                          "LightYear": 0.0000158,
                          "AstronomicalUnit": 1,
                          "Inch": 5889763779528,
                          "Foot": 490813648294,
                          "Yard": 163604549431.3,
                          "Mile": 92957130.35871,
                          "SeaMile": 80777537.79698,
                          "Furlong": 743657042.8696,
                          "Fathom": 81802274715.66
                          }
# this is the ratio between Inch and other length unit
lengthInch = {"Kilometer": 0.0000254,
              "Meter": 0.0254,
              "Decimetre": 0.254,
              "Centimeter": 2.54,
              "Millimeter": 25.4,
              "Nanometer": 25400000,
              "Picometer": 25400000000,
              "LightYear": 2.6848e-18,
              "AstronomicalUnit": 1.6979e-13,
              "Inch": 1,
              "Foot": 0.0833333,
              "Yard": 0.0277778,
              "Mile": 0.0000158,
              "SeaMile": 0.0000137,
              "Furlong": 0.0001263,
              "Fathom": 0.0138889
              }
# this is the ratio between  and other length unit
lengthFoot = {"Kilometer": 0.0003048,
              "Meter": 0.3048,
              "Decimetre": 3.048,
              "Centimeter": 30.48,
              "Millimeter": 304.8,
              "Nanometer": 304800000,
              "Picometer": 304800000000,
              "LightYear": 3.2217e-17,
              "AstronomicalUnit": 2.0375e-12,
              "Inch": 12,
              "Foot": 1,
              "Yard": 0.3333333,
              "Mile": 0.0001894,
              "SeaMile": 0.0001646,
              "Furlong": 0.0015152,
              "Fathom": 0.1666667
              }
# this is the ratio between  and other length unit
lengthYard = {"Kilometer": 0.0009144,
              "Meter": 0.9144,
              "Decimetre": 9.144,
              "Centimeter": 91.44,
              "Millimeter": 914.4,
              "Nanometer": 914400000,
              "Picometer": 914400000000,
              "LightYear": 9.6652e-17,
              "AstronomicalUnit": 6.1124e-12,
              "Inch": 36,
              "Foot": 3,
              "Yard": 1,
              "Mile": 0.0005682,
              "SeaMile": 0.0004937,
              "Furlong": 0.0045455,
              "Fathom": 0.5
              }
# this is the ratio between Mile and other length unit
lengthMile = {"Kilometer": 1.609344,
              "Meter": 1609.344,
              "Decimetre": 16093.44,
              "Centimeter": 160934.4,
              "Millimeter": 1609344,
              "Nanometer": 1609344000000,
              "Picometer": 1.6093e+15,
              "LightYear": 1.7011e-13,
              "AstronomicalUnit": 1.0758e-8,
              "Inch": 63360,
              "Foot": 5280,
              "Yard": 1760,
              "Mile": 1,
              "SeaMile": 0.8689762,
              "Furlong": 8,
              "Fathom": 880
              }
# this is the ratio between SeaMile and other length unit
lengthSeaMile = {"Kilometer": 1.852,
                 "Meter": 1852,
                 "Decimetre": 18520,
                 "Centimeter": 185200,
                 "Millimeter": 1852000,
                 "Nanometer": 1852000000000,
                 "Picometer": 1.8520e+15,
                 "LightYear": 1.9576e-13,
                 "AstronomicalUnit": 1.2380e-8,
                 "Inch": 72913.3858268,
                 "Foot": 6076.1154856,
                 "Yard": 2025.3718285,
                 "Mile": 1.1507794,
                 "SeaMile": 1,
                 "Furlong": 9.2062356,
                 "Fathom": 1012.6859143
                 }
# this is the ratio between Furlong and other length unit
lengthFurlong = {"Kilometer": 0.201168,
                 "Meter": 201.168,
                 "Decimetre": 2011.68,
                 "Centimeter": 20116.8,
                 "Millimeter": 201168,
                 "Nanometer": 201168000000,
                 "Picometer": 2.0117e+14,
                 "LightYear": 2.1263e-14,
                 "AstronomicalUnit": 1.3447e-9,
                 "Inch": 7920,
                 "Foot": 660,
                 "Yard": 220,
                 "Mile": 0.125,
                 "SeaMile": 0.108622,
                 "Furlong": 1,
                 "Fathom": 110
                 }
# this is the ratio between Fathom and other length unit
lengthFathom = {"Kilometer": 0.0018288,
                "Meter": 1.8288,
                "Decimetre": 18.288,
                "Centimeter": 182.88,
                "Millimeter": 1828.8,
                "Nanometer": 1828800000,
                "Picometer": 1828800000000,
                "LightYear": 1.9330e-16,
                "AstronomicalUnit": 1.2225e-11,
                "Inch": 72,
                "Foot": 6,
                "Yard": 2,
                "Mile": 0.0011364,
                "SeaMile": 0.0009875,
                "Furlong": 0.0090909,
                "Fathom": 1
                }


def lengthConver(inputUnit, outputUnit):
    if "Kilometer" in inputUnit:
        dict = lengthKilometer
    elif "Meter" in inputUnit:
        dict = lengthMeter
    elif "Decimetre" in inputUnit:
        dict = lengthDecimetre
    elif "Centimeter" in inputUnit:
        dict = lengthCentimeter
    elif "Millimeter" in inputUnit:
        dict = lengthMillimeter
    elif "Nanometer" in inputUnit:
        dict = lengthNanometer
    elif "Picometer" in inputUnit:
        dict = lengthPicometer
    elif "LightYear" in inputUnit:
        dict = lengthLightYear
    elif "AstronomicalUnit" in inputUnit:
        dict = lengthAstronomicalUnit
    elif "Inch" in inputUnit:
        dict = lengthInch
    elif "Foot" in inputUnit:
        dict = lengthFoot
    elif "Yard" in inputUnit:
        dict = lengthYard
    elif "Mile" in inputUnit:
        dict = lengthMile
    elif "SeaMile" in inputUnit:
        dict = lengthSeaMile
    elif "Furlong" in inputUnit:
        dict = lengthFurlong
    elif "Fathom" in inputUnit:
        dict = lengthFathom
    else:
        raise inputUnitError

    if "Kilometer" in outputUnit:
        output = "Kilometer"
    elif "Meter" in outputUnit:
        output = "Meter"
    elif "Decimetre" in outputUnit:
        output = "Decimetre"
    elif "Centimeter" in outputUnit:
        output = "Centimeter"
    elif "Millimeter" in outputUnit:
        output = "Millimeter"
    elif "Nanometer" in outputUnit:
        output = "Nanometer"
    elif "Picometer" in outputUnit:
        output = "Picometer"
    elif "LightYear" in outputUnit:
        output = "LightYear"
    elif "AstronomicalUnit" in outputUnit:
        output = "AstronomicalUnit"
    elif "Inch" in outputUnit:
        output = "Inch"
    elif "Foot" in outputUnit:
        output = "Foot"
    elif "Yard" in outputUnit:
        output = "Yard"
    elif "Mile" in outputUnit:
        output = "Mile"
    elif "SeaMile" in outputUnit:
        output = "SeaMile"
    elif "Furlong" in outputUnit:
        output = "Furlong"
    elif "Fathom" in outputUnit:
        output = "Fathom"
    else:
        raise outPutUnitError

    return dict[output]