import vrep
import sys, math
import keyboard 
#導入鍵盤
# child threaded script: 
# 內建使用 port 19997 若要加入其他 port, 在  serve 端程式納入
#simExtRemoteApiStart(19999)
  
vrep.simxFinish(-1)
  
clientID = vrep.simxStart('127.0.0.1', 19997, True, True, 5000, 5)
if clientID!= -1:
    print("Connected to remote server")
else:
    print('Connection not successful')
    sys.exit('Could not connect')

KickBallV = 360  
R_KickBallVel = (math.pi/180)*KickBallV
B_KickBallVel = -(math.pi/180)*KickBallV

errorCode,R1_handle=vrep.simxGetObjectHandle(clientID,'R1',vrep.simx_opmode_oneshot_wait)
errorCode,R2_handle=vrep.simxGetObjectHandle(clientID,'R2',vrep.simx_opmode_oneshot_wait)
errorCode,P_handle=vrep.simxGetObjectHandle(clientID,'P',vrep.simx_opmode_oneshot_wait)
vrep.simxSetJointTargetVelocity(clientID,R1_handle,0,vrep.simx_opmode_oneshot_wait)
vrep.simxSetJointTargetVelocity(clientID,R2_handle,0,vrep.simx_opmode_oneshot_wait)
vrep.simxSetJointTargetVelocity(clientID,P_handle,0,vrep.simx_opmode_oneshot_wait)
#定義平移軸旋轉軸

def a1():
    errorCode=vrep.simxSetJointTargetVelocity(clientID,R1_handle,R_KickBallVel,vrep.simx_opmode_oneshot_wait)
def d1():    
     errorCode=vrep.simxSetJointTargetVelocity(clientID,R2_handle,B_KickBallVel,vrep.simx_opmode_oneshot_wait)
def w1():
     errorCode=vrep.simxSetJointTargetVelocity(clientID,P_handle,1,vrep.simx_opmode_oneshot_wait)
#定義平移軸及旋轉軸的速度


vrep.simxStartSimulation(clientID,vrep.simx_opmode_oneshot_wait)
#開始

while True:
    try:
            if keyboard.is_pressed('a'):
                a1()
            elif keyboard.is_pressed('l'):
                d1()
            else:
                errorCode=vrep.simxSetJointTargetVelocity(clientID,R1_handle,B_KickBallVel,vrep.simx_opmode_oneshot_wait)
                errorCode=vrep.simxSetJointTargetVelocity(clientID,R2_handle,R_KickBallVel,vrep.simx_opmode_oneshot_wait)
            if  keyboard.is_pressed('up'):
                w1()
            else:
                errorCode=vrep.simxSetJointTargetVelocity(clientID,P_handle,-1,vrep.simx_opmode_oneshot_wait)
    except:
            break
#執行按建