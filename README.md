# 💸 Expense Tracker

A simple personal expense tracker built with Python and Streamlit. Log what you spend, filter by month, and see where your money goes.

**Live app:** https://expense-tracker-sq9cbaenjkyjwswrcvvjk9.streamlit.app

## Features

- Add an expense with amount (₹), category, date and an optional note
- Filter expenses by month or view all time
- See the total spent and your top spending category
- Bar chart of spending by category
- View all expenses in a table and delete any of them
- Data is saved to a local `expenses.csv` file

## Tech stack

- [Python](https://www.python.org/) 3.10+
- [Streamlit](https://streamlit.io/) for the web interface
- [pandas](https://pandas.pydata.org/) for handling the data

## Run it on your computer

1. Clone the repository:
   ```bash
   git clone https://github.com/Ananya040906/expense-tracker.git
   cd expense-tracker
   ```
2. Create and activate a virtual environment:
   ```bash
   python -m venv .venv
   ```
   - Windows (PowerShell): `.venv\Scripts\activate`
   - Mac/Linux: `source .venv/bin/activate`
3. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Start the app:
   ```bash
   streamlit run app.py
   ```
   It opens in your browser at `http://localhost:8501`.

## Project structure

```
expense-tracker/
├── app.py             # The Streamlit app
├── requirements.txt   # Python dependencies
├── .gitignore         # Files Git should ignore
└── README.md          # This file
```

`expenses.csv` is created automatically the first time you add an expense. It is listed in `.gitignore`, so your personal data is not uploaded to GitHub.

## Deploy on Streamlit Community Cloud

1. Push this repository to GitHub.
2. Go to [share.streamlit.io](https://share.streamlit.io) and sign in with GitHub.
3. Click **Create app** and choose this repository, the `main` branch, and `app.py` as the main file.
4. Click **Deploy**.

## Known limitations

- On Streamlit Community Cloud, saved files can be lost when the app restarts, so data may reset.
- Anyone with the app link can view it and add expenses unless you restrict access in the app's sharing settings.

## Roadmap

- [ ] Permanent storage (Google Sheets or Supabase)
- [ ] Monthly budgets with warnings
- [ ] CSV download for backups
- [ ] Password protection

## License

This project is for personal use and learning. Add a license of your choice if you plan to share it.
