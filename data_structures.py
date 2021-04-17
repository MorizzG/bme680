# BME680 data structures

import constants
from tools import twos_comp, bytes_to_word


class FieldData:
    """Structure for storing BME680 sensor data."""

    def __init__(self):  # noqa D107
        # Contains new_data, gasm_valid & heat_stab
        self.status = None
        self.heat_stable = False
        # The index of the heater profile used
        self.gas_index = None
        # Measurement index to track order
        self.meas_index = None
        # Temperature in degree celsius x100
        self.temperature = None
        # Pressure in Pascal
        self.pressure = None
        # Humidity in % relative humidity x1000
        self.humidity = None
        # Gas resistance in Ohms
        self.gas_resistance = None


class CalibrationData:
    """Structure for storing BME680 calibration data."""

    def __init__(self):  # noqa D107
        self.par_h1 = None
        self.par_h2 = None
        self.par_h3 = None
        self.par_h4 = None
        self.par_h5 = None
        self.par_h6 = None
        self.par_h7 = None
        self.par_gh1 = None
        self.par_gh2 = None
        self.par_gh3 = None
        self.par_t1 = None
        self.par_t2 = None
        self.par_t3 = None
        self.par_p1 = None
        self.par_p2 = None
        self.par_p3 = None
        self.par_p4 = None
        self.par_p5 = None
        self.par_p6 = None
        self.par_p7 = None
        self.par_p8 = None
        self.par_p9 = None
        self.par_p10 = None
        # Variable to store t_fine size
        self.t_fine = None
        # Variable to store heater resistance range
        self.res_heat_range = None
        # Variable to store heater resistance value
        self.res_heat_val = None
        # Variable to store error range
        self.range_sw_err = None

    def set_from_array(self, calibration):
        """Set paramaters from an array of bytes."""
        # Temperature related coefficients
        self.par_t1 = bytes_to_word(
            calibration[constants.T1_MSB_REG], calibration[constants.T1_LSB_REG]
        )
        self.par_t2 = bytes_to_word(
            calibration[constants.T2_MSB_REG],
            calibration[constants.T2_LSB_REG],
            bits=16,
            signed=True,
        )
        self.par_t3 = twos_comp(calibration[constants.T3_REG], bits=8)

        # Pressure related coefficients
        self.par_p1 = bytes_to_word(
            calibration[constants.P1_MSB_REG], calibration[constants.P1_LSB_REG]
        )
        self.par_p2 = bytes_to_word(
            calibration[constants.P2_MSB_REG],
            calibration[constants.P2_LSB_REG],
            bits=16,
            signed=True,
        )
        self.par_p3 = twos_comp(calibration[constants.P3_REG], bits=8)
        self.par_p4 = bytes_to_word(
            calibration[constants.P4_MSB_REG],
            calibration[constants.P4_LSB_REG],
            bits=16,
            signed=True,
        )
        self.par_p5 = bytes_to_word(
            calibration[constants.P5_MSB_REG],
            calibration[constants.P5_LSB_REG],
            bits=16,
            signed=True,
        )
        self.par_p6 = twos_comp(calibration[constants.P6_REG], bits=8)
        self.par_p7 = twos_comp(calibration[constants.P7_REG], bits=8)
        self.par_p8 = bytes_to_word(
            calibration[constants.P8_MSB_REG],
            calibration[constants.P8_LSB_REG],
            bits=16,
            signed=True,
        )
        self.par_p9 = bytes_to_word(
            calibration[constants.P9_MSB_REG],
            calibration[constants.P9_LSB_REG],
            bits=16,
            signed=True,
        )
        self.par_p10 = calibration[constants.P10_REG]

        # Humidity related coefficients
        self.par_h1 = (calibration[constants.H1_MSB_REG] << constants.HUM_REG_SHIFT_VAL) | (
            calibration[constants.H1_LSB_REG] & constants.BIT_H1_DATA_MSK
        )
        self.par_h2 = (calibration[constants.H2_MSB_REG] << constants.HUM_REG_SHIFT_VAL) | (
            calibration[constants.H2_LSB_REG] >> constants.HUM_REG_SHIFT_VAL
        )
        self.par_h3 = twos_comp(calibration[constants.H3_REG], bits=8)
        self.par_h4 = twos_comp(calibration[constants.H4_REG], bits=8)
        self.par_h5 = twos_comp(calibration[constants.H5_REG], bits=8)
        self.par_h6 = calibration[constants.H6_REG]
        self.par_h7 = twos_comp(calibration[constants.H7_REG], bits=8)

        # Gas heater related coefficients
        self.par_gh1 = twos_comp(calibration[constants.GH1_REG], bits=8)
        self.par_gh2 = bytes_to_word(
            calibration[constants.GH2_MSB_REG],
            calibration[constants.GH2_LSB_REG],
            bits=16,
            signed=True,
        )
        self.par_gh3 = twos_comp(calibration[constants.GH3_REG], bits=8)

    def set_other(self, heat_range, heat_value, sw_error):
        """Set other values."""
        self.res_heat_range = (heat_range & constants.RHRANGE_MSK) // 16
        self.res_heat_val = heat_value
        self.range_sw_err = (sw_error & constants.RSERROR_MSK) // 16


class TPHSettings:
    """Structure for storing BME680 sensor settings.

    Comprises of output data rate, over-sampling and filter settings.

    """

    def __init__(self):  # noqa D107
        # Humidity oversampling
        self.os_hum = None
        # Temperature oversampling
        self.os_temp = None
        # Pressure oversampling
        self.os_pres = None
        # Filter coefficient
        self.filter = None


class GasSettings:
    """Structure for storing BME680 gas settings and status."""

    def __init__(self):  # noqa D107
        # Variable to store nb conversion
        self.nb_conv = None
        # Variable to store heater control
        self.heatr_ctrl = None
        # Run gas enable value
        self.run_gas = None
        # Pointer to store heater temperature
        self.heatr_temp = None
        # Pointer to store duration profile
        self.heatr_dur = None
