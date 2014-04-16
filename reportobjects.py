import datetime
import yaml
class Vulnerability:
    def __init__(self, **kwargs):
        try:
            self.generate(**kwargs)
        except:
            self.initialized = False
    def generate(self, **kwargs):
        '''
        datefound is a date object containing the date found
        assessment is the assessment id
        evidence is an array of objects containing figures and captions (figure objects)
        impact is the impact description (string)
        remediation is the remediation instructions (string)
        TODO: Enforce types with this function
        '''
        if (not(self.initialized)):
            self.generate(**kwargs)
            self.category = kwargs['category']
            self.datefound = kwargs['datefound']
            self.assessment = kwargs['assessment']
            self.evidence = kwargs['evidence']
            self.impact = kwargs['impact']
            self.remediation = kwargs['remediation']
            self.initialized = True
        self.vulndata = _Vulndata(self.category,self.datefound,self.assessment,evidence,impact,remediation)
    def generateXML(self):
        #Generates an XML file with the vulnerability information
        print("Not Yet Implemented")
    def loadXML(self):
        #Loads a vulnerability from the XML file
        print("Not Yet Implemented")
    def generateJSON(self):
        print("Not Yet Implemented")
    def loadJSON(self):
        print("Not Yet Implemented")
class _Vulndata(yaml.YAMLObject):
#    yaml_tag = u'!Vulnerability'
    def __init__(self,category,datefound,assessment,evidence,impact,remediation):
        self.category = category
        self.datefound = datefound
        self.assessment = assessment
        self.evidence = evidence
        self.impact = impact
        self.remediation = remediation
    def __repr__(self):
        return("{classname}(category={category},datefound={datefound},assessment={assessment},evidence={evidence},impact={impact},remediation={remediation})".format(category=str(self.__class__.__name__),datefound=repr(self.datefound),assessment=repr(self.assessment),evidence=repr(self.evidence),impact=str(self.impact),remediation=str(self.remediation)))
  
class Assessment:
    def __init__(self,app,startdate,enddate,pci):
        #we could use appname or create an app class
        '''
        app is an application object
        startdate and enddate are date objects
        pci is a boolean of if it's pci or not
        '''
        self.app = app
        self.startdate = startdate
        self.enddate = enddtae
        self.pci = pci

class Figure:
    def __init__(self,caption,filelocation):
        self.caption = caption
        self.filelocation = filelocation

class Savefile:
    def __init__(self,filelocation = None):
        self.filelocation = filelocation
        #file is not open yet
        self.file = None
    def open(self,filelocation = None):
        if (filelocation == None and self.filelocation == None):
            raise Exception("File object has no file location").with_traceback(tracebackobj)
        elif(not(filelocation == None)):
            self.filelocation = filelocation
        
