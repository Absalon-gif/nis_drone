import time
from pymavlink import mavutil

# Change port to 50002
connection = mavutil.mavlink_connection('udpout:127.0.0.1:50002')


# Set up the heartbeat message
def send_heartbeat():
    while True:
        # Send a heartbeat message to the GCS
        connection.mav.heartbeat_send(
            type=mavutil.mavlink.MAV_TYPE_GCS,
            autopilot=mavutil.mavlink.MAV_AUTOPILOT_INVALID,
            base_mode=0,
            custom_mode=0,
            system_status=mavutil.mavlink.MAV_STATE_ACTIVE
        )

        # Log to console to verify the heartbeat is being sent
        print("Heartbeat sent to GCS.")

        time.sleep(1)


# Start the heartbeat message loop
send_heartbeat()
