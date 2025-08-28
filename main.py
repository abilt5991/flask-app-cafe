from flask import Flask, render_template, request, jsonify
import random
import sqlite3

app = Flask(__name__)

db = sqlite3.connect("my_cafe.db", check_same_thread=False)
cur = db.cursor()


# cur.execute("DROP TABLE IF EXISTS my_cafe;")
# db.commit()
#
# cur.execute("""
# CREATE TABLE my_cafe (
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     cafe TEXT,
#     location TEXT,
#     price TEXT
# )
# """)
# db.commit()

@app.route("/submit", methods=["POST"])
def add_cafe():
    cafe = request.form.get("name")
    location = request.form.get("location")
    price = request.form.get("price")
    cur.execute(
        "INSERT INTO my_cafe (cafe, location, price) VALUES (?, ?, ?)",
        (cafe, location, price)
    )
    db.commit()

    db.commit()
    return render_template("index.html")

@app.route("/add")
def add_form():
    return render_template("add.html")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/random", methods=["GET"])
def random_cafe():
    get_cafe = cur.execute("SELECT * FROM my_cafe ORDER BY RANDOM() LIMIT 1").fetchone()
    print(get_cafe)
    id,cafe,loc,price = get_cafe

    # return render_template("index.html")
    return jsonify(id=id,
                   cafe=cafe,
                   loc=loc,
                   price = price)

@app.route("/all", methods=["GET"])
def get_all_cafe():
    result = {}
    all_cafes = cur.execute("SELECT * FROM my_cafe").fetchall()
    for index, cafe in enumerate(all_cafes):
        id, cafename, loc, price = cafe
        result[str(index)] = {
                "id" : id,
                "cafename" : cafename,
                "loc" : loc,
                "price" : price,
            }
    return jsonify(result)

@app.route("/all-html")
def get_all_cafe_html():
    all_cafes = cur.execute("SELECT * FROM my_cafe").fetchall()
    # Pass the list of cafes to the template
    return render_template("all_cafes.html", cafes=all_cafes)

@app.route("/search/<loc>")
def get_loc_cafes(loc):
    loc_cafes_res = {}
    loc_cafes = cur.execute("SELECT * FROM my_cafe WHERE location = ?", (loc,)).fetchall()
    if loc_cafes:
        for index,loc in enumerate(loc_cafes):
            ind, cafe, location, price = loc
            loc_cafes_res[str(index)] = {
                "ind" : ind,
                "cafe" : cafe,
                "location" : location,
                "price" : price
            }
    else:
        loc_cafes_res["error"] = {
            "Not Found" : "No such location found"
        }
    print(loc_cafes)
    return jsonify(loc_cafes_res)

@app.route("/update-price/<int:cafe_id>", methods=["GET","PATCH"])
def update_cafe_price(cafe_id):
    new_price = request.args.get("new_price")
    update_price = cur.execute("UPDATE my_cafe SET price = ? WHERE id = ?", (new_price, cafe_id))
    db.commit()
    return jsonify(success=True, updated_price=new_price)

if __name__ == "__main__":
    app.run(debug = True)
