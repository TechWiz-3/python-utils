import psutil


class Process():

    def __init__(
        self, pid: int = None,
        name: str = None
    ):
        self.pid = pid
        self.name = name


    def is_running(self) -> bool:
        """
        Takes the name of a process and
        returns True if it is running,
        False if it isn't"""
        if self.name:
            target_process_name = self.name
            for process in psutil.process_iter():
                if self.name.lower() == process.name().lower():
                    return True
            return False
        # if the name isn't specified, use the pid instead
        elif self.pid:
            for process in psutil.process_iter():
                if self.pid == process.pid:
                    return True
            return False


    def get_pid(self) -> int:
        """
        Uses self.name to get the pid
        of the specified process"""
        if not self.name:
            print("Name not provided in instance")
        else:
            for process in psutil.process_iter():
                if self.name.lower() == process.name().lower():
                    return process.pid
            return "Process not found"


    def get_name(self) -> str:
        """
        Uses self.pid to get the name
        of the specifried process"""
        if not self.pid:
            print("PID not provided in instance")
        else:
            for process in psutil.process_iter():
                if self.pid == process.pid:
                    return process.name()
            return False


    def get_run_time(self) -> str:
            """
            Uses self.pid or self.name
            to get the specified process
            and returns it's runtime"""
            if self.name:
                from datetime import datetime
                for process in psutil.process_iter():
                    if self.name.lower() == process.name().lower():
                        epoch_created_time = process.create_time()
                        dt_created_time = datetime.fromtimestamp(epoch_created_time)
                        time_elapsed = datetime.now() - dt_created_time
                        # https://stackoverflow.com/a/10981895
                        hours, remainder = divmod(time_elapsed.seconds, 3600)
                        minutes, seconds = divmod(remainder, 60)
                        if time_elapsed.days != 0:
                            return (
                                    f"{time_elapsed.days} day/s"
                                    f"{hours} hour/s"
                                    f"{minutes}minute/s"
                            )
                        else:
                            return f"{hours} hour/s {minutes} minute/s"
                return "Process not found"
            elif self.pid:
                from datetime import datetime
                for process in psutil.process_iter():
                    if self.pid == process.pid:
                        epoch_created_time = process.create_time()
                        dt_created_time = datetime.fromtimestamp(epoch_created_time)
                        time_elapsed = datetime.now() - dt_created_time
                        # https://stackoverflow.com/a/10981895
                        hours, remainder = divmod(time_elapsed.seconds, 3600)
                        minutes, seconds = divmod(remainder, 60)
                        if time_elapsed.days != 0:
                            return (
                                    f"{time_elapsed.days} day/s"
                                    f"{hours} hour/s"
                                    f"{minutes}minute/s"
                            )
                        else:
                            return f"{hours} hour/s {minutes} minute/s"
                return "Process not found"




a = Process(pid=10678)
# print(a.pid)
# print(a.name)

print(a.get_name())
print(a.get_run_time())
