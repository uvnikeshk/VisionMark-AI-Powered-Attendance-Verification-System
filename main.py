class VisionMark:
    def __init__(self):
        self.project_name = "VisionMark"

    def start(self):
        print(f"{self.project_name} Started")

    def register_student(self):
        print("Student Registration Module")

    def mark_attendance(self):
        print("Attendance Marking Module")


if __name__ == "__main__":
    system = VisionMark()
    system.start()