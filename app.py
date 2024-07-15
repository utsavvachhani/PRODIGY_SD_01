from flask import Flask, render_template, request
import subprocess

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/run_script', methods=['POST'])
def run_script():
    script_name = request.form['script']
    try:
        if script_name == 'guessing_game':
            subprocess.run(['python', '/mnt/data/guessing_game.py'], check=True)
        elif script_name == 'temperature_converter':
            subprocess.run(['python', '/mnt/data/temperature_converter.py'], check=True)
        elif script_name == 'contact_manager':
            subprocess.run(['python', '/mnt/data/contact_manager.py'], check=True)
        return f'{script_name} script ran successfully!'
    except subprocess.CalledProcessError as e:
        return f'Error running {script_name} script: {str(e)}'

if __name__ == '__main__':
    app.run(debug=True)
