"""lfr_controller controller."""

# You may need to import some classes of the controller module. Ex:
#  from controller import Robot, Motor, DistanceSensor
from controller import Robot

# create the Robot instance.
robot = Robot()

# get the time step of the current world.
timestep = int(robot.getBasicTimeStep())

# You should insert a getDevice-like function in order to get the
# instance of a device of the robot. Something like:
BRmotor = robot.getDevice('BRWheel')
BLmotor = robot.getDevice('BLWheel')
ir0 = robot.getDevice('ir0')
ir1 = robot.getDevice('ir1')
ir2 = robot.getDevice('ir2')
ir0.enable(timestep)
ir1.enable(timestep)
ir2.enable(timestep)

BLmotor.setPosition(float('inf'))
BRmotor.setPosition(float('inf'))
BLmotor.setVelocity(0)
BRmotor.setVelocity(0)

# Main loop:
# - perform simulation steps until Webots is stopping the controller
max_vell=BLmotor.getMaxVelocity()
max_velr=BRmotor.getMaxVelocity()

while robot.step(timestep) != -1:
    # Read the sensors:
    # Enter here functions to read sensor data, like:
    # ir_val = 1000 for black
    
    ir0_val = round(ir0.getValue(),2)
    ir1_val = round(ir1.getValue(),2)
    ir2_val = round(ir2.getValue(),2)
    
    if ir0_val < 800 and ir1_val < 800 and ir2_val < 800:
        print('Straight')
        BLmotor.setVelocity(max_vell*0.5)
        BRmotor.setVelocity(max_velr*0.5)
        
    if ir0_val < 800 and ir1_val < 800 and ir2_val >= 800:
        print('Rotate Right')
        BLmotor.setVelocity(max_vell*0.5)
        BRmotor.setVelocity(-max_velr*0.5)
        
    if ir0_val < 800 and ir1_val >= 800 and ir2_val >= 800:
        print('Turn Right')
        BLmotor.setVelocity(max_vell*0.5)
        BRmotor.setVelocity(max_velr*0)
        
    if ir0_val >= 800 and ir1_val < 800 and ir2_val >= 800:
        print('Straight')
        BLmotor.setVelocity(max_vell*0.5)
        BRmotor.setVelocity(max_velr*0.5)
        
    if ir0_val < 800 and ir1_val >= 800 and ir2_val < 800:
        print('Straight')
        BLmotor.setVelocity(max_vell*0.5)
        BRmotor.setVelocity(max_velr*0.5)
        
    if ir0_val >= 800 and ir1_val >= 800 and ir2_val < 800:
        print('Turn Left')
        BLmotor.setVelocity(max_vell*0)
        BRmotor.setVelocity(max_velr*0.5)
        
    if ir0_val >= 800 and ir1_val < 800 and ir2_val < 800:
        print('Rotate Left')
        BLmotor.setVelocity(-max_vell*0.5)
        BRmotor.setVelocity(max_velr*0.5)
        
    if ir0_val >= 800 and ir1_val >= 800 and ir2_val >= 800:
        print('Straight')
        BLmotor.setVelocity(max_vell*0.5)
        BRmotor.setVelocity(max_velr*0.5)

      
        
    print(' ')
    print(ir0_val,ir1_val,ir2_val)
    # Process sensor data here.
    

    pass

# Enter here exit cleanup code.









