#nutrition_facts

class invalidFood(Exception):
	pass

def get_nutrition(item=None):

        if item is None:
                raise invalidFood("You have entered an invalid food item")

        elif item == "mango":
                return {'Serving size': '1 ounce (28 g)',
						'Calories': '163',
						'Calories from Fat': '119',
						'Total Fat': '2g 3%',
						'Total Carbohydrate': '12g 4%',
						'Cholesterol': '10mg 4%',
						'Dietary Fiber': '0g 0%',
						'Sodium': '125mg 5%',
						'Sugars': '12g',
						'Protein': '11g',
						'Vitamin A': '10%',
						'Calcium': '30%',
						'Vitamin C': '0%',
						'Iron': '0%'}

        else:
                print("Thanks")





