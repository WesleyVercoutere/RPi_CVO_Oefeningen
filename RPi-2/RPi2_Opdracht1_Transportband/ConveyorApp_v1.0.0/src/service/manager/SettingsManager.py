class SettingsManager:

    def __init__(self):
        default_settings = '{"1":"001","2":"010" , "3":"100"}'
        try:
            f = open("resources/settings.txt", "rt")
            print("File settings.txt exists!")
            current_settings = f.read()
            print("Settings are", current_settings)
            f.close()
        except FileNotFoundError:
            print("File settings.txt not exists, now we create it and save default settings!")
            f = open("resources/settings.txt", "wt")
            f.write(default_settings)
            f.close()
            print("File settings.txt made!")
            print("Settings are", default_settings)
            current_settings = default_settings


if __name__ == "__main__":
    SettingsManager()