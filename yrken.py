class Bard:
    def __init__(self, name):
        self.name = name
        self.skills = {
            "Bluffa": "KAR",
            "Främmande Språk": "INT",
            "Hoppa och klättra": "SMI",
            "Kniv": "SMI",
            "Myter och legender": "INT",
            "Undvika": "SMI",
            "Uppträda": "KAR"
        }

    def show_skills(self):
        """Prints all skills with their associated attributes."""
        print(f"{self.name} (Bard) has the following skills:")
        for skill, attribute in self.skills.items():
            print(f" - {skill} ({attribute})")

    def add_skill(self, skill_name, attribute):
        """Adds a new skill to the bard."""
        if skill_name not in self.skills:
            self.skills[skill_name] = attribute
            print(f"{self.name} learned {skill_name} ({attribute})!")
        else:
            print(f"{self.name} already knows {skill_name}.")
class Hantverkare:
    def __init__(self, name):
        self.name = name
        self.skills = {
            "Fingerfärdighet": "SMI",
            "Finna dolda ting": "INT",
            "Hammare": "STY",
            "Hantverk": "STY",
            "Kniv": "SMI",
            "Slagsmål": "STY",
            "Svärd": "STY",
            "Yxa": "STY"
        }

    def show_skills(self):
        print(f"{self.name} (Craftsman) has the following skills:")
        for skill, attribute in self.skills.items():
            print(f" - {skill} ({attribute})")

        # Add skill in charecter creation
    def add_skill(self, skill_name, attribute):
        if skill_name not in self.skills:
            self.skills[skill_name] = attribute
            print(f"{self.name} learned {skill_name} ({attribute})!")
        else:
            print(f"{self.name} already knows {skill_name}.")
class Jägare:
    def __init__(self, name):
        self.name = name
        self.skills = {
            "Hoppa och klättra": "SMI",
            "Jakt och fiske": "SMI",
            "Kniv": "SMI",
            "Pilbåge": "SMI",
            "Slunga": "SMI",
            "Smyga": "SMI",
            "Upptäcka fara": "INT",
            "Vildmarksvana": "INT"
        }

    def show_skills(self):
        """Prints all skills with their associated attributes."""
        print(f"{self.name} (Hunter) has the following skills:")
        for skill, attribute in self.skills.items():
            print(f" - {skill} ({attribute})")

    def add_skill(self, skill_name, attribute):
        """Adds a new skill to the hunter."""
        if skill_name not in self.skills:
            self.skills[skill_name] = attribute
            print(f"{self.name} learned {skill_name} ({attribute})!")
        else:
            print(f"{self.name} already knows {skill_name}.")



if __name__ == "__main__":
    pass