from flask import Flask, render_template, request, jsonify
import yaml
import os

app = Flask(__name__)


@app.route('/save_yaml', methods=['POST'])
def save_yaml():

    data = request.json
    content = data.get('content', '')

    try:
        # Parse YAML to check for errors before saving
        yaml.safe_load(content)
        
        # Specify the filename and path
        file_path = os.path.join(app.root_path, 'static', 'data.yaml')
        
        with open(file_path, 'w') as file:
            file.write(content)
            
        return jsonify({'message': 'File saved successfully'}), 200
    except yaml.YAMLError as exc:
        return jsonify({'error': str(exc)}), 400
    except Exception as exc:
        return jsonify({'error': 'Error saving file'}), 500

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)