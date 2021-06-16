from decimal import Decimal
from ..Exception import inputUnitError, outPutUnitError

# this is the ratio between and other units
areaSquareKilometer = {"SquareKilometer": 1,
                       "Hectare": 100,
                       "Are": 1000,
                       "SquareMeter": 1000000,
                       "SquareCentimeter": 10000000000,
                       "Acre": 247.1053815,
                       "SquareMile": 0.3861022,
                       "SquareInch": 1550003100.006,
                       "SquareFoot": 10763910.41671,
                       "SquareYard": 1195990.046301,
                       "SquareRood": 39536.8610347
                       }

# this is the ratio between and other units
areaHectare = {"SquareKilometer": Decimal(0.01),
               "Hectare": 1,
               "Are": 100,
               "SquareMeter": 10000,
               "SquareCentimeter": 100000000,
               "Acre": Decimal(2.4710538),
               "SquareMile": Decimal(0.003861),
               "SquareInch": Decimal(15500031.00006),
               "SquareFoot": Decimal(107639.1041671),
               "SquareYard": Decimal(11959.900463),
               "SquareRood": Decimal(395.3686103)
               }

# this is the ratio between and other units
areaAre = {"SquareKilometer": Decimal(0.0001),
           "Hectare": Decimal(0.01),
           "Are": 1,
           "SquareMeter": 100,
           "SquareCentimeter": 1000000,
           "Acre": Decimal(0.0247105),
           "SquareMile": Decimal(0.0000386),
           "SquareInch": Decimal(155000.3100006),
           "SquareFoot": Decimal(1076.3910417),
           "SquareYard": Decimal(119.5990046),
           "SquareRood": Decimal(3.9536861)
           }

# this is the ratio between and other units
areaSquareMeter = {"SquareKilometer": Decimal(1e-6),
                   "Hectare": Decimal(0.0001),
                   "Are": Decimal(0.01),
                   "SquareMeter": (1),
                   "SquareCentimeter": (10000),
                   "Acre": Decimal(0.0002471),
                   "SquareMile": Decimal(3.8610e-7),
                   "SquareInch": Decimal(1550.0031),
                   "SquareFoot": Decimal(10.7639104),
                   "SquareYard": Decimal(1.19599),
                   "SquareRood": Decimal(0.0395369)
                   }

# this is the ratio between and other units
areaSquareCentimeter = {"SquareKilometer": Decimal(1e-10),
                        "Hectare": Decimal(1e-8),
                        "Are": Decimal(1e-6),
                        "SquareMeter": Decimal(0.0001),
                        "SquareCentimeter": (1),
                        "Acre": Decimal(2.4711e-8),
                        "SquareMile": Decimal(3.8610e-11),
                        "SquareInch": Decimal(0.1550003),
                        "SquareFoot": Decimal(0.0010764),
                        "SquareYard": Decimal(0.0001196),
                        "SquareRood": Decimal(3.9537e-6)
                        }

# this is the ratio between and other units
areaAcre = {"SquareKilometer": Decimal(0.0040469),
            "Hectare": Decimal(0.4046856),
            "Are": Decimal(40.4685642),
            "SquareMeter": Decimal(4046.8564224),
            "SquareCentimeter": Decimal(40468564.224),
            "Acre": 1,
            "SquareMile": Decimal(0.0015625),
            "SquareInch": (6272640),
            "SquareFoot": (43560),
            "SquareYard": Decimal(4840),
            "SquareRood": Decimal(160)
            }

# this is the ratio between and other units
areaSquareMile = {"SquareKilometer": Decimal(2.5899881),
                  "Hectare": Decimal(258.998811),
                  "Are": Decimal(25899.8811034),
                  "SquareMeter": Decimal(2589988.110336),
                  "SquareCentimeter": Decimal(25899881103.36),
                  "Acre": (640),
                  "SquareMile": (1),
                  "SquareInch": (4014489600),
                  "SquareFoot": (27878400),
                  "SquareYard": (3097600),
                  "SquareRood": (102400)
                  }

# this is the ratio between and other units
areaSquareFoot = {"SquareKilometer": Decimal(9.2903e-8),
                  "Hectare": Decimal(9.2903e-6),
                  "Are": Decimal(0.000929),
                  "SquareMeter": Decimal(0.092903),
                  "SquareCentimeter": Decimal(929.0304),
                  "Acre": Decimal(0.000023),
                  "SquareMile": Decimal(3.5870e-8),
                  "SquareInch": Decimal(144),
                  "SquareFoot": (1),
                  "SquareYard": Decimal(0.1111111),
                  "SquareRood": Decimal(0.0036731)
                  }

# this is the ratio between and other units
areaSquareInch = {"SquareKilometer": Decimal(6.4516e-10),
                  "Hectare": Decimal(6.4516e-8),
                  "Are": Decimal(6.4516e-6),
                  "SquareMeter": Decimal(0.0006452),
                  "SquareCentimeter": Decimal(6.4512),
                  "Acre": Decimal(1.5942e-7),
                  "SquareMile": Decimal(2.4910e-10),
                  "SquareInch": (1),
                  "SquareFoot": Decimal(0.0069444),
                  "SquareYard": Decimal(0.0007716),
                  "SquareRood": Decimal(0.0000255)
                  }

# this is the ratio between and other units
areaSquareYard = {"SquareKilometer": Decimal(8.3613e-7),
        "Hectare": Decimal(0.0000836),
        "Are": Decimal(0.0083613),
        "SquareMeter": Decimal(0.8361274),
        "SquareCentimeter": Decimal(8361.2736),
        "Acre": Decimal(0.0002066),
        "SquareMile": Decimal(3.2283e-7),
        "SquareInch": Decimal(1296),
        "SquareFoot": (9),
        "SquareYard": (1),
        "SquareRood": Decimal(0.0330579)
        }

# this is the ratio between and other units
areaSquareRood = {"SquareKilometer": Decimal(0.0000253),
        "Hectare": Decimal(0.0025293),
        "Are": Decimal(0.2529285),
        "SquareMeter": Decimal(25.2928526),
        "SquareCentimeter": Decimal(2529.285264),
        "Acre": Decimal(0.00625),
        "SquareMile": Decimal(9.7656e-6),
        "SquareInch": (39204),
        "SquareFoot": Decimal(272.25),
        "SquareYard": Decimal(30.25),
        "SquareRood": (1)
        }