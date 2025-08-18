from flask import Flask,jsonify
import sqlite3

app=Flask(__name__)

@app.route('/feedback')
def get_feedback():
    try:
        conn=sqlite3.connect('feedback.db')
        cursor=conn.cursor()

        cursor.execute("SELECT comment FROM feedback")
        feedback_list=cursor.fetchall()
        conn.close()
        return jsonify({"feedback":feedback_list})




    except sqlite3.Error as e:
        return jsonify({"error":"Database error occured","details":str(e)}),500

    except Exception as e:
        return jsonify({"error":"Something went wrong","details":str(e)}),500