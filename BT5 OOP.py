# Họ và tên: Nguyễn Trung Hiếu
# Mã số sinh viên: 202418898
import sys
import time
from abc import ABC, abstractmethod
Connected_Devices = []
class Device(ABC):
    def __init__(self, deviceid, name, intouse, cost, state):
        if deviceid == None:
            print("Error: No blank device ID allowed.")
            sys.exit()
        if not cost>0:
            print("Error: The cost must be positive.")
            sys.exit()
        if intouse>int(time.strftime("%Y")):
            print("Error: Unsuitable year into usage detected.")
            sys.exit()
        if state != "Active" and state != "Under maintenance" and state != "Retired":
            print("Error: Device state should either be active or under maintenance or retired")
            sys.exit()

        self.deviceid = deviceid
        self.name = name
        self.intouse = intouse
        self.cost = cost
        self.state = state

    def changename(self,newname):
        self.name = newname

    def changeintouse(self, update):
        self.intouse = update

    def changestate(self, newstate):
        if newstate != "Active" and newstate != "Under maintenance" and newstate != "Retired":
                print("Error: Device state should either be active or under maintenance or retired")
                return
        self.state = newstate

    def costchange(self, costchange):
        self.cost = costchange

    @abstractmethod
    def YearlyExpectedMaintenanceCost(self):
        pass
        
    @abstractmethod
    def Info(self):
        pass
class INetworkable():
    def connect(self):
        pass

    def disconnect(self):
        pass

class Computer(Device, INetworkable):
    def __init__(self, deviceid, name, intouse, cost, state, RAM, processor, GPUavailable, IPaddress):
        if deviceid == None:
            print("Error: No blank device ID allowed.")
            sys.exit()
        if not cost>0:
            print("Error: The cost must be positive.")
            sys.exit()
        if intouse>int(time.strftime("%Y")):
            print("Error: Unsuitable year into usage detected.")
            sys.exit()
        if (state != "Active") and (state != "Under maintenance") and (state != "Retired"):
            print("Error: Device state should either be active or under maintenance or retired")
            sys.exit()
        if not RAM>0:
            print("Error: Memory storage must be positive, in GBs.")
            sys.exit()
        if processor == None:
            print("Error: No blank processor allowed.")
            sys.exit()
        if type(GPUavailable) is not bool:
            print("Error: GPU availability should be either True or False only")
            sys.exit()
        if IPaddress == None:
            print("Error: IP adress cannot be blank")
            sys.exit()
        super().__init__(deviceid, name, intouse, cost, state)
        self.RAM = RAM
        self.processor = processor
        self.GPUavailable = GPUavailable
        self.networksupport = True
        self.IPaddress = IPaddress
        self.isconnected = False
        self.MaintenanceRate = 0.05
        if int(time.strftime("%Y"))-intouse>5:
            self.MaintenanceRate += 0.01
        if GPUavailable:
            self.MaintenanceRate += 0.02

    def changeRAM(self, newval):
        self.RAM = newval

    def changeprocessor(self, newp):
        self.processor = newp

    def changesGPUavailability(self, availability):
        if (availability!=str(True) or availability!=str(False)):
            print("Error. GPU availability should either be True or False")
            sys.exit()
        else:
            self.GPUavailable = availability
        
    def changeIPaddress(self, new):
        if new == None:
            print("Error: IP address cannot be blank")
            return None
        else:
            self.IPaddress = new
   
    def connect(self):
        if self.isconnected:
            print("No, you have already connected to the Internet")
            return None
        print(f"Device with {self.IPaddress} connects to the Internet")
        self.isconnected = True
        global Connected_Devices
        Connected_Devices.append(self.deviceid)
        
    def disconnect(self):
        print(f"Device with {self.IPaddress} disconnected")
        self.isconnected = False
        global Connected_Devices
        Connected_Devices.remove(self.deviceid)
        
    def YearlyExpectedMaintenanceCost(self):
        return self.MaintenanceRate*self.cost

    def Info(self):
        print(f"Computer ID:{self.deviceid}")
        print(f"Computer name:{self.name}")
        print(f"Computer year of into usage:{self.intouse}")
        print(f"Computer cost:{self.cost}")
        print(f"State of the device:{self.state}")
        print(f"RAM storage:{self.RAM}")
        print(f"IP address:{self.IPaddress}")
        print(f"Processor used:{self.processor}")
        print(f"GPU Availability:{str(self.GPUavailable)}")

