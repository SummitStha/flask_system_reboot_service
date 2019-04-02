from subprocess import Popen
from flask import Flask, request, render_template, Response

app = Flask(__name__)

@app.route('/')
def index():
    """ Function that renders the homepage """
    return render_template('home.html')


@app.route('/restart')
def run_script():
    """ Function to run the provided script """
    try:
        Process = Popen('scripts/execute.sh', shell=True)
        if Process.wait() != 0:
            output, error = Process.communicate()
            print(output, error)
        return render_template('success.html')
    except Exception as e:
        msg = "Error : {}".format(e)
        return Response("<center><h1>" + msg + "</h1></center>")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9000)

