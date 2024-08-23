import os
class Linux:
    def get_disk_status(self):
        return f"Disk status: \n\n{os.popen('df -h').read()}"
    
    def get_memory_status(self):
        return f"Memory status: \n\n{os.popen('free -m').read()}"

    def get_processes_list(self):
        return f"List processes status: \n\n{os.popen('ps -aux | grep root').read()}"
