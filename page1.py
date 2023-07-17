def get_user_preferences():
    preferences = {}

    print("Welcome to the Personalized Meal Planner!")
    print("Let's gather some information about your dietary restrictions, preferences, and body goals.")

    preferences['dietary_restrictions'] = input("Do you have any dietary restrictions? (vegan, gluten-free, vegetarian, meat, pescatarian): ")
    preferences['food_preferences'] = input("What are your food preferences? (e.g., Mediterranean, Asian, comfort food): ")
    preferences['body_goals'] = input("What are your body goals? (e.g., weight loss, muscle gain, maintenance): ")
    preferences['height'] = float(input("Please enter your height (in cm): "))
    preferences['weight'] = float(input("Please enter your weight (in kg): "))

    return preferences


def calculate_calorie_intake(weight, height, body_goals):
    # Custom logic to calculate calorie intake based on body goals and other factors
    if body_goals == 'weight loss':
        calorie_intake = weight * 22
    elif body_goals == 'muscle gain':
        calorie_intake = weight * 25
    else:
        calorie_intake = weight * 20

    return calorie_intake


def generate_vegan_meal_plan():
    meal_plan = [
        "Breakfast: Overnight oats with almond milk, chia seeds, and mixed berries",
        "Lunch: Quinoa salad with roasted vegetables and avocado",
        "Dinner: Chickpea curry with brown rice",
        "Snack: Hummus with carrot sticks",
        "Snack: Mixed nuts and seeds"
    ]

    return meal_plan


def generate_gluten_free_meal_plan():
    meal_plan = [
        "Breakfast: Gluten-free toast with avocado and smoked salmon",
        "Lunch: Quinoa bowl with grilled chicken, mixed greens, and lemon dressing",
        "Dinner: Grilled salmon with quinoa and roasted asparagus",
        "Snack: Rice cakes with almond butter",
        "Snack: Fresh fruit salad"
    ]

    return meal_plan


def generate_vegetarian_meal_plan():
    meal_plan = [
        "Breakfast: Veggie omelette with spinach, mushrooms, and feta cheese",
        "Lunch: Caprese salad with tomatoes, mozzarella, and basil",
        "Dinner: Lentil bolognese with whole wheat pasta",
        "Snack: Greek yogurt with honey and granola",
        "Snack: Vegetable crudites with tzatziki dip"
    ]

    return meal_plan


def generate_meat_meal_plan():
    meal_plan = [
        "Breakfast: Scrambled eggs with bacon and whole wheat toast",
        "Lunch: Grilled chicken salad with mixed greens and balsamic vinaigrette",
        "Dinner: Steak with roasted potatoes and steamed broccoli",
        "Snack: Protein shake with whey protein and almond milk",
        "Snack: Cottage cheese with sliced fruit"
    ]

    return meal_plan


def generate_pescatarian_meal_plan():
    meal_plan = [
        "Breakfast: Smoked salmon and cream cheese bagel",
        "Lunch: Tuna salad with mixed greens and lemon dressing",
        "Dinner: Grilled shrimp skewers with quinoa and grilled vegetables",
        "Snack: Greek yogurt with fresh berries",
        "Snack: Edamame beans"
    ]

    return meal_plan


def main():
    preferences = get_user_preferences()

    calorie_intake = calculate_calorie_intake(preferences['weight'], preferences['height'], preferences['body_goals'])

    if preferences['dietary_restrictions'] == 'vegan':
        meal_plan = generate_vegan_meal_plan()
    elif preferences['dietary_restrictions'] == 'gluten-free':
        meal_plan = generate_gluten_free_meal_plan()
    elif preferences['dietary_restrictions'] == 'vegetarian':
        meal_plan = generate_vegetarian_meal_plan()
    elif preferences['dietary_restrictions'] == 'meat':
        meal_plan = generate_meat_meal_plan()
    elif preferences['dietary_restrictions'] == 'pescatarian':
        meal_plan = generate_pescatarian_meal_plan()
    else:
        print("Invalid dietary restriction.")
        return

    print("\nBased on your preferences and body goals, we recommend the following meal plan:")
    print("Calorie Intake: {} calories per day".format(calorie_intake))
    print("Meal Plan:")
    for meal in meal_plan:
        print("- " + meal)


if __name__ == "__main__":
    main()
