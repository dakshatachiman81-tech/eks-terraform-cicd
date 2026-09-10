from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <title>DevOps Cloud Platform - v3</title>

    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: "Segoe UI", Arial, sans-serif;
            background: linear-gradient(135deg, #eff6ff, #f5f3ff, #e0f2fe);
            color: #1e293b;
            min-height: 100vh;
        }

        .container {
            width: 90%;
            max-width: 1100px;
            margin: auto;
        }

        /* Header */

        header {
            border-bottom: 1px solid #dbeafe;
            background: rgba(255, 255, 255, 0.95);
        }

        .navbar {
            height: 70px;
            display: flex;
            align-items: center;
            justify-content: space-between;
        }

        .logo {
            font-size: 21px;
            font-weight: 700;
            color: #172554;
            letter-spacing: 0.5px;
        }

        .logo span {
            color: #2563eb;
        }

        .status {
            display: flex;
            align-items: center;
            gap: 8px;
            font-size: 14px;
            color: #64748b;
        }

        .status-dot {
            width: 9px;
            height: 9px;
            background: #22c55e;
            border-radius: 50%;
            box-shadow: 0 0 10px rgba(34, 197, 94, 0.5);
        }

        /* Hero */

        .hero {
            padding: 85px 0 55px;
            text-align: center;
        }

        .badge {
            display: inline-block;
            padding: 7px 15px;
            border: 1px solid #93c5fd;
            border-radius: 20px;
            color: #2563eb;
            font-size: 13px;
            margin-bottom: 22px;
            background: rgba(239, 246, 255, 0.9);
        }

        .hero h1 {
            font-size: clamp(38px, 6vw, 64px);
            line-height: 1.1;
            font-weight: 750;
            color: #172554;
            margin-bottom: 20px;
        }

        .hero h1 span {
            color: #2563eb;
        }

        .hero p {
            max-width: 650px;
            margin: auto;
            color: #64748b;
            font-size: 17px;
            line-height: 1.7;
        }

        /* Cards */

        .cards {
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 18px;
            margin: 25px 0 65px;
        }

        .card {
            background: rgba(255, 255, 255, 0.92);
            border: 1px solid #dbeafe;
            border-radius: 12px;
            padding: 25px;
            transition: 0.25s ease;
            box-shadow: 0 8px 25px rgba(37, 99, 235, 0.06);
        }

        .card:hover {
            transform: translateY(-4px);
            border-color: #60a5fa;
            box-shadow: 0 12px 30px rgba(37, 99, 235, 0.12);
        }

        .icon {
            font-size: 25px;
            margin-bottom: 18px;
        }

        .card h3 {
            color: #172554;
            font-size: 17px;
            margin-bottom: 8px;
        }

        .card p {
            color: #64748b;
            font-size: 13px;
        }

        .card .online {
            color: #16a34a;
            font-size: 13px;
            margin-top: 14px;
            font-weight: 600;
        }

        /* Architecture */

        .architecture {
            background: rgba(255, 255, 255, 0.92);
            border: 1px solid #dbeafe;
            border-radius: 14px;
            padding: 35px;
            margin-bottom: 70px;
            box-shadow: 0 8px 25px rgba(37, 99, 235, 0.06);
        }

        .architecture h2 {
            text-align: center;
            color: #172554;
            margin-bottom: 30px;
            font-size: 25px;
        }

        .flow {
            display: flex;
            align-items: center;
            justify-content: center;
            flex-wrap: wrap;
            gap: 10px;
        }

        .flow-item {
            padding: 13px 18px;
            background: #eff6ff;
            border: 1px solid #93c5fd;
            border-radius: 8px;
            font-size: 14px;
            color: #1e40af;
            font-weight: 500;
        }

        .arrow {
            color: #2563eb;
            font-size: 20px;
        }

        /* Health */

        .health {
            text-align: center;
            padding-bottom: 70px;
        }

        .health h2 {
            color: #172554;
            margin-bottom: 12px;
        }

        .health p {
            color: #64748b;
            margin-bottom: 22px;
        }

        .health-button {
            display: inline-block;
            padding: 11px 22px;
            background: #2563eb;
            color: white;
            text-decoration: none;
            border-radius: 7px;
            font-size: 14px;
            font-weight: 600;
            transition: 0.2s ease;
            box-shadow: 0 5px 15px rgba(37, 99, 235, 0.2);
        }

        .health-button:hover {
            background: #1d4ed8;
            transform: translateY(-2px);
        }

        /* Footer */

        footer {
            border-top: 1px solid #dbeafe;
            background: rgba(255, 255, 255, 0.95);
            padding: 25px 0;
            text-align: center;
            color: #64748b;
            font-size: 13px;
        }

        footer span {
            color: #2563eb;
        }

        /* Responsive */

        @media (max-width: 850px) {
            .cards {
                grid-template-columns: repeat(2, 1fr);
            }
        }

        @media (max-width: 550px) {
            .cards {
                grid-template-columns: 1fr;
            }

            .hero {
                padding: 60px 0 40px;
            }

            .architecture {
                padding: 25px 15px;
            }
        }
    </style>
</head>

<body>

<header>
    <div class="container navbar">

        <div class="logo">
            Cloud<span>Ops</span>
        </div>

        <div class="status">
            <div class="status-dot"></div>
            System Operational
        </div>

    </div>
</header>


<main>

    <section class="hero container">

        <div class="badge">
            AWS Cloud & DevOps Platform
        </div>

        <h1>
          Modern Infrastructure.<br>
          <span>Automated Delivery. - v3</span>
        </h1>

        <p>
            A containerized Flask application deployed using Docker,
            Amazon ECR, Amazon EKS, Kubernetes, Terraform and
            GitHub Actions CI/CD.
        </p>

    </section>


    <section class="container">

        <div class="cards">

            <div class="card">
                <div class="icon">☁️</div>
                <h3>AWS EKS</h3>
                <p>Managed Kubernetes infrastructure</p>
                <div class="online">● Operational</div>
            </div>

            <div class="card">
                <div class="icon">🐳</div>
                <h3>Docker</h3>
                <p>Containerized application runtime</p>
                <div class="online">● Running</div>
            </div>

            <div class="card">
                <div class="icon">⚙️</div>
                <h3>Terraform</h3>
                <p>Infrastructure as Code automation</p>
                <div class="online">● Managed</div>
            </div>

            <div class="card">
                <div class="icon">🚀</div>
                <h3>CI/CD</h3>
                <p>Automated build and deployment</p>
                <div class="online">● Enabled</div>
            </div>

        </div>

    </section>


    <section class="container architecture">

        <h2>Deployment Architecture</h2>

        <div class="flow">

            <div class="flow-item">GitHub</div>

            <div class="arrow">→</div>

            <div class="flow-item">GitHub Actions</div>

            <div class="arrow">→</div>

            <div class="flow-item">Docker</div>

            <div class="arrow">→</div>

            <div class="flow-item">Amazon ECR</div>

            <div class="arrow">→</div>

            <div class="flow-item">Amazon EKS</div>

            <div class="arrow">→</div>

            <div class="flow-item">Application</div>

        </div>

    </section>


    <section class="health container">

        <h2>Application Health</h2>

        <p>
            The application health endpoint is available for
            Kubernetes readiness and liveness monitoring.
        </p>

        <a href="/health" class="health-button">
            Check Health
        </a>

    </section>

</main>


<footer>

    Built with <span>Flask</span> · Docker · Kubernetes · Terraform · AWS

</footer>

</body>
</html>
"""


@app.route("/health")
def health():
    return "Healthy"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)