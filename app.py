import streamlit as ice_cream
from database import create_tables, add_flavor, get_flavors, add_suggestion, filter_flavors_by_ingredient, filter_flavors_by_allergen


create_tables()


ice_cream.title("Ice Cream Parlor")


def authenticate_admin(secret):
    if secret == "super_secret":
        return True
    return False

# Admin authentication
if ice_cream.sidebar.checkbox("Admin Authentication"):
    secret = ice_cream.sidebar.text_input("Enter Admin Secret", type="password")
    if authenticate_admin(secret):
        ice_cream.sidebar.success("Authentication Successful")
        add_option = ice_cream.sidebar.radio("Admin Options", ["Add Flavor", "Logout"])
        if add_option == "Add Flavor":
            ice_cream.subheader("Add New Flavor")
            flavor_name = ice_cream.text_input("Flavor Name")
            description = ice_cream.text_area("Description")
            available = ice_cream.checkbox("Available")
            ingredients = ice_cream.text_area("Ingredients (comma-separated)")
            allergens = ice_cream.text_area("Allergens (comma-separated)")
            if ice_cream.button("Add Flavor"):
                add_flavor(flavor_name, description, available, ingredients, allergens)
                ice_cream.success("Flavor Added Successfully")
    else:
        ice_cream.sidebar.error("Authentication Failed")

# Filter by Ingredient
ingredient_filter = ice_cream.checkbox("Filter by Ingredient", key="ingredient_filter_checkbox")
if ingredient_filter:
    all_ingredients = list(set([flavor[3] for flavor in get_flavors()]))
    selected_ingredient = ice_cream.selectbox("Select Ingredient", all_ingredients, index=0, key="ingredient_dropdown")
    if ice_cream.button("Apply Ingredient Filter", key="apply_ingredient_filter_button"):
        ice_cream.subheader(f"Flavors with Ingredient: {selected_ingredient}")
        filtered_flavors = filter_flavors_by_ingredient(selected_ingredient)
        if filtered_flavors:
            for flavor in filtered_flavors:
                ice_cream.write(flavor[0])  

# Filter by Allergen
allergen_filter = ice_cream.checkbox("Filter by Allergen", key="allergen_filter_checkbox")
if allergen_filter:
    all_allergens = list(set([flavor[4] for flavor in get_flavors()]))
    selected_allergen = ice_cream.selectbox("Select Allergen", all_allergens, index=0, key="allergen_dropdown")
    if ice_cream.button("Apply Allergen Filter", key="apply_allergen_filter_button"):
        ice_cream.subheader(f"Flavors with Allergen: {selected_allergen}")
        filtered_flavors = filter_flavors_by_allergen(selected_allergen)
        if filtered_flavors:
            for flavor in filtered_flavors:
                ice_cream.write(flavor[0]) 

# Main content
ice_cream.header("Explore Flavors")
all_flavors = [flavor[0] for flavor in get_flavors()]
selected_flavor = ice_cream.selectbox("Select Flavor", all_flavors, index=0, key="flavor_dropdown")
# Display selected flavor details
if selected_flavor:
    flavor_details = get_flavors(selected_flavor)[0]
    flavor_name, description, available, ingredients, allergens = flavor_details
    ice_cream.write(f"Flavor Name: {flavor_name}")
    ice_cream.write(f"Description: {description}")
    ice_cream.write(f"Available: {'Yes' if available else 'No'}")
    ice_cream.write(f"Ingredients: {ingredients}")
    ice_cream.write(f"Allergens: {allergens}")
    
    if ice_cream.button("Add to Cart", key="add_to_cart_button"):
        selected_flavors = ice_cream.session_state.get("selected_flavors", [])
        selected_flavors.append(flavor_name)
        ice_cream.session_state.selected_flavors = selected_flavors
        ice_cream.success(f"{flavor_name} added to cart!")

# User Suggestions
ice_cream.header("User Suggestions")
customer_name = ice_cream.text_input("Your Name", key="customer_name_input")
suggestion = ice_cream.text_area("Suggestion", key="suggestion_text_area")
suggested_flavors = [flavor[0] for flavor in get_flavors()]
selected_flavor_suggestion = ice_cream.selectbox("Select Flavor", suggested_flavors, index=0, key="flavor_suggestion_dropdown")
allergy_concerns = ice_cream.text_area("Allergy Concerns", key="allergy_concerns_text_area")
if ice_cream.button("Submit Suggestion", key="submit_suggestion_button"):
    add_suggestion(1, customer_name, selected_flavor_suggestion, suggestion, allergy_concerns)
    ice_cream.success("Suggestion Submitted Successfully")

# View Cart
ice_cream.sidebar.header("Your Cart")
selected_flavors = ice_cream.session_state.get("selected_flavors", [])
for flavor in selected_flavors:
        ice_cream.sidebar.write(flavor)
