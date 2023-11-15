from tkinter import filedialog
import os, os.path, math
import deptCodes
from requests_html import HTMLSession


def exported_xml_files(root_path):
    # Get list of xml files from ..\APE\APE Export\data\xml
    fullpath=os.path.join(root_path, "data/xml")
    return [f.split(".")[0] for f in os.listdir(fullpath) if f.split(".")[-1] == "xml"]
    

def current_APE_values(count="", page_no="", references = []):
    """ Get current depts from content checker site at https://contentchecker.archivesportaleurope.net/advanced-search/search-in-archives/?term=*&levels[]=archdesc&countries[]=UNITED_KINGDOM:G:37&institutions[]=The%20National%20Archives%202:32391&using=default&sort=Finding%20aid%20no&context=listTab
        Currently (14/11/2023) the APE webpage requires javascript to work which is why we are using requests_html rather than requests and beautiful soup
    """
    session = HTMLSession()
    
    if page_no == "":
        webpage = session.get("https://contentchecker.archivesportaleurope.net/advanced-search/search-in-archives/?term=*&levels[]=archdesc&countries[]=UNITED_KINGDOM:G:37&institutions[]=The%20National%20Archives%202:32391&using=default&sort=Finding%20aid%20no&context=listTab")
        page_no = 2
    else:
        webpage = session.get("https://contentchecker.archivesportaleurope.net/advanced-search/search-in-archives/?term=*&levels[]=archdesc&countries[]=UNITED_KINGDOM:G:37&institutions[]=The%20National%20Archives%202:32391&using=default&sort=Finding%20aid%20no&context=listTab&page="+str(page_no))
        page_no += 1


    webpage.html.render()

    if count == "":
        count = webpage.html.xpath("//span[@data-populate='results_count']/text()")[0]

    last_page = math.ceil(int(count) / 10)

    references += webpage.html.xpath("//div[@class='searchResult']/@data-lazy-load")

    print(page_no)
    #print(count)
    #print(references)
    
    if page_no < (last_page + 1):
        return current_APE_values(count, page_no, references)  
    else:
        return references



def get_root_path():
    '''Get the root directory of the APE Export folder'''
    return filedialog.askdirectory(title="Select Ape Export directory")


root_path = get_root_path()
values = {}
values["deptsList"] = deptCodes.depts
values["exportedFiles"] = exported_xml_files(root_path)
values["APECurrent"] = current_APE_values()

# comparing deptList and exportedFiles
difference_result1 = set(values["deptsList"]).symmetric_difference(set(values["exportedFiles"]))

# comparing deptList and APECurrent
difference_result2 = set(values["deptsList"]).symmetric_difference(set(values["APECurrent"]))

if len(difference_result1) > 0:
    print("Difference between department list and exported files")
    print(difference_result1)

if len(difference_result2) > 0:
    print("Difference between department list and previously exported files")
    print(difference_result2)