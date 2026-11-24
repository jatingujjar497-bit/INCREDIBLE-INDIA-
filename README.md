# Incredible India – Smart Tourism Explorer

A beginner-friendly **Python terminal-based tourism project** that helps users explore Indian States and Union Territories through a simple menu-driven program.

## Project Overview

Incredible India stores basic tourism information for Indian States and Union Territories, including:

- Capital
- Popular tourist places
- Famous food
- Culture and traditions
- Best time to visit

The program runs in the terminal/command prompt. It does not require Streamlit, Folium, or any external Python libraries.

## Features

1. **Explore a State** – View the capital, tourist places, food, culture, and best time to visit.
2. **Show All States** – Display the available States and Union Territories.
3. **Search Tourist Place** – Search for a tourist attraction and find the state where it is listed. Partial place names are supported.
4. **Smart Trip Planner** – Create a simple day-wise sample plan using the tourist places stored for a selected state.
5. **Travel Budget Calculator** – Estimate hotel, food, and local travel expenses based on the number of days and costs entered by the user.
6. **Compare Two States** – Compare tourism information for two different states.
7. **Favourite Places** – Add a listed tourist place to a favourites list and view saved favourites during the current program session.
8. **Exit** – Close the program.

## Technologies Used

- **Programming Language:** Python 3
- **Interface:** Command-line / Terminal
- **Python modules:** No external modules required; the project uses Python's built-in features.

## Python Concepts Used

- Variables and data types
- Dictionaries and nested dictionaries
- Lists and tuples
- Functions and function parameters
- `while` and `for` loops
- `if`, `elif`, and `else` conditions
- User input with `input()`
- String methods such as `strip()` and `lower()`
- Dictionary methods such as `items()` and `values()`
- List methods such as `append()`
- `enumerate()` and `range()`
- Arithmetic operators
- Type conversion using `int()` and `float()`
- Exception handling using `try` and `except`
- `return` and `break`

## Requirements

- Python 3 installed on your computer
- A code editor or terminal (for example, Visual Studio Code)

No `pip install` command is needed because the program does not use external libraries.

## How to Run

1. Download or clone this repository.
2. Open the project folder in Visual Studio Code or a terminal.
3. Open the terminal in the folder containing `app.py`.
4. Run:

```bash
python app.py
```

If your computer uses the Python launcher, you can also try:

```bash
py app.py
```

## Sample Menu

```text
==============================================
              INCREDIBLE INDIA
           SMART TOURISM EXPLORER
==============================================

--------------- MAIN MENU ---------------
1. Explore a State
2. Show All States
3. Search Tourist Place
4. Smart Trip Planner
5. Travel Budget Calculator
6. Compare Two States
7. Favourite Places
8. Exit

Enter your choice (1-8):
```

## Notes and Limitations

- The information is stored in the Python program as sample project data.
- The trip planner creates a simple sample itinerary from the listed places. It does not calculate actual travel routes, distances, opening hours, or travel times.
- The budget calculator uses the costs entered by the user. It provides an estimate, not a live travel quotation.
- Favourite places are stored in memory only while the program is running. They are cleared when the program is closed.

## Future Improvements

- Save favourite places permanently in a file.
- Add more tourist destinations and detailed information.
- Add destination-wise estimated travel distances.
- Add a graphical user interface in a future version.

## Project Purpose

This project demonstrates how basic Python programming concepts can be combined to build a useful, menu-driven tourism information system.

---

**Project:** Incredible India – Smart Tourism Explorer  
**Version:** Terminal-based Python version
