#                    Class Checker Script
#         This script contains two classes and two function
#             A ClassCheckerError and A ClassChecker
#    The ClassCheckerError is a custom error raised by the ClassChecker
#      The ClassChecker checks if a value belongs to a given class
#    The function allows the user to check for multiple classes

import cGUIf #For warning pop-up


class ClassCheckerError(Exception):
    """Error raised by the ClassChecker
    when a parameter does not belong to a given class.
    """

    def __init__(self,param,param_class):
        """Initialize the error message."""
        self.param = param
        self.param_class = param_class
        self.message = f"The parameter \"{self.param}\" does not "\
        + f"belong to the class \"{self.param_class.__name__}\""
        
        super(ClassCheckerError,self).__init__(self.message)
        

class ClassChecker(object):
    """Checks if a parameter belongs to a given class."""

    def __init__(self,param,param_class):
        """Initialize the class checker object."""

        self.param = param #Parameter to check if belong to a given class

        if isinstance(param_class,type):
            self.__param_class = param_class #Class given

        else:
            raise ClassCheckerError(param_class,type)

        self.__belongs_to = None #Represents wheter a parameter belongs to a class or not
        self.__newCallCheck = False #Represents if a new check was made

    def getParamValue(self):
        """Returns the value of the parameter to check."""

        return self.param

    def getClassName(self):
        """Returns the name of the class being evaluated."""

        return self.__param_class.__name__

    def getBelongingValue(self):
        """Returns the belonging value of a parameter."""

        if self.__belongs_to == None or not self.__newCallCheck:
            return "A check has not been made yet."

        else:
            return self.__belongs_to

    def setNewParam(self,newParam):
        """Set a new parameter to check."""

        self.param = newParam
        self.__newCallCheck = False

    def setNewClass(self,newClass):
        """Set new class to evaluate to."""

        if isinstance(newClass,type):
            self.__param_class = newClass
            self.__newCallCheck = False

        else:
            raise ClassCheckerError(newClass,type)


    def check(self,withError = True):
        """Check if given parameter belongs to the given class."""

        if not isinstance(self.param,self.__param_class):
            self.__newCallCheck = True
            self.__belongs_to = False

            if withError:
                raise ClassCheckerError(self.param,self.__param_class)

        else:
            self.__newCallCheck = True
            self.__belongs_to = True

#Create a function that gets a list or tuple of tuples or lists of
#Parameters and their classes and check if parameters belong to
#Those respective classes


def doQuickCheck(param,param_class,withError=True):
    """Performs a simple class check.
    It does not return anything when "withError" is True,
    It returns a boolean when "withError" is False."""

    checker = ClassChecker(param,param_class)
    checker.check(withError)

    if not withError:
        return checker.getBelongingValue()
    


def checkIfPureClassArray(array,class_to_check,withError=True):
    """Check if a given array only contains elements that belong
    to one class."""

    #First check that the parameter "array" is indeed an array
    isArray = checkIfBelongsToAny(array,list,tuple)

    if isArray:

        #If show error message is True, there is no need to return anything
        #Just perform the checks
        if withError:

            for element in array:

                checker = ClassChecker(element,class_to_check)
                checker.check(withError)

        else:
            #The user chose to not display error messages, return booleans

            for element in array:

                checker = ClassChecker(element,class_to_check)
                checker.check(withError)
                itBelongs = checker.getBelongingValue()

                if not itBelongs:#One element does not belong
                    return itBelongs

            #All elements belong to the class specified
            return itBelongs

    else:
        #Tell the user this function only works with arrays
        return "This function\\method only works with arrays (Tuples or Lists)."
        
def checkIfBelongsToAny(param,*classes):
    """Check if a parameter belongs to any of the given classes."""

    #If less than two classes are given return early saying it won't work
    if len(classes) < 2:
        return "Cannot work with less than two classes"

    #Check if the paramater belongs to any class
    for each_class in classes:

        checker = ClassChecker(param,each_class)
        checker.check(withError = False)
        doesItBelong = checker.getBelongingValue()

        if doesItBelong == True:
            return doesItBelong #Value is True

    return doesItBelong #Value is False for all classes tested
        
        

def checkIfBelongsToAll(param,*classes,showError=False):
    """Check if a parameter belongs to all given classes."""

    #If less than two classes given return early saying it won't work
    if len(classes) < 2:
        return "Cannot work with less that two classes"

    if showError: #Run if an error is to be shown if the parameter does not belong to a class

        for each_class in classes:
            
            checker = ClassChecker(param,each_class)
            checker.check(withError = showError)

            #No return value is required here, parameter belongs to all classes
            #listed at this point if no error was raised.

    else:

        for each_class in classes:
            
            checker = ClassChecker(param,each_class)
            checker.check(withError = showError)
            doesItBelong = checker.getBelongingValue()

            if not doesItBelong:
                return doesItBelong #False because it does not belong to a given class

        return doesItBelong #True, because it belongs to all given classes

    
def main():

    
    cGUIf.show_warning("Import Warning",
                           "\nThis script contains two classes for checking " \
                           + "if some values belong to a given class." \
                           + "\n\nDO NOT RUN THIS SCRIPT DIRECLY.")

if __name__ == "__main__": 
    main()
