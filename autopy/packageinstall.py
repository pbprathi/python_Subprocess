from packageinstallchk import package

def main():
    try:
        checkoutput=package.packagesCheck("NANO","CHECK")
    except OSError as e:
        sys.exit("failed to execute the command {} :{}".format(str(e)))

if __name__=='__main__':
    main()

# if checkoutput==0:
#  package.packageInstall("NANO","INSTALL")
