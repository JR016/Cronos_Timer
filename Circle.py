#                                 Circle Class
#           A circle class defined to facilitate drawing and stuff

#If the modules are not present, show the user an error messagebox and tell
#them to import them

#IMPORTS
import math
import cGUIf #For GUI warning pop-ups
import ClassChecker as CC #To check that data belongs to certain classes

#GLOBAL CONSTANTS
PI = round(math.pi,2)
        
class Circle(object):
    """A software based circle in the Cartesian plane"""

    def __init__(self,xcenter,ycenter,radius):
        """Initialize a circle object."""

        #Check that all parameters are integers first
        params = [xcenter,ycenter,radius]
        CC.checkIfPureClassArray(params,int)

        self.xcenter = xcenter
        self.ycenter = ycenter

        if radius <= 0: #Check the radius is an positive integer
            self.radius = 1

        else:
            self.radius = radius

    #Define common properties of a circle in the cartesian plane

    @property
    def diameter(self):
        """Create a diameter property."""
        
        return self.radius * 2

    @diameter.setter
    def diameter(self,newDiameter):
        """What to do when the diameter is changed."""

        #Check that "newDiameter" is a number
        isNum = CC.doQuickCheck(newDiameter,int,False)

        if isNum and newDiameter > 1:

            self.radius = newDiameter // 2

    @property
    def center_coors(self):
        """Create a central coordinates property."""
        
        return (self.xcenter,self.ycenter)

    @center_coors.setter
    def center_coors(self,newCenter):
        """What to do if the central coordinates are changed."""

        #First check that "newCenter" parameter is an array of two integers
        toChange = CC.checkIfPureClassArray(newCenter,int,False)

        #Check that "toChange" is a boolean
        isBoolean = CC.doQuickCheck(toChange,bool,False)

        if toChange and isBoolean:
            
            self.xcenter = newCenter[0]
            self.ycenter = newCenter[1]

    @property
    def perimeter(self):
        """Defines the perimeter of the circle."""

        return round(2 * PI * self.radius,2)

    @perimeter.setter
    def perimeter(self,newPerimeter):
        """What to do if the perimeter changes."""

        #Check that "newPerimeter is of type int or float.
        isNum = CC.checkIfBelongsToAny(newPerimeter,float,int)

        if isNum:

            self.radius = int(newPerimeter // (2 * PI))

    @property
    def area(self):
        """Defines the area of the circle."""

        return round(PI * pow(self.radius,2),2)

    @area.setter
    def area(self,newArea):
        """What to do if the area changes."""

        #Check that "newArea" is a number
        isNum = CC.checkIfBelongsToAny(newArea,float,int)

        if isNum:
        
            self.radius = int(math.sqrt(newArea/PI))


    def __str__(self):
        """Return info about this circle."""

        info = "\n\nCircle object\n\n"
        info += f"\nId:                              {id(self)}"
        info += f"\nX coordinate of central point:   {self.xcenter}"
        info += f"\nY coordinate of central point:   {self.ycenter}"
        info += f"\nCentral point coordinates:       {self.center_coors}"
        info += f"\nRadius:                          {self.radius}"
        info += f"\nDiameter:                        {self.diameter}"
        info += f"\nPerimeter:                       {self.perimeter}"
        info += f"\nArea:                            {self.area}\n\n"
        return info


    #The only method of this class
    def pointInsideThis(self,coors):
        """Checks if a given point exists inside this circle."""

        #Check if "coors" is an array and if all its elements are integers
        CC.checkIfPureClassArray(coors,int)

        xpoint = coors[0] #x coordinate of the given point
        ypoint = coors[1] #y coordinate of the given point

        #Do the real checking
        statement1 = pow((xpoint - self.xcenter),2) + pow((ypoint - self.ycenter),2)
        statement2 = pow(self.radius,2)

        return statement1 <= statement2                            
            

def main(): 
    """Execute when script is run directly."""

    #Tell the user this script should not be run directly
    message = "This script contains a Circle class to use in another scripts"
    message += "\n\nTherefore, this script IS NOT MEANT TO BE RUN DIRECTLY."
    message += "\n\nPlease, IMPORT IT IN ANOTHER SCRIPT."

    cGUIf.show_warning("Import Warning",message)



if __name__ == "__main__": 
    main()
