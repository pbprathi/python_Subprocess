from autopy.packageinstallchk import package

class Mainclass:

    def __init__(self):
        self.name="NANO"
        self.cmdType="CHECK"

    def start(self):
        try:
            checkoutput=package.packagesCheck(self.name,self.cmdType)
        except OSError as e:
            sys.exit("failed to execute the command {} :{}".format(str(e)))


# if checkoutput==0:
#  package.packageInstall("NANO","INSTALL")
