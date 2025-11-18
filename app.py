from flask import Flask,render_template,url_for,request,redirect
import sqlite3

def init_db():

  with sqlite3.connect("Student.db") as connection:
    cursor=connection.cursor()
    cursor.execute("DROP TABLE IF EXISTS student")
        # Create new table with new column
    cursor.execute("""CREATE TABLE student(
    UNI INTEGER PRIMARY KEY,  
    NAME TEXT NOT NULL,
    AGE INTEGER NOT NULL,
    COURSE TEXT NOT NULL
    ) """)
    connection.commit()
#  Calling the  DB method to initialized the DB
init_db()

# initializing the fask object
app=Flask(__name__)

# Home page
@app.route('/')
def home():
  return render_template('Home.html')

@app.route('/form',methods=['GET','POST'])
def form():
  return render_template('Form.html')

@app.route('/submit',methods=['GET','POST'])
def Submit():
  name=request.form['name']
  age=int(request.form['age'])
  course=request.form['course']
  uni_no=int(request.form['uni_no'])
  if len(course)>50:
    return f'The Course Name is Not Valid'
  try:
    with sqlite3.connect("Student.db") as connection:
      cursor=connection.cursor()
      cursor.execute('INSERT INTO student(UNI,NAME,AGE,COURSE) values(?,?,?,?)',[uni_no,name,age,course])
      connection.commit()
      return redirect('/get_data')
  except Exception as e:
    print('The is error is ------->',e)
    return render_template('NOTFOUNT.html')

  # finally:

@app.route('/get_data')
def get_data():
  try:
    with sqlite3.connect('Student.db') as connection:
        cursor= connection.cursor()
        cursor.execute('SELECT  * From student')
        data=cursor.fetchall()
        return render_template('getData.html',data=data)

  except  Exception as e:
    print("The error is .........",e)  
    return f'Their Might Be some error'
  
@app.route('/delete_Data_Row')
def delete_Data_Row():
  return render_template('Delete_data.html')

@app.route('/delete',methods=['POST','GET'])
def delete_data():
  uni_no=int(request.form['uni_no'])
  try:
    with sqlite3.connect('Student.db') as connection:
      cursor=connection.cursor()
      cursor.execute('SELECT * FROM student where UNI=?',(uni_no,))
      connection.commit()
      data=cursor.fetchone()

      if data is None:
        return render_template('NOTFOUNT.html')
      else:
        cursor.execute('DELETE FROM student WHERE UNI=?',(uni_no,))
        return redirect('/get_data')
  except Exception as e:
       return render_template('NOTFOUNT.html')


@app.route('/update')
def update():
  return render_template('UPDATE.html') 


@app.route('/update_data',methods=['GET','POST'])
def update_data():
  key=request.form['key']
  value=request.form['value']
  uni_no=int(request.form['uni_no'])
  if key=='AGE':
    value=int(value)
  key=key.upper()  
  with sqlite3.connect('Student.db') as connection:
    cursor=connection.cursor()
    try:
      cursor.execute("PRAGMA table_info(student)")
      valid_cols = [c[1] for c in cursor.fetchall()] 
      if key not in valid_cols:
        return render_template('NOTFOUNT.html')
      else:
        cursor.execute(f"UPDATE  student SET {key}=? where UNI=? ",(value,uni_no,))
      connection.commit()  
      return redirect('/get_data')
      
    except Exception as e:
      return f'the error is {e}'
  return f'The data is updated' 
    

if __name__=='__main__':
  app.run(debug=True)

