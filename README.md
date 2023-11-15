# APE Export Dept Checker
 
## Installing
Requires the following installed in the python environment being used:
* tkinter
* requests_html

Expects APE Export (https://github.com/nationalarchives/ctd-APE) to be installed locally. If this can't be installed then it expects the following folder system:

* root
    * data
        * xml (this folder should contain the exported XML files intended for import into Archives Portal Europe with a file per registration code)
    


## Running
Take a copy of the most recent deptCodes.py from the APE Export and copy it into the same folder as the dept-checker script (if you do not have APE Export then debtCodes.py should contain "depts = (XXX)" where XXX is a comma separated list of the registration codes to be exported). 

When the dept-checker script is run it will pop up a folder selector asking for the root directory of the APE Export or the folder system above. It will compare the list of registration codes in debtCodes with the files in the XML directory and the list of registration codes with what is already in the APE content checker and report any discrepancies.
