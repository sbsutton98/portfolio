from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/<string:page_name>')
def html(page_name):
    return render_template(page_name)


def write_to_file(data):
    with open('data.txt', 'a') as data:
        email = data['email']
        subject = data['subject']
        message = data['message']
        file = data.write(f'\n{email},{subject},{message}')


def write_to_csv(data):
    with open('data.csv', 'a', newline='') as data2:
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_writer = csv.writer(data2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            # write_to_file(data)
            write_to_csv(data)
            return redirect('/thankyou.html')
        except:
            return 'did not save'
    else:
        'you don messed up'
