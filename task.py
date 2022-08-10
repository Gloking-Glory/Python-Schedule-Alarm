import datetime
from playsound import playsound

class TaskSchedule:
    def __init__(self) -> None:
        self.username = input('Enter your username >> ')
        self.days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
        self.setTask()
    
    def setTask(self):
        print(self.username.upper() + ' Task Manager')
        self.tasks = {}
        for day in self.days:
            print('SET ' + day.upper() + ' TASKS')
            title = input('Enter the Title for your task >> ')
            time = input('Set time for the task alarm in 24 hours e.g. 10:00 or 15:00 >> ')
            self.tasks.update({ day: {'taskTitle': title, 'taskTime': time }})
        self.taskAlarm()
    
    def taskAlarm(self):
        while True:
            dateTime = datetime.datetime.now()
            currentDay = dateTime.strftime("%A")
            currentTime = dateTime.strftime("%H:%M")
            
            for taskDay, taskDetails in self.tasks.items():
                if taskDay == currentDay and taskDetails['taskTime'] == currentTime:
                    print(taskDetails['taskTitle'] + ' is ringing now')
                    playsound('9ice-Aye-Po-Gan.mp3')


task = TaskSchedule()