# Pusername-gen: A Powerful Python Username Generator

![Python Version](https://img.shields.io/badge/python-3.6%2B-blue.svg)
[![GitHub stars](https://img.shields.io/github/stars/sayamcoder/Pusername-gen?style=social)](https://github.com/sayamcoder/Pusername-gen/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/sayamcoder/Pusername-gen?style=social)](https://github.com/sayamcoder/Pusername-gen/network/members)

A versatile and customizable command-line tool for generating creative and powerful usernames. Built with a clean, modular structure, this generator allows for easy expansion and personalization without touching the core logic.

## ✨ Features

- **Multiple Generation Styles**: Create usernames based on different patterns, like `AdjectiveNoun` or a more complex `GamerTag`.
- **Powerful Transformations**: Apply optional modifications like:
  - Appending random numbers.
  - Using underscores (`_`) as separators.
  - Converting to basic 1337 (leet) speak (e.g., `e` -> `3`, `s` -> `5`).
- **Easily Extensible**: Add your own adjectives, nouns, prefixes, and suffixes by simply editing the `.txt` files in the `data/` directory.
- **Interactive CLI**: A user-friendly command-line interface guides you through the generation process.
- **Modular Codebase**: The project is split into separate files for the main interface, core generator logic, and utility functions, making it easy to understand and maintain.

## 🚀 Demo

Here's a quick look at the generator in action:
==============================
Powerful Username Generator
Generate 'Adjective + Noun' usernames (e.g., SilentPhoenix)
Generate 'Gamer' usernames (e.g., xX_Gamer_Xx)
Exit
Choose a style (1-3): 1
How many usernames would you like to generate? 5
Add random numbers to the end? (y/n): y
Use underscore '_' as a separator? (y/n): y
Convert to 1337 (leet) speak? (y/n): n
--- Generated Usernames ---
Brave_Phoenix123
Golden_Jaguar852
Swift_Warden475
Electric_Wolf901
Mystic_Knight228
Press Enter to continue...
code
Code
## 📂 Project Structure

The project is organized for clarity and scalability:
Pusername-gen/
├── main.py # Main application entry point (CLI)
├── generator.py # Core class for generating usernames
├── utils.py # Helper functions (e.g., file loading, leet speak)
├── README.md # You are here!
└── data/
├── adjectives.txt
├── nouns.txt
├── prefixes.txt
└── suffixes.txt
code
Code
## 🛠️ Installation & Setup

Get your local copy up and running in a few simple steps.

1.  **Clone the repository:**
    ```sh
    git clone https://github.com/sayamcoder/Pusername-gen.git
    ```

2.  **Navigate to the project directory:**
    ```sh
    cd Pusername-gen
    ```

3.  This project uses only Python's standard libraries, so **no external packages are needed!**

## 🏃‍♂️ How to Run

1.  (Optional) Customize the word lists by editing the `.txt` files in the `data/` directory.
2.  Run the main script from your terminal:
    ```sh
    python main.py
    ```
3.  Follow the on-screen prompts to select your desired username style and transformations.

## 🎨 How to Customize

The true power of this generator lies in its customizability. To add your own words:

1.  Navigate to the `data/` directory.
2.  Open the file you want to edit (e.g., `nouns.txt`).
3.  Add your new words, with **one word per line**.
4.  Save the file.
5.  Run the program again. Your new words will now be included in the generation pool!

## 🤝 Contributing

Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".

1.  Fork the Project
2.  Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3.  Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4.  Push to the Branch (`git push origin feature/AmazingFeature`)
5.  Open a Pull Request

## 📬 Contact

Sayam - [@sayamcoder](https://github.com/sayamcoder)

Project Link: [https://github.com/sayamcoder/Pusername-gen](https://github.com/sayamcoder/Pusername-gen)
