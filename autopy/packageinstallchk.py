from subprocess import check_output,CalledProcessError,Popen,STDOUT,PIPE
from random import choice
from autopy.readconfigjson import jsonConfig
import sys
class package:
    def packagesCheck(pkg_name,pkg_cmdtype):

        searchstr="install ok installed"
        counter=0
        try:

            #print(jsonConfig.getconfig(pkg_name,pkg_cmdtype))
            numbers=check_output([jsonConfig.getconfig(pkg_name,pkg_cmdtype)],shell=True)
               # we can also use "apt-cache policy python3" command to get the version of the package.
               # https://stackoverflow.com/questions/18885820/how-to-check-the-version-before-install-packages-using-apt-get?rq=1
            numbers=numbers.decode("utf-8")
            output=numbers.split("\n")
            for line in output:
                if searchstr in line:
                    if counter==0:
                        #print("Python package already available")
                        searchstr="Version"
                        counter+=1
                    elif counter==1:
                        print("{} already exists with {} ".format(pkg_name.lower(),line))
                        break
            if counter==1:
                return counter
            elif counter ==0:
                print("{} package doesn't exist, will install in a while".format(pkg_name.lower()))
                pkg_cmdtype="INSTALL"
                packageInstall(pkg_name,pkg_cmdtype)
        except CalledProcessError as e:
           sys.exit("{} failed, Error Code :{}".format(cmd,e.returncode))
        except OSError as e:
           sys.exit("failed to execute the command:{}".format(str(e)))

    def packageInstall(pkg_name,pkg_cmdtype):
        try:
            proc=Popen([jsonConfig.getconfig(pkg_name,pkg_cmdtype)],shell=True, stdout=PIPE,stderr=PIPE)
            (out,err)=proc.communicate();
            proc.wait()
            print("Error :{} Output :{}".format(err,out))
        except OSError as e:
            sys.exit("failed to execute the command {} :{}".format(str(e)))
