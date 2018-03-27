'''
Script for Bicycle Generator related calculations
'''

class Bicycle_Generator:
    '''Class Definition'''
    def __init__(self, data_dict):
        """
        Structure for data_dict
        {
            bicycle_weight: double kg,
            rider_weight: double kg,
            bicycle_wheel_diameter: double m
            bicycle_pedal_diameter: double m
            bicycle_front_gear_diameter: double m
            bicycle_back_gear_diameter: double m
            coil_turns: int
            coil_magnet_distance: double m
            bulb_voltage: double V
            circuit_resistance: double ohm
        }

        Thing to calculate:
            RPM
            Voltage
            Magnetic Field
            
        """
        self.weight_of_bicycle = data_dict['bicycle_weight']
        self.rider_weight = data_dict['rider_weight']
        self.bicycle_wheel_diameter = data_dict['bicycle_wheel_diameter']
        self.bicycle_pedal_diameter = data_dict['bicycle_pedal_diameter']
        self.bicycle_front_gear_diameter = data_dict['bicycle_front_gear_diameter']
        self.bicycle_back_gear_diameter = data_dict['bicycle_back_gear_diameter']
        self.coil_turns = data_dict['coil_turns']
        self.coil_magnet_distance = data_dict['coil_magnet_distance']
        self.bulb_voltage = data_dict['bulb_voltage']
        self.circuit_resistance = data_dict['circuit_resistance']
        
        # Assumption Parameter 
        self.pedal_force = 300.0 # Unit N
        self.pedal_distance = 0.175 # m
        self.bike_speed = 7.0 # m/s
        
        # Common constant
        pi = 3.14 
        
        def force_transfer(self):
            front_gear_distance = self.bicycle_front_gear_diameter / self.bicycle_pedal_diameter * self.pedal_distance
            back_gear_distance = self.bicycle_back_gear_diameter / self.bicycle_back_gear_diameter * front_gear_distance
            wheel_distance = self.bicycle_wheel_diameter / self.bicycle_back_gear_diameter * back_gear_distance
            print ("pedal_distance: ", self.pedal_distance, " wheel_distance: ", wheel_distance)
            torque_input = self.pedal_force * self.pedal_distance
            torque_back_gear = self.bicycle_back_gear_diameter / self.bicycle_back_gear_diameter * torque_input 
            print ("torque input: ", torque_input, " torque_back_gear: ", torque_back_gear)
            return 

        def power_output(self):
            pedal_velocity = self.bicycle_pedal_diameter / self.bicycle_wheel_diameter * bike_speed
            print('pedal velocity: ', pedal_velocity)
            power = self.pedal_force * pedal_velocity
            print('pedal power: ', pedal_velocity)
            return
        
        def Other_functions
            return
            
            

