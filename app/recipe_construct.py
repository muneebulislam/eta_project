from app.Edamam import Edamam
from app.Exceptions import APIError, LowQualityQuery

class Recipe:

    def __init__(self, recipe_app_id, recipe_app_key, nutrition_id, nutrition_key):
        """
        Purposes:
            Initialize the app. Including the app window, search bar, search button, and welcome image showing.
        Pre-conditions:
            None
        Post_conditions:
            None
        Return: None
        """

        # The whole window of the app
        self.recipe_app_id = recipe_app_id
        self.recipe_app_key = recipe_app_key
        self.nutrition_id = nutrition_id
        self.nutrition_key = nutrition_key

    def run_search_query(self, query):
        """
        Purpose:
            Search on the website for a recipe that matches with user's input.
        Pre-conditions:
            None
        Post_conditions:
            None
        Return: None
        """
        recipe_list = self.__get_recipe(query)
        return recipe_list

    def __get_recipe(self, query):
        """
        Purpose:
            Gets the recipe(s) that matches user input string.
        Pre-conditions:
            :param query: the string that the user inputs into the search bar
        Post_conditions:
            None
        Return: recipe_list - a list of recipes that matches with the user input
        """

        # Uses edamam API to do the searches
        edamam_object = Edamam(recipes_appid=self.recipe_app_id, recipes_appkey=self.recipe_app_key)
        query_result = edamam_object.search_recipe(query)

        recipe_list = []
        # Returns a list of recipes that matches the input string if the recipe was found
        if query_result["hits"]:
            for r in range(len(query_result)):
                recipe_name = query_result["hits"][r]
                recipe_list.append(recipe_name)

        # Appends "Empty" to the list of recipes if the recipe was not found
        else:
            recipe_name = "Empty"
            recipe_list.append(recipe_name)
        return recipe_list

# Create App and run the app
if __name__ == "__main__":
    # API Keys
    APP_ID = "a8ee5e3a"  # Put your app id for edamam api
    APP_KEY = "a5af30bf418171d4c205bb8c27cb02f2"  # Put your app key for edamam api

    NUTRITION_ID = "70dc1ef4"
    NUTRITION_KEY = "aeff761abf4758bc4076d53add38585e"

    recipe_app = Recipe(APP_ID, APP_KEY, NUTRITION_ID, NUTRITION_KEY)
