import streamlit as st
import pandas as pd
from datetime import date
from pathlib import Path

DATA_FILE = Path(__file__).parent / "expenses.csv"
COLUMNS = ["id", "date", "category", "amount", "note"]
CATEGORIES = ["Food", "Transport", "Rent", "Bills", "Shopping", "Health", "Fun", "Other"]


def load_data():
    if DATA_FILE.exists():
        df = pd.read_csv(DATA_FILE)
        df["date"] = pd.to_datetime(df["date"])
        df["note"] = df["note"].fillna("")
        return df
    return pd.DataFrame({
        "id": pd.Series(dtype="int"),
        "date": pd.Series(dtype="datetime64[ns]"),
        "category": pd.Series(dtype="str"),
        "amount": pd.Series(dtype="float"),
        "note": pd.Series(dtype="str"),
    })


def save_data(df):
    df[COLUMNS].to_csv(DATA_FILE, index=False)

st.set_page_config(page_title="Expense Tracker", page_icon="💸")
st.title("Expense Tracker")

df = load_data()

with st.form("add_expense", clear_on_submit=True):
    c1, c2 = st.columns(2)
    amount = c1.number_input("Amount (₹)", min_value=0.0, step=10.0)
    category = c2.selectbox("Category", CATEGORIES)
    d = c1.date_input("Date", value=date.today())
    note = c2.text_input("Note (optional)")
    submitted = st.form_submit_button("Add expense")

if submitted:
    if amount <= 0:
        st.error("Enter an amount greater than zero.")
    else:
        new_id = int(df["id"].max()) + 1 if not df.empty else 1
        new_row = pd.DataFrame([{
            "id": new_id,
            "date": pd.Timestamp(d),
            "category": category,
            "amount": amount,
            "note": note.strip(),
        }])
        df = pd.concat([df, new_row], ignore_index=True)
        save_data(df)
        st.success("Expense added.")

st.divider()

if df.empty:
    st.info("No expenses yet. Add your first one above.")
    st.stop()

df["month"] = df["date"].dt.strftime("%Y-%m")
months = ["All time"] + sorted(df["month"].unique(), reverse=True)
choice = st.selectbox("Month", months)
view = df if choice == "All time" else df[df["month"] == choice]

total = view["amount"].sum()
by_cat = view.groupby("category")["amount"].sum().sort_values(ascending=False)

m1, m2 = st.columns(2)
m1.metric("Total spent", f"₹{total:,.2f}")
m2.metric("Top category", by_cat.index[0], f"₹{by_cat.iloc[0]:,.2f}", delta_color="off")

st.subheader("Spending by category")
st.bar_chart(by_cat)

st.subheader("Expenses")
view = view.sort_values("date", ascending=False)
st.dataframe(view[COLUMNS], hide_index=True)

to_delete = st.selectbox(
    "Select an expense to delete",
    view["id"],
    format_func=lambda i: (
        f"#{i}: {view.loc[view['id'] == i, 'category'].iloc[0]} "
        f"₹{view.loc[view['id'] == i, 'amount'].iloc[0]:,.2f}"
    ),
)
if st.button("Delete selected expense"):
    df = df[df["id"] != to_delete]
    save_data(df)
    st.rerun()

