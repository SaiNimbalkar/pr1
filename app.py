from flask import Flask, request, render_template_string

app = Flask(__name__)

form_html = '''
<form method="POST">
    Name: <input type="text" name="name"><br>
    Email: <input type="email" name="email"><br>
    <input type="submit" value="Register">
</form>
'''

@app.route("/", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        return f"Registered {name} with {email}"
    return render_template_string(form_html)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)