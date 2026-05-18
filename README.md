# Flash Card Learning App

An interactive desktop flash card application designed to help users learn French language vocabulary efficiently. 

## Key Features
* **Dynamic Card Flipping:** Automatically flips the card from French to English after a 3-second delay to test the user's memory.
* **Smart Progress Tracking:** Keeps track of words the user already knows. Known words are removed from the deck so they don't repeat.
* **Data Persistence:** Saves the user's progress automatically into a new file so they can pick up right where they left off next time.

## 🛠️ How It Works (Technical Concepts)
* **Data Management with Pandas:** Uses the `pandas` library to read the original French vocabulary CSV file and convert it into a workable Python dictionary.
* **File Operations:** Uses `pandas.to_csv()` to dynamically create and update a `words_to_learn.csv` file based on user performance.
* **Graphical User Interface (GUI):** Built using Python's built-in `tkinter` library, utilizing canvas widgets to overlay text smoothly onto images.
* **Event-Driven Timers:** Uses the `.after()` method in Tkinter to handle the asynchronous 3-second delay before revealing the answer.

## 📦 Tech Stack
* **Language:** Python 3
* **Libraries:** Tkinter, Pandas, Random
