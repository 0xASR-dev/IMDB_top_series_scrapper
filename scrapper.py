import pandas as pd
from jinja2 import Template
import requests
from bs4 import BeautifulSoup


url='https://www.imdb.com/chart/toptv/'
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
    "Accept-Language": "en-US,en;q=0.5"
}
data = requests.get(url,headers=headers)
print(data.status_code)

html = data.text

webseries= BeautifulSoup(html, 'html.parser')

fseries_data=webseries.find_all('li', class_='ipc-metadata-list-summary-item')
title=[]
release=[]
episodes=[]
S_rating=[]
for i in fseries_data:
  title.append(i.find('h3', class_='ipc-title__text').text)
  release.append(i.find_all('div',class_='hTMtRz')[0].find_all('span')[0].text)
  episodes.append(i.find_all('div',class_='hTMtRz')[0].find_all('span')[1].text)
  S_rating.append(i.find_all('div',class_='hTMtRz')[0].find_all('span')[2].text)



df = pd.DataFrame({
    "s_title" : title,
    "s_release" : release,
    "s_episodes" : episodes,
    "s_rating" : S_rating
})

df.to_csv('top_25_webseries.csv', index=False)

html_template = """
<!DOCTYPE html>
<html lang="en" data-theme="light">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Top 25 Web Series</title>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    <style>
        :root {
            --bg-primary: #fafafa;
            --bg-secondary: #ffffff;
            --bg-table-header: #f5f5f7;
            --text-primary: #1d1d1f;
            --text-secondary: #6e6e73;
            --border-color: #e5e5e7;
            --shadow: 0 4px 20px rgba(0, 0, 0, 0.08);
            --hover-bg: #f0f0f2;
            --accent: #f5c518;
            --transition: all 0.3s ease;
        }

        [data-theme="dark"] {
            --bg-primary: #1a1a1d;
            --bg-secondary: #2c2c2e;
            --bg-table-header: #3a3a3c;
            --text-primary: #f5f5f7;
            --text-secondary: #a1a1a6;
            --border-color: #3a3a3c;
            --shadow: 0 4px 20px rgba(0, 0, 0, 0.3);
            --hover-bg: #3a3a3c;
        }

        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
            background-color: var(--bg-primary);
            color: var(--text-primary);
            min-height: 100vh;
            padding: 40px 20px;
            transition: var(--transition);
        }

        .container {
            max-width: 1200px;
            margin: 0 auto;
        }

        .header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 40px;
            flex-wrap: wrap;
            gap: 20px;
        }

        .title-section {
            display: flex;
            align-items: center;
            gap: 15px;
        }

        .imdb-badge {
            background: var(--accent);
            color: #000;
            padding: 8px 12px;
            border-radius: 8px;
            font-weight: 700;
            font-size: 14px;
            letter-spacing: 1px;
        }

        h1 {
            font-size: 2.5rem;
            font-weight: 700;
            letter-spacing: -0.5px;
        }

        .subtitle {
            color: var(--text-secondary);
            font-size: 1rem;
            margin-top: 8px;
            font-weight: 400;
        }

        .theme-toggle {
            display: flex;
            align-items: center;
            gap: 12px;
            background: var(--bg-secondary);
            padding: 10px 20px;
            border-radius: 50px;
            box-shadow: var(--shadow);
            cursor: pointer;
            transition: var(--transition);
        }

        .theme-toggle:hover {
            transform: translateY(-2px);
        }

        .toggle-label {
            font-size: 14px;
            font-weight: 500;
            color: var(--text-secondary);
        }

        .toggle-switch {
            position: relative;
            width: 50px;
            height: 26px;
            background: var(--border-color);
            border-radius: 50px;
            transition: var(--transition);
        }

        .toggle-switch::after {
            content: '';
            position: absolute;
            top: 3px;
            left: 3px;
            width: 20px;
            height: 20px;
            background: white;
            border-radius: 50%;
            transition: var(--transition);
            box-shadow: 0 2px 4px rgba(0,0,0,0.2);
        }

        [data-theme="dark"] .toggle-switch {
            background: var(--accent);
        }

        [data-theme="dark"] .toggle-switch::after {
            left: 27px;
        }

        .toggle-icon {
            font-size: 18px;
        }

        .header-actions {
            display: flex;
            align-items: center;
            gap: 16px;
        }

        .download-btn {
            display: flex;
            align-items: center;
            gap: 8px;
            background: linear-gradient(135deg, var(--accent) 0%, #e6b800 100%);
            color: #000;
            padding: 12px 24px;
            border-radius: 50px;
            font-weight: 600;
            font-size: 14px;
            text-decoration: none;
            box-shadow: var(--shadow);
            transition: var(--transition);
            cursor: pointer;
            border: none;
        }

        .download-btn:hover {
            transform: translateY(-2px);
            box-shadow: 0 6px 25px rgba(245, 197, 24, 0.4);
        }

        .download-btn svg {
            width: 18px;
            height: 18px;
        }

        .table-container {
            background: var(--bg-secondary);
            border-radius: 16px;
            box-shadow: var(--shadow);
            overflow: hidden;
            transition: var(--transition);
        }

        table {
            width: 100%;
            border-collapse: collapse;
        }

        th, td {
            padding: 18px 24px;
            text-align: left;
            border-bottom: 1px solid var(--border-color);
            transition: var(--transition);
        }

        th {
            background-color: var(--bg-table-header);
            font-weight: 600;
            font-size: 13px;
            text-transform: uppercase;
            letter-spacing: 0.5px;
            color: var(--text-secondary);
        }

        td {
            font-size: 15px;
        }

        tbody tr {
            transition: var(--transition);
        }

        tbody tr:hover {
            background-color: var(--hover-bg);
        }

        tbody tr:last-child td {
            border-bottom: none;
        }

        .title-cell {
            font-weight: 600;
            color: var(--text-primary);
        }

        .rating-cell {
            display: inline-flex;
            align-items: center;
            gap: 6px;
            background: linear-gradient(135deg, var(--accent) 0%, #e6b800 100%);
            color: #000;
            padding: 6px 12px;
            border-radius: 20px;
            font-weight: 600;
            font-size: 14px;
        }

        .rating-cell::before {
            content: '★';
        }

        .index-cell {
            font-weight: 700;
            color: var(--text-secondary);
            font-size: 14px;
            min-width: 50px;
        }

        .year-cell, .episodes-cell {
            color: var(--text-secondary);
            font-weight: 500;
        }

        .footer {
            text-align: center;
            margin-top: 40px;
            color: var(--text-secondary);
            font-size: 14px;
        }

        @media (max-width: 768px) {
            h1 {
                font-size: 1.75rem;
            }
            
            th, td {
                padding: 14px 16px;
            }
            
            .header {
                flex-direction: column;
                align-items: flex-start;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <div>
                <div class="title-section">
                    <span class="imdb-badge">IMDb</span>
                    <h1>Top 25 Web Series</h1>
                </div>
                <p class="subtitle">The highest-rated TV shows of all time</p>
            </div>
            <div class="header-actions">
                <a href="top_25_webseries.csv" download class="download-btn">
                    <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-4l-4 4m0 0l-4-4m4 4V4" />
                    </svg>
                    Download CSV
                </a>
                <div class="theme-toggle" onclick="toggleTheme()">
                    <span class="toggle-icon">☀️</span>
                    <div class="toggle-switch"></div>
                    <span class="toggle-icon">🌙</span>
                </div>
            </div>
        </div>

        <div class="table-container">
            <table>
                <thead>
                    <tr>
                        <th>#</th>
                        <th>Title</th>
                        <th>Release Year</th>
                        <th>Episodes</th>
                        <th>Rating</th>
                    </tr>
                </thead>
                <tbody>
                    {% for index, row in data.iterrows() %}
                    <tr>
                        <td class="index-cell">{{ index + 1 }}</td>
                        <td class="title-cell">{{ row.s_title }}</td>
                        <td class="year-cell">{{ row.s_release }}</td>
                        <td class="episodes-cell">{{ row.s_episodes }}</td>
                        <td><span class="rating-cell">{{ row.s_rating }}</span></td>
                    </tr>
                    {% endfor %}
                </tbody>
            </table>
        </div>

        <p class="footer">Data sourced from IMDb • Updated automatically</p>
    </div>

    <script>
        function toggleTheme() {
            const html = document.documentElement;
            const currentTheme = html.getAttribute('data-theme');
            const newTheme = currentTheme === 'light' ? 'dark' : 'light';
            html.setAttribute('data-theme', newTheme);
            localStorage.setItem('theme', newTheme);
        }

        // Load saved theme preference
        const savedTheme = localStorage.getItem('theme') || 'light';
        document.documentElement.setAttribute('data-theme', savedTheme);
    </script>
</body>
</html>
"""


template = Template(html_template)
html_output = template.render(data=df)
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html_output)