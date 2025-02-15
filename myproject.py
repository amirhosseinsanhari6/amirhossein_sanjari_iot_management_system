
'''

APM:
salam taske 1 bayad CLass Devcie real world ro bezarid va behesh yek devcie_tyep jadid ezafe konid

Sensor-->tabeye turn_off va turn_on ndre fgth reread-data ro dare

dota tabeye turn_on_all_devices( va turn_off_all_devices( ro check konid

TASK3 ham doroste ahsant

'''
import random

class Device:
    def __init__(self, topic, pin, device_type):
        self.topic = topic
        self.topic_list = self.topic.split('/')
        self.location = self.topic_list[0]
        self.group = self.topic_list[1]
        self.device_type = device_type
        self.name = self.topic_list[3]
        self.status = 'off'
        self.pin = pin

    def turn_on(self):
        self.status = 'on'
        print(f'{self.name}: now it is turned on')

    def turn_off(self):
        self.status = 'off'
        print(f'{self.name}: now it is turned off')

    def get_status(self):
        return self.status

class Sensor:
    def __init__(self, name, group, unit, pin):
        self.name = name
        self.group = group
        self.pin = pin
        self.unit = unit
        self.current_value = None

    def reread_data(self):
        self.current_value = random.choice([20, 21, 22, 23, 24, 25])
        print(f'{self.name}: new data is {self.current_value} {self.unit}')

class AdminPanel:
    def __init__(self):
        self.groups = {}

    def create_group(self, group_name):
        if group_name not in self.groups:
            self.groups[group_name] = []
            print(f'group {group_name} created')

    def add_device_to_group(self, group_name, device):
        if group_name in self.groups:
            self.groups[group_name].append(device)
            print(f'device {device.name} added to group {group_name}')

    def create_device(self, group_name, device_type, name, pin):
        if group_name in self.groups:
            topic = f'home/{group_name}/{device_type}/{name}'
            new_device = Device(topic, pin, device_type)
            self.add_device_to_group(group_name, new_device)
            print(f'device {name} ({device_type}) created in group {group_name}')

    def create_multiple_devices(self, group_name, device_type, pin, count):
        for i in range(count):
            name = f'{device_type}{i+1}'
            self.create_device(group_name, device_type, name, pin)

    def create_sensor(self, name, group, unit, pin):
        if group in self.groups:
            new_sensor = Sensor(name, group, unit, pin)
            self.groups[group].append(new_sensor)
            print(f'sensor {name} added in group {group}')

    def turn_on_all_devices(self):
        for devices in self.groups.values():
            all_device = []
            all_device.extend(devices)
            for i in all_device:
                if isinstance(i, Device):
                    i.turn_on()
        print('all devices are turned on now')

    def turn_off_all_devices(self):
        for devices in self.groups.values():
            all_device = []
            all_device.extend(devices)
            for i in all_device:
                if isinstance(i, Device):
                    i.turn_off()
        print('all devices are turned off now')

    def get_status_in_group(self, group_name):
        if group_name in self.groups:
            for device in self.groups[group_name]:
                print(f'device {device.name}: {device.get_status()}')

    def get_status_in_device_type(self, device_type):
        for group_name, devices in self.groups.items():
            for device in devices:
                if device.device_type == device_type:
                    print(f'{device.name} in {group_name}: {device.get_status()}')

    def get_data_from_sensor_in_group(self, group_name):
        if group_name in self.groups:
            for device in self.groups[group_name]:
                if isinstance(device, Sensor):
                    print(f'sensor {device.name} value: {device.reread_data()} {device.unit}')

    def reset_all_devices(self):
        for group_name in self.groups:
            for device in self.groups[group_name]:
                if isinstance(device, Device):
                    device.turn_off()
        print('all devices are now turned off and will be reset.')

        if self.groups:
            devices = random.choice(list(self.groups.values()))
            if devices:
                random_device = random.choice(devices)
                random_device.turn_on()
                print(f'{random_device.name} is randomly turned on after reset.')

    def get_devices_by_status(self, status):
        for group_name, devices in self.groups.items():
            for device in devices:
                if device.get_status() == status:
                    print(f'{device.name} in {group_name}: {device.get_status()}')
a2 = Device('home/living_room/lamps/lamp1', 5, 'lamp')

a = AdminPanel()
a.create_group('living_room')
a.create_device('living_room', 'lamp', 'lamp1', 5)
a.create_device('living_room', 'fan', 'fan1', 6)
a.create_device('living_room', 'water_pump', 'pump1', 7)

sensor1 = Sensor('temp_sensor', 'living_room', 'C', 8)
a.add_device_to_group('living_room', sensor1)

a.turn_on_all_devices()
a.turn_off_all_devices()
sensor1.reread_data()
a.reset_all_devices()
a.get_data_from_sensor_in_group('on')
