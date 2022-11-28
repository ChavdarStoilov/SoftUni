from project.hardware.power_hardware import PowerHardware
from project.hardware.heavy_hardware import HeavyHardware
from project.software.express_software import ExpressSoftware
from project.software.light_software import LightSoftware


class System:
    _hardware = []
    _software = []

    @staticmethod
    def register_power_hardware(name: str, capacity: int, memory: int):
        power_hardware = PowerHardware(name, capacity, memory)

        System._hardware.append(power_hardware)

    @staticmethod
    def register_heavy_hardware(name: str, capacity: int, memory: int):
        heavy_hardware = HeavyHardware(name, capacity, memory)

        System._hardware.append(heavy_hardware)

    @staticmethod
    def register_express_software(hardware_name: str, name: str, capacity_consumption: int,
                                  memory_consumption: int):

        express_software = ExpressSoftware(name, capacity_consumption, memory_consumption)

        for hardware in System._hardware:
            if hardware.name == hardware_name:
                hardware.install(express_software)
                System._software.append(express_software)
                break
        else:
            return 'Hardware does not exist'

    @staticmethod
    def register_light_software(hardware_name: str, name: str, capacity_consumption: int,
                                memory_consumption: int):

        light_software = LightSoftware(name, capacity_consumption, memory_consumption)

        for hardware in System._hardware:
            if hardware.name == hardware_name:
                hardware.install(light_software)
                System._software.append(light_software)
                break
        else:
            return 'Hardware does not exist'

    @staticmethod
    def release_software_component(hardware_name: str, software_name: str):

        hardware = [h for h in System._hardware if h.name == hardware_name]
        software = [s for s in System._software if s.name == software_name]

        if not hardware or not software:
            return 'Some of the components do not exist'

        hardware[0].uninstall(software[0])
        System._software.remove(software[0])

    @staticmethod
    def analyze():
        result = f'System Analysis\n' \
                 f'Hardware Components: {len(System._hardware)}\n' \
                 f'Software Components: {len(System._software)}\n' \
                 f'Total Operational Memory: {sum([s.memory_consumption for s in System._software])} / {sum([h.memory for h in System._hardware])}\n' \
                 f'Total Capacity Taken: {sum([s.capacity_consumption for s in System._software])} / {sum([h.capacity for h in System._hardware])}'

        return result

    @staticmethod
    def system_split():
        result = ""

        for hardware in System._hardware:
            all_software = [soft.name for soft in hardware.software_components]
            resul_from_software = ', '.join(all_software) if len(all_software) > 0 else None
            number_of_express_software = len([express for express in hardware.software_components if express.software_type == 'Express'])
            number_of_light_for_software = len([light for light in hardware.software_components if light.software_type == 'Light'])
            total_memory_soft = sum([soft.memory_consumption for soft in hardware.software_components])
            total_capacity_soft = sum([soft.capacity_consumption for soft in hardware.software_components])

            result += f'Hardware Component - {hardware.name}\n' \
                      f'Express Software Components: {number_of_express_software}\n' \
                      f'Light Software Components: {number_of_light_for_software}\n' \
                      f'Memory Usage: {total_memory_soft} / {hardware.memory}\n' \
                      f'Capacity Usage: {total_capacity_soft} / {hardware.capacity}\n' \
                      f'Type: {hardware.hardware_type}\n' \
                      f'Software Components: {resul_from_software}\n'

        return result.strip()
