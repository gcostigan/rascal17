import modes
import sys
import time

if __name__ == "__main__":
    controller = modes.Modes()

    try:
        # start the controller
        controller.start()
        print "Xbox controller running"
        controller.universal(1)
        print "Main loop started"
        while True:
            time.sleep(1)

    # Ctrl C
    except KeyboardInterrupt:
        print "User cancelled"

    # error
    except:
        print "Unexpected error:", sys.exc_info()[0]

    finally:
        # stop the controller
        controller.stop(1)

