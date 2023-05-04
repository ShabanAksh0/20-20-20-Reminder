import winsound
import time

while True:
    # Beep for 20 seconds
    winsound.Beep(440, 20000)
    
    # Wait for 20 minutes
    time.sleep(20*60)
