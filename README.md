# 🎬 IMDb Top 25 Web Series Scraper

A Python web scraper that fetches the top 25 highest-rated TV series from IMDb and generates a beautiful, responsive HTML page with dark/light mode support. Automatically updates weekly via GitHub Actions and deploys to GitHub Pages.

![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python&logoColor=white)
![GitHub Actions](https://img.shields.io/badge/GitHub%20Actions-Automated-2088FF?logo=github-actions&logoColor=white)
![GitHub Pages](https://img.shields.io/badge/Deployed%20on-GitHub%20Pages-222?logo=github&logoColor=white)

## ✨ Features

- 🕷️ **Web Scraping** - Extracts top 25 TV series data from IMDb
- 🎨 **Modern UI** - Beautiful, responsive design with soft color palette
- 🌙 **Dark/Light Mode** - Toggle between themes with persistent preference
- 📊 **CSV Export** - Download the data as a CSV file
- 🔄 **Auto Updates** - Weekly automated scraping via GitHub Actions
- 🚀 **GitHub Pages** - Automatic deployment to GitHub Pages

## 📸 Preview

The generated page displays:
- Ranking index for each series
- Title, release year, episodes count, and IMDb rating
- IMDb-style yellow rating badges
- Download CSV button

## 🛠️ Technologies Used

- **Python 3.11** - Core programming language
- **BeautifulSoup4** - HTML parsing and web scraping
- **Pandas** - Data manipulation and CSV generation
- **Jinja2** - HTML templating
- **Requests** - HTTP requests
- **GitHub Actions** - CI/CD automation
- **GitHub Pages** - Static site hosting

## 📁 Project Structure

```
IMDB_top_series_scrapper/
├── .github/
│   └── workflows/
│       └── deploy.yml      # GitHub Actions workflow
├── scrapper.py             # Main scraper script
├── requirements.txt        # Python dependencies
├── index.html              # Generated HTML output
├── top_25_webseries.csv    # Generated CSV data
└── README.md               # Project documentation
```

## 🚀 Getting Started

### Prerequisites

- Python 3.11 or higher
- pip (Python package manager)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/IMDB_top_series_scrapper.git
   cd IMDB_top_series_scrapper
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the scraper**
   ```bash
   python scrapper.py
   ```

4. **View the results**
   - Open `index.html` in your browser
   - Check `top_25_webseries.csv` for raw data

## ⚙️ GitHub Actions Automation

The project includes a GitHub Actions workflow that:

| Trigger | Description |
|---------|-------------|
| 🕐 **Scheduled** | Runs every Sunday at midnight UTC |
| 🖱️ **Manual** | Can be triggered from Actions tab |
| 📤 **On Push** | Runs when pushing to main branch |

### Setting Up GitHub Pages

1. Push the repository to GitHub
2. Go to **Settings** → **Pages**
3. Under **Source**, select **GitHub Actions**
4. The workflow will automatically deploy to GitHub Pages

### Manual Trigger

1. Go to the **Actions** tab in your repository
2. Select **Scrape and Deploy to GitHub Pages**
3. Click **Run workflow**

## 📦 Dependencies

```
pandas
jinja2
requests
beautifulsoup4
```

## 🔧 How It Works

1. **Fetch Data** - Sends a request to IMDb's top TV chart
2. **Parse HTML** - Extracts series information using BeautifulSoup
3. **Process Data** - Organizes data into a Pandas DataFrame
4. **Generate CSV** - Exports data to `top_25_webseries.csv`
5. **Render HTML** - Uses Jinja2 to create a styled HTML page
6. **Deploy** - GitHub Actions publishes to GitHub Pages

## 🤝 Contributing

Contributions are welcome! Feel free to:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## ⚠️ Disclaimer

This project is for educational purposes only. Please respect IMDb's terms of service and robots.txt when scraping their website.

---

<p align="center">
  Made with ❤️ using Python
</p>
