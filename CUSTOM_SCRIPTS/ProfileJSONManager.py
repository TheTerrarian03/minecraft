import json


DEF_PROF_JSON_NAME = "profiles.json"

def get_default_path_to_json():
    return __file__[:__file__.rfind("\\")+1] + DEF_PROF_JSON_NAME

class ProfileManager:
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = self._load_data()

    def _load_data(self):
        try:
            with open(self.file_path, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return {"profiles": {}}

    def save_changes(self):
        with open(self.file_path, 'w') as file:
            json.dump(self.data, file, indent=4)

    def add_profile(self, profile_name, player_name, shader_name, resource_pack, other_options=None):
        if other_options is None:
            other_options = {}

        self.data["profiles"][profile_name] = {
            "player_name": player_name,
            "shader_name": shader_name,
            "resource_pack": resource_pack,
            "other_options": other_options
        }
        self.save_changes()

    def update_profile(self, profile_name, bat_wifi: bool=False, bat_change_name: bool=False, bat_new_name: str="", optionstxt={}, optionsshaderstxt={}):
        profile = self.data["profiles"].get(profile_name, {})
        
        bat_options = {
            "disable_wifi": bat_wifi,
            "change_name": bat_change_name,
            "new_name": bat_new_name
        }

        profile["bat_options"] = bat_options
        
        if optionstxt is not None:
            profile["options.txt"] = optionstxt
        
        if optionsshaderstxt is not None:
            profile["optionsshaders.txt"] = optionsshaderstxt
        
        self.data["profiles"][profile_name] = profile
        self.save_changes()

    def delete_profile(self, profile_name):
        if profile_name in self.data["profiles"]:
            del self.data["profiles"][profile_name]
            self.save_changes()

    def get_profile_names(self):
        names = []
        for profile_name in self.data["profiles"]:
            names.append(profile_name)
        return names

    def get_data_for_profile(self, profile_name):
        try:
            return self.data["profiles"][profile_name]
        except:
            return {}
