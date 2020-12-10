#                               Timer Controlers
#                     Contains a Timer Countdown Class
#                        Might include an Stopwatch



#Imports
import cGUIf,datetime
import ClassChecker as CC

def second_passed():
    """Returns True if a second has passed."""

    old_now = datetime.datetime.now()
    new_now = None
    iterations = 0
    max_iterations = 200000 #Have a limited number of iterations to speed up stuff

    while iterations < max_iterations: 

        iterations += 1

        new_now = datetime.datetime.now()

        if old_now.second != new_now.second:
            return True
#Classes

class Timer(object):
    """A Countdown Timer Software Blueprint."""

    #Define the minimum values possible for seconds, minutes and hours
    MIN_SECS  = 0
    MIN_MINS  = 0
    MIN_HOURS = 0

    #Define the maximum values possible for seconds, minutes and hours
    MAX_SECS  = 59
    MAX_MINS  = 59
    MAX_HOURS = 99


    def __init__(self):
        """Inititalize a Timer object."""

        self.__secs  = 0 #Number of seconds
        self.__mins  = 0 #Number of minutes
        self.__hours = 0 #Number of hours
        self.__running = False #Timer running state
        self.__time_up = False #Chech if the time is up

    #Define property getters and setters for these private attributes

    @property
    def time_isUp(self):
        """Return if the time is up."""

        return self.__time_up

    @property
    def seconds(self):
        """Return the number of seconds."""

        return self.__secs

    @seconds.setter
    def seconds(self,newSeconds):
        """Ensure that the new value for seconds is appropiate."""

        CC.doQuickCheck(newSeconds,int)

        self.__secs = newSeconds

    @property
    def minutes(self):
        """Return the number of minutes."""

        return self.__mins

    @minutes.setter
    def minutes(self,newMinutes):
        """Ensure that the new value for minutes is appropiate."""

        CC.doQuickCheck(newMinutes,int)

        self.__mins = newMinutes

    @property
    def hours(self):
        """Return the number of hours."""

        return self.__hours

    @hours.setter
    def hours(self,newHours):
        """Ensure that the new value for hours is appropiate."""

        CC.doQuickCheck(newHours,int)

        self.__hours = newHours

    @property
    def isRunning(self):
        """Return the running state of the timer."""

        return self.__running


    def run(self):
        """Start or restart the timer."""
        
        if not self.isRunning:
            self.__running = True

    def freeze(self):
        """Freeze the timer."""

        if self.isRunning:
            self.__running = False

    def reset(self):
        """Reset the timer."""
        
        self.seconds = 0
        self.minutes = 0
        self.hours = 0

    def countdown(self):
        """Main countdown function."""

        #This method must be run inside a while loop to work propertly

        if self.isRunning:
            
            if second_passed():

                self.seconds -= 1

                if self.hours > Timer.MIN_HOURS and self.minutes == Timer.MIN_MINS \
                   and self.seconds < Timer.MIN_SECS:
                    self.minutes = Timer.MAX_MINS
                    self.seconds = Timer.MAX_SECS
                    self.hours -= 1

                if self.seconds < Timer.MIN_SECS and self.minutes > Timer.MIN_MINS:
                    self.minutes -= 1
                    self.seconds = Timer.MAX_SECS


            if self.seconds == Timer.MIN_SECS \
               and self.minutes == Timer.MIN_MINS \
               and self.hours == Timer.MIN_HOURS:
                self.freeze()
                self.__time_up = True

            else:
                self.__time_up = False

    @property
    def timeFormat(self):
        """How the Timer should be displayed for external software objects."""

        return str(self.hours).zfill(2) + ":" + str(self.minutes).zfill(2) \
               + ":" + str(self.seconds).zfill(2)

    def __str__(self):
        """Info displayed when the object is print."""

        info = "\n\nTimer Object:\n\n"
        info += f"Id:                {id(self)}\n"
        info += f"Countdown Running: {self.__running}\n"
        info += f"Seconds:           {self.seconds}\n"
        info += f"Minutes:           {self.minutes}\n"
        info += f"Hours:             {self.hours}\n"
        info += f"Display Format:    {self.timeFormat}\n\n"

        return info


#Tell the user not to run this file directly
def main(): 

    message = "This script contains a Countdown Timer Class for the \"Cronos\" project"
    message += "\n\nThis script is NOT MEANT TO BE RUN DIRETCLY"
    message += "\nPlease, IMPORT IT IN ANOTHER SCRIPT."

    cGUIf.show_warning("Import Warning",message)


#Run "main" if script is run directly
if __name__ == "__main__": 
    main()
