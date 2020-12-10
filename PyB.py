#                            Pygame Button Class
#               File that contains the class of a button in pygame
#        There will be a rectangular and circular subclass for buttons
#                                 That's it


#Imports
import pygame,cGUIf,Cronos_Text,types,Circle
import ClassChecker as CC

#Start Pygame
pygame.init()

class Rect_Button(pygame.Rect):
    """A Rectangular Button Class."""

    def __init__(self,xpos,ypos,width,height,message="",textcolor = (0,155,0),textsize=15,
                 bgcolor=(155,155,155)):
        """Initialize the Button."""

        #Perfom checks before building attributes
        CC.doQuickCheck(xpos,int)
        CC.doQuickCheck(ypos,int)
        CC.doQuickCheck(width,int)
        CC.doQuickCheck(height,int)
        CC.doQuickCheck(height,int)
        CC.doQuickCheck(message,str)
        CC.checkIfPureClassArray(textcolor,int)
        CC.checkIfPureClassArray(bgcolor,int)

        #Make the attributes
        self.font_file = "freesansbold.ttf"
        self.xpos = xpos
        self.ypos = ypos
        self.width = width
        self.height = height
        self.textsize = textsize
        self.bgcolor = bgcolor #Color of the Button
        self.textcolor = textcolor #Color of the Text
        self.message = message
        self.text = Cronos_Text.Cronos_Text(message,
                                            self.font_file,
                                            self.textsize,
                                            self.textcolor,
                                            self.xtext,
                                            self.ytext)

        self.__onHover = False
        self.__clicked = False
        self.__mouseClick = None #Which button mouse clicked

        #Call parent's constructor method
        super(Rect_Button, self).__init__(self.xpos,
                                          self.ypos,
                                          self.width,
                                          self.height)

    def draw_button(self,surface):
        """Draw the button on the screen."""

        pygame.draw.rect(surface,self.bgcolor,(self.buttonx,
                                               self.buttony,
                                               self.width,
                                               self.height))

        if self.message:
            
            self.text.setXpos(self.xtext)
            self.text.setYpos(self.ytext)

            surface.blit(self.text.Surface,self.text.Surface_Rect)
        

    def check_onhover(self,mouse_coors):
        """Checks if the button is on hover."""

        CC.checkIfPureClassArray(mouse_coors,int)

        if self.collidepoint(mouse_coors):

            self.__onHover = True

        else:
            
            self.__onHover = False
            

    def check_clicked(self,mouse_coors,RoL = "R"):
        """Checks if button was clicked."""

        CC.checkIfPureClassArray(mouse_coors,int)

        if self.collidepoint(mouse_coors):

            self.__clicked = True
            self.__mouseClick = RoL

        else:

            self.__clicked = False
            self.__mouseClick = None
            

    def on_hover(self,action):
        """What to do when mouse button is on hover."""

        CC.doQuickCheck(action,types.FunctionType)
            
        if self.__onHover:
            action()

    def not_onhover(self,action):
        """What to do when button is not on hover."""

        CC.doQuickCheck(action,types.FunctionType)

        if not self.__onHover:
            action()


    def on_click(self,action,onlyOnce=True):
        """What to do when the button is clicked."""

        CC.doQuickCheck(action,types.FunctionType)

        if onlyOnce:

            if self.__clicked:
                action()
                self.__clicked = False
                self.__mouseClick = None

        else:
            if self.__clicked:
                action()

    @property
    def on_Hover(self):
        """Return if button is on hover."""

        return self.__onHover

    @property
    def on_Click(self):
        """Return is button was clicked."""

        return self.__clicked

    @property
    def buttonx(self):
        """X coordinate of the button."""
        
        return self.xpos

    @property
    def buttony(self):
        """Y coordinate of the button."""
        
        return self.ypos

    @property
    def xtext(self):
        """X coordinate of the text."""
        
        return self.xpos + self.width // 2

    @property
    def ytext(self):
        """Y coordinate of the text."""

        return self.ypos + self.height // 2

    @property
    def buttonClicked(self):
        """Return which button did the click."""

        return self.__mouseClick
        

    def changeFontFile(self,newFontFile):
        """Change the font file of the text."""

        CC.doQuickCheck(newFontFile,str)
        
        self.text.setFontFile(newFontFile)
        self.font_file = newFontFile

    def changeTextSize(self,newSize):
        """Change the size of the text."""

        CC.doQuickCheck(newSize,int)

        self.text.setSize(newSize)
        self.textsize = newSize

    def changeTextColor(self,newColor):
        """Change the color of the text."""

        CC.checkIfPureClassArray(newColor,int)

        self.text.setColor(newColor)
        self.textcolor = newColor

    def changeBgColor(self,newBgColor):
        """Change the color of the button."""

        CC.checkIfPureClassArray(newBgColor,int)
        self.bgcolor = newBgColor

    def changeButtonDims(self,newDims):
        """Change the dimensions of the Button."""
        
        CC.checkIfPureClassArray(newDims,int)
        self.width, self.height = newDims

    def changeButtonCoors(self,newCoors):
        """Change the coordinates of the Button."""
        
        CC.checkIfPureClassArray(newCoors,int)
        self.xpos, self.ypos = newCoors 

    def changeButtonMessage(self,newMessage):
        """Change the message of the button."""

        self.text.setMessage(newMessage)
        self.message = newMessage



