'''
Script for Bicycle Generator related calculations
'''

class Bicycle_Generator:
    '''Class Definition'''
    def __init__(self, data_dict):
        """
        Structure for data_dict
        {
            bicycle_weight:int kg,
            rider_weight: int kg,
            bicycle_wheel_diameter: int m
            bicycle_pedal_diameter: int m
            bicycle_front_gear_diameter: int m
            bicycle_back_gear_diameter: int m
            coil_turns: int
            coil_magnet_distance: int m
            bulb_voltage: int V
            circuit_resistance: int ohm
            
            
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
        self.pedal_force = 300 # Unit N
        self.pedal_distance = 0.15 m
        
        
        def force_transfer(self):
            front_gear_distance = 
            

