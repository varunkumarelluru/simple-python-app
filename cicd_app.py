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
            background-color: #181a1b;
            margin: 0;
            padding: 0;
            min-height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
        }
        .main-wrapper {
            width: 100vw;
            min-height: 100vh;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            background: #181a1b;
        }
        .heading-box {
            background: #23272f;
            color: #fff;
            padding: 18px 32px 12px 32px;
            border-radius: 22px;
            box-shadow: 0 4px 16px rgba(0,0,0,0.25);
            font-size: 2rem;
            font-weight: 700;
            letter-spacing: 1px;
            text-align: center;
            margin-bottom: 22px;
            max-width: 900px;
            width: 100%;
        }
        .container {
            max-width: 900px;
            width: 100%;
            background: #23272f;
            padding: 22px 40px 22px 40px;
            border-radius: 22px;
            box-shadow: 0 4px 16px rgba(0,0,0,0.25);
            display: flex;
            flex-direction: column;
            align-items: center;
        }
        h1 {
            color: #f7ca18;
            margin-top: 0;
            margin-bottom: 18px;
            text-align: center;
            font-size: 1.3rem;
        }
        p, ul, li {
            font-size: 1rem;
            line-height: 1.6;
            color: #e0e0e0;
        }
        ul {
            margin-top: 0.5em;
            margin-bottom: 0.5em;
        }
        .footer {
            margin-top: 28px;
            font-size: 12px;
            color: #aaa;
            text-align: center;
        }
        strong {
            color: #f7ca18;
        }
        @media (max-width: 1000px) {
            .container, .heading-box {
                max-width: 98vw;
                padding-left: 8px;
                padding-right: 8px;
            }
        }
    </style>
</head>
<body>
    <div class="main-wrapper">
        <div class="heading-box">CI/CD Integration</div>
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
                CI/CD helps teams release software quickly, efficiently, and with higher confidence.<br>
                Popular tools include Jenkins, GitHub Actions, GitLab CI, etc.
            </p>
            <div class="footer">
                Deployed via CI/CD Pipeline | Flask App © 2025
            </div>
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
