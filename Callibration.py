import odrive
from odrive.enums import *

import math
import time

class ODrive_Callibration:
    def Axis_Param(self, axis, pid_param):
        axis.motor.config.current_lim = pid_param['current_lim']
        axis.controller.config.vel_limit = pid_param['vel_limit']
        axis.controller.config.vel_gain = pid_param['vel_gain']
        axis.controller.config.pos_gain = pid_param['pos_gain']
        axis.controller.config.vel_integrator_gain = pid_param['vel_integrator_gain']


    def Drive_Param(self, drive):
        xBoardSerial = '35627702825038'
        yBoardSerial = '35692127137870'

        ifile = open('PID_parameters.json', "r")
        pid_param = json.load(ifile)

        if(str(drive.serial_number) == xBoardSerial):
            self.Axis_Param(drive.axis0, pid_param['X-axis'])
            #self.Axis_Param(drive.axis1, pid_param['Z-axis'])

        if(str(drive.serial_number) == yBoardSerial):
            self.Axis_Param(drive.axis0, pid_param['Y_axis_main'])
            self.Axis_Param(drive.axis1, pid_param['Y_axis_copy'])
        return drive

    def Initialize(self, serial_num):
        #Works if serial_num is single odrive or a list of odrives
        drives = []
        #Apply PID settings to each axis
        print('Searching for ODrive(s)...')
        for i in range(len(serial_num)):
            my_drive = odrive.find_any(drives[i])
            self.Drive_Param(my_drive)
            drives.append(my_drive)
            print("ODrive " + serial_num + " Connected")

        print("Intializing Callibration Sequence...")

        for drive in drives:
            drive.axis0.requested_state = AXIS_STATE_FULL_CALIBRATION_SEQUENCE
            drive.axis1.requested_state = AXIS_STATE_FULL_CALIBRATION_SEQUENCE

        while 1:
            drivesNotCallibrated = 0
            for drive in drives:
                if drive.axis0.current_state != AXIS_STATE_IDLE or drive.axis1.current_state != AXIS_STATE_IDLE:
                    drivesNotCallibrated += 1
            if drivesNotCallibrated == 0:
                break
            time.sleep(0.1)
            
        for drive in drives:
            drive.axis0.requested_state = AXIS_STATE_CLOSED_LOOP_CONTROL
            drive.axis1.requested_state = AXIS_STATE_CLOSED_LOOP_CONTROL

        return tuple(drives)

    def Bounds_Callibration:
        curr_amp_axis0 = 


#class Homing_Callibration:
    #def Bounds_Callibration:

#class Bounds_Callibration:
