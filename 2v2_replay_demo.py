from dynamixel_control import Dynamixel
from time import sleep


dxl_control = Dynamixel()
# For XL330
dxl_control.add_dynamixel(type="XL-330", ID_number=0, calibration=[1023,2048,3073], shift = 0) # Negative on left side was -25
dxl_control.add_dynamixel(type="XL-330", ID_number=1, calibration=[1023,2048,3073], shift = 0)
dxl_control.add_dynamixel(type="XL-330", ID_number=3, calibration=[1023,2048,3073], shift = 0) # Positive on right side was 25
dxl_control.add_dynamixel(type="XL-330", ID_number=4, calibration=[1023,2048,3073], shift = 0)
#4565, 545, 450, 553
dxl_control.set_speed(100)
dxl_control.setup_all()
dxl_control.update_PID(1000,400,2000)

#Dynamixel_control.update_speed(400)
#Dynamixel_control.test_write()
#input("press enter to continue")
#Dynamixel_control.update_speed(100)
#Dynamixel_control.go_to_center()
sleep(1)
print("Speed done")

file_list = ['N_mod', 'NE', 'E', 'SE', 'S', 'SW', 'W', 'NW']
counter = 0


try:
    while True:
        trial_name = file_list[counter] + '_2v2_50.50_50.50_1.1_63.pkl'
        dxl_control.set_speed(100)
        dxl_control.go_to_initial_position(file_location = "replay_data",file_name=trial_name)
        #Dynamixel_control.update_speed(1000)
        dxl_control.set_speed(25)

        dxl_control.replay_pickle_data(file_location = "replay_data",file_name=trial_name, delay_between_steps = .05)
    
        counter += 1
        if counter == 8:
            counter = 0
        sleep(3)
except Exception as e:
    print(e)
    dxl_control.reboot_dynamixel()

    dxl_control.end_program()