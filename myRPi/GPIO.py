try:
    from RPi.GPIO import StepperMotor
    _imported: bool = True
except ImportError:
    _imported: bool = False

print(f"----- 'RPi.GPIO' import {"was successful" if _imported else "failed (simulation code)"} -----")

if not _imported:
    BCM = 0
    OUT = 0


    def setwarnings(*args, **kwargs):
        return None


    def setmode(*args, **kwargs):
        return None


    def setup(*args, **kwargs):
        return None



    class PWM:
        def __init__(self, *args, **kwargs):
            pass

        @staticmethod
        def start(*args, **kwargs):
            return None


