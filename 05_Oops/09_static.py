class ChaiUtils:
    @staticmethod
    def clean_ingredients(text):
       return [item.strip() for item in text.split(",")]

raw="water , milk  , ginger , honey "

# obj=ChaiUtils()
# obj.clean_ingredients(raw) self laga dena method arguments mai

cleaned=ChaiUtils.clean_ingredients(raw) #static method not used when we initialize an objectf
print(cleaned)