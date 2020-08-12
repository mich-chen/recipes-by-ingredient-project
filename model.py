"""Models for ingredient recipe app"""

from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class User(db.Model):
    """A user."""

    __tablename__ = 'users'

    user_id = db.Column(db.Integer,
                         autoincrement=True,
                         primary_key=True)
    email = db.Column(db.String)
    password = db.Column(db.String)
    name = db.Column(db.String)

    def __repr__(self):
        return f'<User user_id={self.user_id} email={self.email}>'


class Users_Recipe(db.Model):
    """User's selected recipes."""

    __tablename__ = 'users_recipes'

    user_recipe_id = db.Column(db.Integer,
                         autoincrement=True,
                         primary_key=True)
    recipe_id = db.Column(db.Integer,
                          db.ForeignKey('recipes.recipe_id'))
    user_id = db.Column(db.Integer,
                              db.ForeignKey('users.user_id'))
    favorite = db.Column(db.Boolean)

    def __repr__(self):
        return f'<User"s selected recipes recipe={self.recipe_id} user={self.user_id} is_favorite={self.favorite}>'


class Recipe(db.Model):
    """A recipe."""

    __tablename__ = 'recipes'

    recipe_id = db.Column(db.Integer,
                         autoincrement=True,
                         primary_key=True)
    title = db.Column(db.String)
    image = db.Column(db.String)
    serverings = db.Column(db.Integer)

    def __repr__(self):
        return f'<Recipe recipe_id={self.recipe_id} title={self.title}>'


class Ingredient(db.Model):
    """An Ingredient."""

    __tablename__ = 'ingredients'

    ingredient_id = db.Column(db.Integer,
                         autoincrement=True,
                         primary_key=True)
    name = db.Column(db.String)

    def __repr__(self):
        return f'<Ingredient ingredient_id={self.ingredient_id} name={self.name}>'


class Recipe_Ingredient(db.Model):
    """A recipe's ingredient."""

    __tablename__ = 'recipe_ingredients'

    rec_ing_id = db.Column(db.Integer,
                         autoincrement=True,
                         primary_key=True)
    recipe_id = db.Column(db.Integer,
                          db.ForeignKey('recipes.recipe_id'))
    ingredient_id = db.Column(db.Integer,
                              db.ForeignKey('ingredients.ingredient_id'))
    amount = db.Column(db.Integer)
    unit = db.Column(db.String)

    def __repr__(self):
        return f'<Recipe Ingredient recipe={self.recipe_id} ingredient={self.ingredient_id}>'


class Instructions(db.Model):
    """A recipe's instructions"""

    __tablename__ = 'instructions'

    instruction_id = db.Column(db.Integer,
                         autoincrement=True,
                         primary_key=True)
    recipe_id = db.Column(db.Integer,
                          db.ForeignKey('recipes.recipe_id'))
    step_num = db.Column(db.Integer)
    step_instruction = db.Column(db.String)
    cooking_mins = db.Column(db.Integer)
    prep_mins = db.Column(db.Integer)
    ready_mins = db.Column(db.Integer)
    equipment = db.Column(db.String)

    def __repr__(self):
        return f'<Instructions recipe={self.recipe_id} step={self.step_num}>'