class Printer(Device):
    def __init__(self, deviceid, name, intouse, cost, state, type, pagesprinted):
        if deviceid == None:
            print("Error: No blank device ID allowed.")
            sys.exit()
        if not cost>0:
            print("Error: The cost must be positive.")
            sys.exit()
        if intouse>int(time.strftime("%Y")):
            print("Error: Unsuitable year into usage detected.")
            sys.exit()
        if state != "Active" and state != "Under maintenance" and state != "Retired":
            print("Error: Device state should either be active or under maintenance or retired")
            sys.exit()
        if pagesprinted<0 or isinstance(pagesprinted, int) == False:
            print("Error: The number of pages printed must be a positive integer.")
            sys.exit()
        if not type == "Laser" and not type == "Inkjet":
            print("Error: The printer type should either be laser or inkjet only")
            sys.exit()

        super().__init__(deviceid, name, intouse, cost, state)
        self.type = type
        self.pagesprinted = pagesprinted
        self.baseMaintenanceCost = 0.04*cost

    def changetype(self, newtype):
        if newtype!="Laser" and newtype!="Inkjet":
            print("Error: The printer type should either be laser or inkjet only")
            sys.exit()
        else:
            self.type = newtype

    def updatepagesprinted(self, newval):
        if isinstance(newval, int) == False or newval<0:
            print("Error: The number of pages printed must be a positive integer.")
            sys.exit()

    def updatenetworkcapability(self, update):
        if type(update) is not bool:
            print("Error: Gaining network support should be either True or False only")
            sys.exit()
        else:
            self.networksupport = update

    def YearlyExpectedMaintenanceCost(self):
        if self.type == "Laser":
            self.baseMaintenanceCost += 300000
        if self.pagesprinted>100000:
            self.baseMaintenanceCost += 500000
        return self.baseMaintenanceCost

    def Info(self):
        print(f"Printer ID:{self.deviceid}")
        print(f"Printer name:{self.name}")
        print(f"Years into use:{self.intouse}")
        print(f"Obtainment Cost:{self.cost}")
        print(f"Current state:{self.state}")
        print(f"Printer type:{self.type}")
        print(f"Pages printed:{self.pagesprinted}")
        print(f"Expected maintenance cost:{self.YearlyExpectedMaintenanceCost()}")

class PrinterWithInternetCapability(Printer, INetworkable):
    def __init__(self, deviceid, name, intouse, cost, state, type, pagesprinted, IPaddress):
        if deviceid == None:
            print("Error: No blank device ID allowed.")
            sys.exit()
        if not cost>0:
            print("Error: The cost must be positive.")
            sys.exit()
        if intouse>int(time.strftime("%Y")):
            print("Error: Unsuitable year into usage detected.")
            sys.exit()
        if state != "Active" and state != "Under maintenance" and state != "Retired":
            print("Error: Device state should either be active or under maintenance or retired")
            sys.exit()
        if pagesprinted<0 or isinstance(pagesprinted, int) == False:
            print("Error: The number of pages printed must be a positive integer.")
            sys.exit()
        if not type == "Laser" and not type == "Inkjet":
            print("Error: The printer type should either be laser or inkjet only")
            sys.exit()
        if IPaddress == None:
            print("Error: IP adress cannot be blank")
            sys.exit()

        def Info(self):
            super().Info()

        super().__init__(deviceid, name, intouse, cost, state, type, pagesprinted)
        self.IPaddress = IPaddress
        self.isconnected = False
    def connect(self):
        if self.isconnected:
            print("No, your printer is already connected!")
            return None
        print(f"Your printer is connected, with the IP address:{self.IPaddress}")
        self.isconnected = True
        global Connected_Devices
        Connected_Devices.append(self.deviceid)

    def disconnect(self):
        if self.isconnected == False:
            print("You have already disconnected!")
            return
        print("Your printer disconnected sucessfully!")
        self.isconnected = False
        global Connected_Devices
        Connected_Devices.remove(self.deviceid)
        

