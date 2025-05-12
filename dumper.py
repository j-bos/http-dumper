from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def dump_environment_variables():
    # Collect HTTP environment variables
    env_vars = {key: value for key, value in request.environ.items()}
    # Format them as HTML for display
    response = "<h1>HTTP Environment Variables</h1>"
    response += "<ul>"
    for key, value in env_vars.items():
        response += f"<li><strong>{key}</strong>: {value}</li>"
    response += "</ul>"
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
