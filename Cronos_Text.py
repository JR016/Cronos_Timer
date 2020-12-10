#               A Class that Simplifies the use of pygame Text

#IMPORTS
import pygame,cGUIf
import ClassChecker as CC
import os

#Initialize Pygame Font
pygame.font.init()

class Cronos_Text(object):
    """Easier form to use text using PyGame."""

    def __init__(self,message,font_filename,size,color,xpos,ypos,anti_alias = True):

        #Check all data belongs to the appropiate class
        CC.doQuickCheck(message,str)
        CC.doQuickCheck(font_filename,str)
        CC.doQuickCheck(size,int)
        CC.checkIfPureClassArray(color,int)
        CC.doQuickCheck(anti_alias,bool)
        CC.doQuickCheck(xpos,int)
        CC.doQuickCheck(ypos,int)

        #At this point there were no errors,so create attributes
        self.message = message
        self.font_filename = font_filename
        self.size = size
        self.color = color
        self.anti_alias = anti_alias
        self.__xpos = xpos
        self.__ypos = ypos

    @property
    def Font(self):
        return pygame.font.Font(self.font_filename,self.size)

    @property
    def Surface(self):
        return self.Font.render(self.message,
                                self.anti_alias,
                                self.color)
    @property    
    def Surface_Rect(self):
        return self.Surface.get_rect(centerx = self.__xpos,
                                     centery = self.__ypos)

    def getxPos(self):
        return self.__xpos

    def getYpos(self):
        return self.__ypos

    def setXpos(self,newXpos):

        CC.doQuickCheck(newXpos,int)
        self.__xpos = newXpos

    def setYpos(self,newYpos):

        CC.doQuickCheck(newYpos,int)
        self.__ypos = newYpos

    def setFontFile(self,newFontFile):

        #Check the file is avaliable
        if os.path.isfile(newFontFile):
            self.font_filename = newFontFile

    def setSize(self,newSize):

        CC.doQuickCheck(newSize,int)
        self.size = newSize

    def setColor(self,newColor):

        CC.checkIfPureClassArray(newColor,int)
        self.color = newColor

    def setMessage(self,newMessage):
        CC.doQuickCheck(newMessage,str)
        self.message = newMessage
        
        
    def __str__(self):
        """Give a short description of the object."""

        info = "\nCronos Text Object\n\n"
        info += f"Message:                 {self.message}\n"
        info += f"Font File                {self.font_filename}\n"
        info += f"Size:                    {self.size}\n"
        info += f"With Anti-Alias:         {self.anti_alias}\n"
        info += f"Font Object:             {self.Font}\n"
        info += f"Surface Object:          {self.Surface}\n"
        info += f"Surface Rectangle:       {self.Surface_Rect}\n\n"

        return info
                


pygame.font.quit()


def main(): 

    message = "This script contain a Text class that facilitates the use "
    message += "of pygame Text"
    message += "\n\nThis module is NOT MEANT TO BE RUN DIRECTLY"
    message += "\nPlease, IMPORT IT IN ANOTHER SCRIPT."
    
    cGUIf.show_warning("Import Warning",message)

if __name__ == "__main__": 
    main()
