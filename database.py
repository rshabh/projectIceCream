import sqlite3

def create_tables():
    connection = sqlite3.connect('ice_cream_database.db')
    cursor = connection.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS SeasonalFlavors (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        flavor_name TEXT NOT NULL,
        description TEXT,
        is_available BOOLEAN NOT NULL CHECK (is_available IN (0, 1)),
        ingredients TEXT,
        allergens TEXT
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS CustomerSuggestions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        flavor_id INTEGER,
        customer_name TEXT NOT NULL,
        suggestion TEXT,
        allergy_concerns TEXT,
        FOREIGN KEY (flavor_id) REFERENCES SeasonalFlavors (id)
    )
    ''')

    connection.commit()
    connection.close()

def add_flavor(flavor_name, description, is_available, ingredients=None, allergens=None):
    connection = sqlite3.connect('ice_cream_database.db')
    cursor = connection.cursor()
    cursor.execute('''
    INSERT INTO SeasonalFlavors (flavor_name, description, is_available, ingredients, allergens)
    VALUES (?, ?, ?, ?, ?)
    ''', (flavor_name, description, is_available, ingredients, allergens))
    connection.commit()
    connection.close()

def add_suggestion(flavor_id, customer_name, suggestion, allergy_concerns):
    connection = sqlite3.connect('ice_cream_database.db')
    cursor = connection.cursor()
    cursor.execute('''
    INSERT INTO CustomerSuggestions (flavor_id, customer_name, suggestion, allergy_concerns)
    VALUES (?, ?, ?, ?)
    ''', (flavor_id, customer_name, suggestion, allergy_concerns))
    connection.commit()
    connection.close()

def get_flavors(search_term=None):
    connection = sqlite3.connect('ice_cream_database.db')
    cursor = connection.cursor()
    if search_term:
        cursor.execute('''
        SELECT flavor_name, description, is_available, ingredients, allergens FROM SeasonalFlavors
        WHERE flavor_name LIKE ? OR description LIKE ?
        ''', (f'%{search_term}%', f'%{search_term}%'))
    else:
        cursor.execute('SELECT flavor_name, description, is_available, ingredients, allergens FROM SeasonalFlavors')
    flavors = cursor.fetchall()
    connection.close()
    return flavors

def filter_flavors_by_ingredient(ingredient):
    connection = sqlite3.connect('ice_cream_database.db')
    cursor = connection.cursor()
    cursor.execute('''
    SELECT flavor_name, description, is_available, ingredients, allergens FROM SeasonalFlavors
    WHERE ingredients LIKE ?
    ''', (f'%{ingredient}%',))
    flavors = cursor.fetchall()
    connection.close()
    return flavors

def filter_flavors_by_allergen(allergen):
    connection = sqlite3.connect('ice_cream_database.db')
    cursor = connection.cursor()
    cursor.execute('''
    SELECT flavor_name, description, is_available, ingredients, allergens FROM SeasonalFlavors
    WHERE allergens LIKE ?
    ''', (f'%{allergen}%',))
    flavors = cursor.fetchall()
    connection.close()
    return flavors
