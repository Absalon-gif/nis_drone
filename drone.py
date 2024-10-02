import time
from pymavlink import mavutil


def start_drone():
    # Replace 192.168.4.1 with the drone's actual Wi-Fi IP address
    master = mavutil.mavlink_connection('udpout:192.168.4.2:14550')

    print("Waiting for GCS heartbeat...")
    master.wait_heartbeat()
    print("GCS heartbeat received.")

    while True:
        master.mav.heartbeat_send(
            type=mavutil.mavlink.MAV_TYPE_QUADROTOR,
            autopilot=mavutil.mavlink.MAV_AUTOPILOT_GENERIC,
            base_mode=0,
            custom_mode=0,
            system_status=mavutil.mavlink.MAV_STATE_ACTIVE
        )
        print("Heartbeat sent to GCS.")
        time.sleep(1)


if __name__ == "__main__":
    start_drone()
