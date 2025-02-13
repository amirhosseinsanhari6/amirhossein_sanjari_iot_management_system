
'''

APM:
salam taske 1 bayad CLass Devcie real world ro bezarid va behesh yek devcie_tyep jadid ezafe konid

Sensor-->tabeye turn_off va turn_on ndre fgth reread-data ro dare

dota tabeye turn_on_all_devices( va turn_off_all_devices( ro check konid

TASK3 ham doroste ahsant

'''
import random

class Device:
    def __init__(self, topic, pin):
        self.topic = topic
        self.topic_list = self.topic.split('/')
        self.location = self.topic_list[0]
        self.group = self.topic_list[1]
        self.device_type = self.topic_list[2]
        self.name = self.topic_list[3]
        self.status = 'off'
        self.pin = pin

    def turn_on(self):
        self.status = 'on'
        print(f'{self.name} now it is turned on')

    def turn_off(self):
        self.status = 'off'
        print(f'{self.name} now it is turned off')

    def get_status(self):
        return self.status


class Sensor:
    def __init__(self, name, group, unit, pin):
        self.name = name
        self.group = group
        self.pin = pin
        self.unit = unit
        self.current_value = None
        self.status = 'off'

    def read_sensor(self):
        possible_values = [22, 23, 24, 25]
        self.current_value = random.choice(possible_values)
        return self.current_value

    def turn_on(self):
        self.status = 'on'
        print(f'{self.name} now it is turned on')

    def turn_off(self):
        self.status = 'off'
        print(f'{self.name} now it is turned off')

    def get_status(self):
        return self.status


class AdminPanel:
    def __init__(self):
        self.groups = {}

    def create_group(self, group_name):
        if group_name not in self.groups:
            self.groups[group_name] = []
            print(f'group "{group_name}" is created')
        else:
            print('name is dublicated')

    def add_device_to_group(self, group_name, device):
        if group_name in self.groups:
            self.groups[group_name].append(device)
            print(f'device {device.name} added in group {group_name}')
        else:
            print(f'group {group_name} does not exist')

    def create_device(self, group_name, device_type, name, pin):
        if group_name in self.groups:
            topic = f'home/{group_name}/{device_type}/{name}'
            new_device = Device(topic, pin)
            self.add_device_to_group(group_name, new_device)
            print(f'device {name} ({device_type}) is created in group {group_name}')
        else:
            print(f'group {group_name} does not exist')

    def create_multiple_devices(self, group_name, device_type, number_of_devices, pin):
        if group_name in self.groups:
            for i in range(1, number_of_devices + 1):
                device_name = f'{device_type}{i}'
                topic = f'home/{group_name}/{device_type}/{device_name}'
                new_device = Device(topic, pin)
                self.add_device_to_group(group_name, new_device)
                print(f'device {device_name} ({device_type}) added to group {group_name}')
        else:
            print(f'group {group_name} does not exist')

    def get_devices_in_group(self, group_name):
        if group_name in self.groups:
            return self.groups[group_name]
        else:
            print(f'group {group_name} does not exist')
            return []

    def turn_on_all_in_group(self, group_name):
        devices = self.get_devices_in_group(group_name)
        for device in devices:
            if isinstance(device, Device):
                device.turn_on()
        print(f'all devices in group {group_name} are now turned on')

    def turn_off_all_in_group(self, group_name):
        devices = self.get_devices_in_group(group_name)
        for device in devices:
            if isinstance(device, Device):
                device.turn_off()
        print(f'all devices in group {group_name} are now turned off')

    def turn_on_all_devices(self):
        for group_name in self.groups:
            for device in self.groups[group_name]:
                if isinstance(device, Device):
                    device.turn_on()
                elif isinstance(device, Sensor):
                    device.turn_on()
        print('all devices are now turned on.')

    def turn_off_all_devices(self):
        for group_name in self.groups:
            for device in self.groups[group_name]:
                if isinstance(device, Device):
                    device.turn_off()
                elif isinstance(device, Sensor):
                    device.turn_off()
        print('all devices are now turned off.')

    def get_status_in_group(self, group_name):
        devices = self.get_devices_in_group(group_name)
        for device in devices:
            print(f'device {device.name}: {device.get_status()}')

    def get_status_in_device_type(self, device_type):
        for group_name, devices in self.groups.items():
            for device in devices:
                if device.device_type == device_type:
                    print(f'{device.name} in {group_name}: {device.get_status()}')

    def create_sensor(self, name, group, unit, pin):
        if group in self.groups:
            new_sensor = Sensor(name, group, unit, pin)
            self.groups[group].append(new_sensor)
            print(f'sensor {name} added in group {group}')
        else:
            print(f'group {group} does not exist')

    def get_data_from_sensor_in_group(self, group_name):
        if group_name in self.groups:
            for device in self.groups[group_name]:
                if isinstance(device, Sensor):
                    print(f'sensor {device.name} value: {device.read_sensor()} {device.unit}')
        else:
            print(f'group {group_name} does not exist')

    def reset_all_devices(self):
        for group_name in self.groups:
            for device in self.groups[group_name]:
                if isinstance(device, Device):
                    device.turn_off()
                elif isinstance(device, Sensor):
                    device.turn_off()
        print(' devices are now turned off and will be reset')

        devices = random.choice(list(self.groups.values()))
        random_device = random.choice(devices)
        random_device.turn_on()
        print(f'{random_device.name} is randomly turned on after reset')

    def get_devices_by_status(self, status):
        for group_name, devices in self.groups.items():
            for device in devices:
                if device.get_status() == status:
                    print(f'{device.name} in {group_name}: {device.get_status()}')

a2 = Device('home/living_room/lamps/lamp1', 5)
a = AdminPanel()
a.create_group('living_room')
a.create_multiple_devices('living_room', 'lamp', 5, 1)
a.create_sensor('temperatureSensor', 'living_room', 'Celsius', 6)

a.turn_on_all_devices()
a.get_status_in_group('living_room')

a.get_data_from_sensor_in_group('living_room')
a.reset_all_devices()

a.get_devices_by_status('on')
