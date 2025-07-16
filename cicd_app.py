from flask import Flask, render_template_string

app = Flask(__name__)

html = '''
<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>CI/CD Pipeline Overview</title>
    <style>
        body {
            font-family: 'Segoe UI', sans-serif;
            background-color: #f4f6f8;
            margin: 0;
            padding: 20px;
        }
        .container {
            max-width: 900px;
            margin: auto;
            background: #fff;
            padding: 30px;
            border-radius: 10px;
            box-shadow: 0 4px 12px rgba(0,0,0,0.1);
        }
        h1 {
            color: #2c3e50;
        }
        p {
            font-size: 16px;
            line-height: 1.6;
            color: #34495e;
        }
        .footer {
            margin-top: 40px;
            font-size: 13px;
            color: #888;
            text-align: center;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>What is a CI/CD Pipeline?</h1>
        <p>
            CI/CD stands for <strong>Continuous Integration</strong> and <strong>Continuous Deployment (or Delivery)</strong>.
            It is a method to frequently deliver apps to customers by introducing automation into the stages of app development.
        </p>
        <p>
            The key concepts attributed to CI/CD are:
            <ul>
                <li><strong>CI (Continuous Integration):</strong> Developers frequently push code changes to a shared repository. Automated builds and tests run to validate the changes.</li>
                <li><strong>CD (Continuous Delivery/Deployment):</strong> Once validated, code is automatically delivered to production or staging environments with minimal human intervention.</li>
            </ul>
        </p>
        <p>
            CI/CD helps teams release software quickly, efficiently, and with higher confidence.
            Popular tools include Jenkins, GitHub Actions, GitLab CI, Travis CI, CircleCI, etc.
        </p>

        <div class="footer">
            Deployed via CI/CD Pipeline | Flask App © 2025
        </div>
    </div>
</body>
</html>
'''

@app.route('/')
def home():
    return render_template_string(html)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
