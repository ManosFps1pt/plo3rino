try:
    from stepper import StepperMotor
    _imported: bool = True
except ImportError:
    _imported: bool = False

print(f"----- 'stepper.StepperMotor' import {"was successful" if _imported else "failed (simulation code)"} -----")

if not _imported:
    class StepperMotor:
        def __init__(self, *args, **kwargs):
            pass

        def enable(self, *args, **kwargs):
            pass

        def disable(self, *args, **kwargs):
            pass

        def run(self, *args, **kwargs):
            pass


