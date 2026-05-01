# FromageFinder

A full-stack cheese discovery platform that helps users explore and find their perfect cheese based on flavor, texture, and preferences — powered by real-world data.  
Built an interactive recommendation system over 1,100+ cheeses across 50+ countries with dynamic filtering and analytics.

---

## Features

- Cheese Finder
  - Multi-filter search across 1,187 cheeses
  - Filter by:
    - Flavor (creamy, nutty, tangy, etc.)
    - Texture (soft, crumbly, gooey, etc.)
    - Milk type (cow, goat, sheep, buffalo, etc.)
  - Instant results with real-time filtering

- Personality Quiz
  - 5-question interactive quiz
  - Maps user preferences to a “cheese personality”
  - Suggests cheeses based on taste profile

- Dashboard
  - Visual insights:
    - Top cheese-producing countries
    - Flavor distribution
    - Milk type breakdown

- User System
  - Login / signup functionality
  - Session-based authentication

---

## How It Works

- Dataset is converted from CSV → JSON for faster access  
- Filters dynamically match user-selected attributes  
- Quiz responses map to predefined flavor profiles  
- Results update instantly without page reload  

---

## Tech Stack

- Backend: Python, Flask  
- Frontend: HTML, CSS, JavaScript  
- Data Processing: CSV → JSON  
- Visualization: Chart.js  
- Authentication: Flask sessions  

---

## Project Structure

fromagefinder/
- app.py
- convert.py
- cheeses.csv
- users.json
- static/
  - cheeses.json
- templates/
  - explore.html
  - auth.html

---

## Getting Started

pip install flask  
python app.py  

Then open: http://localhost:5000

---

## Dataset

- Source: Kaggle (Cheese Across the World dataset)  
- Includes flavor, texture, milk type, and country data  

---

## License

MIT

---

## Author

Dhyeya Aneesh
