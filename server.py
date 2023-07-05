from flask import *
import sqlite3
app=Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html");

@app.route("/add")
def add():
    return render_template("add.html")

@app.route("/savedetails",methods = ["POST","GET"])  
def saveDetails():  
    msg = "msg"  
    if request.method == "POST":  
        try:  
            name = request.form["name"]  
            email = request.form["email"]  
            department = request.form["department"]
            phone = request.form["phone"]

            with sqlite3.connect("employee.db") as con:  
                cur = con.cursor()  
                cur.execute("INSERT into EmployeeDetails (name, email, department, phone) values (?,?,?,?)",(name,email,department,phone))  
                con.commit()  
                msg = "Employee successfully Added"  
        except:  
            con.rollback()  
            msg = "We can not add the employee to the list"  
        finally:  
            return render_template("success.html",msg = msg)  
            con.close()

@app.route("/view")  
def view():  
    con = sqlite3.connect("employee.db")  
    con.row_factory = sqlite3.Row  
    cur = con.cursor()  
    cur.execute("select * from EmployeeDetails")  
    rows = cur.fetchall()  
    return render_template("view.html",rows = rows)


@app.route("/delete")  
def delete():  
    return render_template("delete.html")  
 
@app.route("/deleterecord",methods = ["POST"])  
def deleterecord():  
    id = request.form["id"]  
    with sqlite3.connect("employee.db") as con:  
        try:  
            cur = con.cursor()  
            cur.execute("delete from EmployeeDetails where id = ?",id)  
            msg = "record successfully deleted"  
        except:  
            msg = "can't be deleted"  
        finally:  
            return render_template("delete_record.html",msg = msg) 

@app.route("/edit", methods=["GET", "POST"])
def edit(id):
    if request.method == "GET":
        con = sqlite3.connect("employee.db")
        con.row_factory = sqlite3.Row
        cur = con.cursor()
        cur.execute("SELECT * from EmployeeDetails WHERE id=?",(id,))
        row = cur.fetchone()
        con.close()
        return render_template("edit.html", row=row)
    elif request.method == "POST":
        try:
            name = request.form["name"]
            email = request.form["email"]
            department = request.form["department"]
            phone = request.form["phone"]

            with sqlite3.connect("employee.db") as con:
                cur = con.cursor()
                cur.execute("UPDATE EmployeeDetails SET name=?, email=?, department=?, phone=? WHERE id=?",
                            (name, email, department, phone, id))
                con.commit()
                msg = "Employee details successfully updated"
        except:
            con.rollback()
            msg = "Unable to update employee details"
        finally:
            return render_template(view.html)
        
if __name__=="__main__":
    app.run(debug=True)
