import re

FOOD_DATABASE = {
    "egg": {"calories": 78, "protein": 6},         # per piece
    "milk": {"calories": 42, "protein": 3.4},      # per 100ml
    "banana": {"calories": 89, "protein": 1.1},    # per 100g
    "rice": {"calories": 130, "protein": 2.7},     # per 100g cooked
    "chicken": {"calories": 239, "protein": 27},   # per 100g
    "paneer": {"calories": 265, "protein": 18}     # per 100g
}

def get_nutrition(item):
    item = item.lower().strip()

    # Extract quantity and unit using regex
    match = re.match(r"(\d+)\s*(g|gm|ml|piece|pieces)?\s*(.*)", item)
    if match:
        amount = int(match.group(1))
        unit = match.group(2) or "piece"
        food_name = match.group(3).strip()
    else:
        amount = 1
        unit = "piece"
        food_name = item

    data = FOOD_DATABASE.get(food_name)
    if not data:
        return {"calories": 0, "protein": 0}

    # Scale based on quantity
    if unit in ["ml"]:
        multiplier = amount / 100
    elif unit in ["g", "gm"]:
        multiplier = amount / 100
    elif unit in ["piece", "pieces"]:
        multiplier = amount
    else:
        multiplier = 1

    return {
        "calories": round(data["calories"] * multiplier, 2),
        "protein": round(data["protein"] * multiplier, 2)
    }