class Projector(Device):
    def __init__(self, deviceid, name, intouse, cost, state, brightness, hours_used):
        if deviceid == None:
            print("Error: No blank device ID allowed.")
            sys.exit()
        if not cost>0:
            print("Error: The cost must be positive.")
            sys.exit()
        if intouse>int(time.strftime("%Y")):
            print("Error: Unsuitable year into usage detected.")
            sys.exit()
        if not state == "Active" and not state == "Under maintenance" and not state == "Retired":
            print("Error: Device state should either be active or under maintenance or retired")
            sys.exit()
        if not brightness>0 or isinstance(brightness, (float, int)) == False:
            print("Error: Brightness fo the projector must be a positive number!")
            sys.exit()
        if hours_used<0 or isinstance(hours_used, (float, int)) == False:
            print("Error: Hours of light usage must be a positive number!")
            sys.exit()

        super().__init__(deviceid, name, intouse, cost, state)
        self.brightness = brightness
        self.hours_used = hours_used
        self.network_capability = False
        self.MaintenanceCost = 0.03*cost
        if(self.hours_used>3000):
            self.MaintenanceCost += 1500000

    def updatebrightness(self, new):
        if not new>0 or isinstance(new, (float, int)) == False:
            print("Error: Brightness fo the projector must be a positive number!")
            sys.exit()
        else:
            self.brightness = new

    def updatehoursusage(self, new):
        if new<0 or isinstance(new, (float, int)) == False:
            print("Error: Hours of light usage must be a positive number!")
            sys.exit()
        else:
            self.hours_used = new

    def YearlyExpectedMaintenanceCost(self):
        return self.MaintenanceCost

    def Info(self):
        print(f"Projector ID:{self.deviceid}")
        print(f"Projector name:{self.name}")
        print(f"Projector first year into use:{self.intouse}")
        print(f"Cost:{self.cost}")
        print(f"Current state:{self.state}")
        print(f"Current brightness:{self.brightness}")
        print(f"Hours of light usage:{self.hours_used}")
        print(f"Expected yearly maintenance cost:{self.YearlyExpectedMaintenanceCost()}")

class LabRoom():
    def __init__(self, roomid, name, capacity, devices_inside):
        if roomid == None or name == None:
            print("Error, room ID and room name cannot be blank!")
            sys.exit()
        if capacity<0 or type(capacity) is not int:
            print("Error, the capacity of the room must be a non-negative integer!")
            sys.exit()
        for i in range(0, len(devices_inside)-1, 1):
            for j in range(i+1, len(devices_inside)-1, 1):
                if devices_inside[j].deviceid == devices_inside[j].deviceid:
                    print("Error, you cannot have 2 devices with the same ID!")
                    return None
                

        self.roomid = roomid
        self.roomname = name
        self.capacity = capacity
        self.devices_inside = []
        for i in devices_inside:
            self.devices_inside.append(i)

    def AddDevice(self, device):
        for i in self.devices_inside:
            if device.deviceid == i.deviceid:
                print("You cannot add another device with an already existing ID")
                return None
            if device == None:
                print("No blank devices!")
                return None

        self.devices_inside.append(device)
        print("Device added to the lab room!")

    def RemoveDevice(self, deviceid):
        for i in self.devices_inside:
            if i.id == deviceid:
                self.device_inside.remove(i)
                return

        print("No device found that matches your device ID")
            
    def FindDevice(self, deviceid):
        for i in self.devices_inside:
            if i.id == deviceid:
                print("You found it!. Here is the information of the device:")
                i.Info()
                return

        print("No device found that matches your device ID")
        return

    def CalculateAnnualMaintenanceCost(self):
        s = 0
        for i in self.devices_inside:
            s += i.YearlyExpectedMaintenanceCost()

        return s

    def GetDevicesRequireMaintenance(self):
        M = []
        for i in self.devices_inside:
            if i.state == "Under maintenance" or int(time.strftime("%Y"))-i.intouse>5:
                M.append(i)

        return M

def main():
    PC1 = Computer("PC01", "Macbook Neo", 2022, 20000000, "Active", 8, "M4", False, "168.132.12.50")
    PC2 = Computer("PC02", "iMac", 2021, 35000000, "Under maintenance", 16, "M4", True, "168.132.11.9")
    Lab1 = LabRoom("L1", "Lab 01", 42, [])
    print("79")
    Lab1.AddDevice(PC1)
    PR1 = Printer("PR01", "HPLaserJet", 2012, 15750000, "Under maintenance", "Inkjet", 145000)
    PR2 = Printer("PR02", "HPHyperion", 2022, 42500000, "Active", "Laser", 2500)
    PJ1 = Projector("PJ01", "PJ project F", 2020, 10000000, "Under maintenance", 80, 4550)
    PJ2 = Projector("PJ02", "Project Panelling Bareicades", 2023, 22500000, "Active", 105, 250)
    L2 = LabRoom("L02", "Lab 02", 50, [PR1, PJ1])
    L2.AddDevice(PC2)
    L2.AddDevice(PJ1)
    PC1.connect()
    PC2.connect()
    PR3 = PrinterWithInternetCapability("PR03", "Project Blast Power", 2025, 50000000, "Active", "Laser", 12, "150.128.15.7")
    PR3.connect()
    print(Connected_Devices)
if __name__ == '__main__':
    main()

            

        

        