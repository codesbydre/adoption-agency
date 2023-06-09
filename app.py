from flask import Flask, render_template, redirect, flash, url_for
from models import Pet, db, connect_db
from forms import AddPetForm, EditPetForm
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adopt'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = "secret123"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

connect_db(app)
# db.create_all()

@app.route("/")
def list_pets():
    pets = Pet.query.all()
    return render_template("home.html", pets=pets)

@app.route("/add", methods=["GET", "POST"])
def add_pet():
    form = AddPetForm()

    if form.validate_on_submit():
        pet = Pet(name=form.name.data, species=form.species.data, photo_url=form.photo_url.data or None, age=form.age.data, notes=form.notes.data, available=True)
        db.session.add(pet)
        db.session.commit()
        flash(f"Added {pet.name}", "success")
        return redirect(url_for('list_pets'))

    else:
        return render_template("add_pet_form.html", form=form)

@app.route("/<int:pet_id>", methods=["GET", "POST"])
def edit_pet(pet_id):
    pet = Pet.query.get_or_404(pet_id)
    form = EditPetForm(obj=pet)

    if form.validate_on_submit():
        pet.photo_url = form.photo_url.data
        pet.notes = form.notes.data
        pet.available = form.available.data
        db.session.commit()
        flash(f"Updated {pet.name}", "success")
        return redirect(url_for('list_pets'))

    else:
        return render_template("edit_pet_form.html", form=form, pet=pet)

@app.route("/<int:pet_id>/details", methods=["GET"])
def show_pet(pet_id):
    pet = Pet.query.get_or_404(pet_id)
    return render_template("pet_detail.html", pet=pet)
