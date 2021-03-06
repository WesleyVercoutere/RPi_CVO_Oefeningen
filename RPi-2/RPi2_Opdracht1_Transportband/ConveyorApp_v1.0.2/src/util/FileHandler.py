import json


class FileHandler:

    def __init__(self, file):
        self.filePath = f"resources/{file}.txt"

    def read(self, defaultSettings):
        settings = None

        try:
            f = open(self.filePath,"rt")
            settings = json.loads(f.read())
            f.close()

        except:
            f = open(self.filePath,"wt")
            f.write(defaultSettings)
            f.close()

            settings = defaultSettings

        return settings

    def write(self, json):
        f = open(self.filePath,"wt")
        f.write(json)
        f.close()