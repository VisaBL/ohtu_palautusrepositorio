import tomllib

from urllib import request
from project import Project

#toml tiedostojen käytettävä kirjasto pyhton 3.11 vakiopaketeissa, -> Päivitetty projektin minimivaatimukseksi pyhton 3.11
class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        content = request.urlopen(self._url).read().decode("utf-8")
        content_parsed = tomllib.loads(content)["tool"]["poetry"]
        name = content_parsed["name"]
        desc = content_parsed["description"]
        legal = content_parsed["license"]
        dep = content_parsed["dependencies"] 
        dev_dep = content_parsed["group"]["dev"]["dependencies"]
        authors = content_parsed["authors"]
        return Project(name, desc, dep, dev_dep, legal, authors)

