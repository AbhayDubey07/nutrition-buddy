from flask import Flask, render_template, request
from food_data import get_nutrition  # make sure this function exists

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    total_calories = 0
    total_protein = 0
    meal_suggestions = []

    if request.method == "POST":
        meals = request.form.get("meals")
        if meals:
            meal_list = [meal.strip() for meal in meals.split(",")]
            for meal in meal_list:
                nutrition = get_nutrition(meal)
                total_calories += nutrition["calories"]
                total_protein += nutrition["protein"]

            # basic suggestion logic
            if total_protein < 60:
                meal_suggestions.append("Add more eggs, chicken, or paneer for protein.")
            if total_calories < 2000:
                meal_suggestions.append("Consider adding rice, potatoes, or oats for calories.")

    return render_template("index.html",
                           calories=total_calories,
                           protein=total_protein,
                           suggestions=meal_suggestions)

if __name__ == "__main__":
    app.run(debug=True)
    