class Circular_Button(Circle.Circle):
    """A Circular Button."""

    def __init__(self,xcenter,ycenter,radius,
                 message="",textcolor = (0,155,0),
                 textsize=15,
                 bgcolor=(155,155,155)):

        #Perform checks before building attributes
        CC.doQuickCheck(xcenter,int)
        CC.doQuickCheck(ycenter,int)
        CC.doQuickCheck(radius,int)
        CC.doQuickCheck(message,str)
        CC.checkIfPureClassArray(textcolor,int)
        CC.doQuickCheck(textsize,int)
        CC.checkIfPureClassArray(bgcolor,int)

        #Make the attributes
        self.font_file = "freesansbold.ttf"
        self.xcenter = xcenter
        self.ycenter = ycenter
        self.radius = radius
        self.textsize = textsize
        self.bgcolor = bgcolor #Color of the Button
        self.textcolor = textcolor #Color of the Text
        self.message = message
        self.text = Cronos_Text.Cronos_Text(message,
                                            self.font_file,
                                            self.textsize,
                                            self.textcolor,
                                            self.xcenter,
                                            self.ycenter)

        self.__onHover = False
        self.__clicked = False
        self.__mouseClick = None #Which mouse button clicked

        #Call Parents constructor method
        super(Circular_Button,self).__init__(self.xcenter,
                                             self.ycenter,
                                             self.radius)

    def draw_button(self,surface):
        """Draw the button on the screen."""

        pygame.draw.circle(surface,self.bgcolor,self.center_coors,self.radius)

        if self.message:
            
            self.text.setXpos(self.xcenter)
            self.text.setYpos(self.ycenter)

            surface.blit(self.text.Surface,self.text.Surface_Rect)

    def check_onhover(self,mouse_coors):
        """Checks if the button is on hover."""

        if self.pointInsideThis(mouse_coors):

            self.__onHover = True

        else:
            
            self.__onHover = False
            

    def check_clicked(self,mouse_coors,RoL = "R"):
        """Checks if button was clicked."""


        if self.pointInsideThis(mouse_coors):

            self.__clicked = True
            self.__mouseClick = RoL

        else:

            self.__clicked = False
            self.__mouseClick = None
            

    def on_hover(self,action):
        """What to do when mouse button is on hover."""

        CC.doQuickCheck(action,types.FunctionType)
            
        if self.__onHover:
            action()

    def not_onhover(self,action):
        """What to do when button is not on hover."""

        CC.doQuickCheck(action,types.FunctionType)

        if not self.__onHover:
            action()


    def on_click(self,action,onlyOnce=True):
        """What to do when the button is clicked."""

        CC.doQuickCheck(action,types.FunctionType)    

        if onlyOnce:

            if self.__clicked:
                action()
                self.__clicked = False
                self.__mouseClick = None

        else:
            if self.__clicked:
                action()

    def changeFontFile(self,newFontFile):
        """Change the font file of the text."""

        CC.doQuickCheck(newFontFile,str)
        
        self.text.setFontFile(newFontFile)
        self.font_file = newFontFile

    def changeTextSize(self,newSize):
        """Change the size of the text."""

        CC.doQuickCheck(newSize,int)

        self.text.setSize(newSize)
        self.textsize = newSize

    def changeTextColor(self,newColor):
        """Change the color of the text."""

        CC.checkIfPureClassArray(newColor,int)

        self.text.setColor(newColor)
        self.textcolor = newColor

    def changeBgColor(self,newBgColor):
        """Change the color of the button."""

        CC.checkIfPureClassArray(newBgColor,int)
        self.bgcolor = newBgColor

    def changeButtonDims(self,newDims):
        """Change the dimensions of the Button."""
        
        CC.checkIfPureClassArray(newDims,int)

        self.radius = newDims

    def changeButtonCoors(self,newCoors):
        """Change the coordinates of the Button."""
        
        CC.checkIfPureClassArray(newCoors,int)
        self.xcenter, self.ycenter = newCoors 

    def changeButtonMessage(self,newMessage):
        """Change the message of the button."""

        CC.doQuickCheck(newMessage,str)

        self.text.setMessage(newMessage)
        self.message = newMessage

    @property
    def buttonClicked(self):
        """Return which button did the click."""

        return self.__mouseClick

    @property
    def on_Hover(self):
        """Return if button is on hover."""

        return self.__onHover

    @property
    def on_Click(self):
        """Return is button was clicked."""

        return self.__clicked


pygame.quit() #Quit Pygame

def main():

    message = "This script contains two classes of Pygame Buttons."
    message += "\n\nThis script is NOT MEANT TO BE RUN DIRECTLY."
    message += "\nPlease, IMPORT IT IN ANOTHER SCRIPT."

    cGUIf.show_warning("Import Warning",message)

if __name__ == "__main__": 
    main()
