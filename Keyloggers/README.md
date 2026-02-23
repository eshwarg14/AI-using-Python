# 🛑 Python Keylogger (Educational Project)

## 👨‍💻 About This Project

This project was developed by me and my friend as part of our learning
in Python and basic cybersecurity concepts.

We built this keylogger to understand:

-   How keyboard listeners work in Python\
-   How keystrokes can be captured programmatically\
-   How file handling works\
-   How to send emails using SMTP\
-   The ethical risks associated with monitoring tools

This project is strictly for educational and demonstration purposes.

------------------------------------------------------------------------

## ⚙️ How This Program Works

The program uses the `pynput` library to listen to keyboard events.

### Step-by-step Working:

### 1️⃣ Keyboard Listener Starts

When the script runs, it activates a keyboard listener. It continuously
monitors key presses in the background.

### 2️⃣ Logging Keystrokes

-   Every key pressed is written into a file named `log.txt`.
-   Normal character keys are stored directly.
-   Special keys (like Shift, Enter, etc.) are stored in bracket format.

### 3️⃣ Stopping the Logger

When the `ESC` key is pressed: - The logger stops listening. - The
program triggers the email function.

### 4️⃣ Sending the Log via Email

-   The `smtplib` module connects to Gmail's SMTP server.
-   The `log.txt` file is attached to the email.
-   The email is sent to the configured recipient address.

After sending, the program exits.

------------------------------------------------------------------------

## 📧 Email Configuration

The script uses:

-   Gmail SMTP server (`smtp.gmail.com`)
-   Port 587 (TLS encryption)

To make this work:

1.  Enable 2-Step Verification in your Google account.
2.  Generate a Gmail App Password.
3.  Use the App Password instead of your regular Gmail password.
4.  Do NOT upload real passwords to public repositories.

Generate App Password here: https://myaccount.google.com/apppasswords

------------------------------------------------------------------------

## 🛠️ Technologies Used

-   Python 3
-   pynput
-   smtplib
-   email.mime
-   os

------------------------------------------------------------------------

## 📦 Installation

Install required library:

``` bash
pip install pynput
```

Make sure Python 3 is installed on your system.

------------------------------------------------------------------------

## 📂 Project Structure

    keylogger/
    │
    ├── keylogger.py
    ├── log.txt (generated automatically)
    └── README.md

------------------------------------------------------------------------

## ⚠️ Ethical & Legal Warning

This project is created only for learning purposes.

Keyloggers can be misused for illegal surveillance and privacy
violations.

Please follow these guidelines:

-   Use only on your own system.
-   Never install on someone else's device without explicit permission.
-   Unauthorized monitoring is illegal in many countries.
-   Misuse can lead to serious legal consequences.

We do not support or encourage unethical usage of this project.

------------------------------------------------------------------------

## 📚 What We Learned

By building this project, we understood:

-   How system-level input listeners work
-   How sensitive user data can be captured
-   Why cybersecurity awareness is important
-   The importance of ethical responsibility in programming

------------------------------------------------------------------------

## 👥 Authors

Developed by:

-   Eshwar G\
-   \[Your Friend's Name\]

BSc Statistics & Computer Science\
Python & Cybersecurity Learners

------------------------------------------------------------------------

## 🚨 Final Note

This repository is meant to demonstrate technical concepts and raise
awareness about security risks.

Please use responsibly and ethically.
# 🛑 Python Keylogger (Educational Project)

## 👨‍💻 About This Project

This project was developed by me and my friend as part of our learning
in Python and basic cybersecurity concepts.

We built this keylogger to understand:

-   How keyboard listeners work in Python\
-   How keystrokes can be captured programmatically\
-   How file handling works\
-   How to send emails using SMTP\
-   The ethical risks associated with monitoring tools

This project is strictly for educational and demonstration purposes.

------------------------------------------------------------------------

## ⚙️ How This Program Works

The program uses the `pynput` library to listen to keyboard events.

### Step-by-step Working:

### 1️⃣ Keyboard Listener Starts

When the script runs, it activates a keyboard listener. It continuously
monitors key presses in the background.

### 2️⃣ Logging Keystrokes

-   Every key pressed is written into a file named `log.txt`.
-   Normal character keys are stored directly.
-   Special keys (like Shift, Enter, etc.) are stored in bracket format.

### 3️⃣ Stopping the Logger

When the `ESC` key is pressed: - The logger stops listening. - The
program triggers the email function.

### 4️⃣ Sending the Log via Email

-   The `smtplib` module connects to Gmail's SMTP server.
-   The `log.txt` file is attached to the email.
-   The email is sent to the configured recipient address.

After sending, the program exits.

------------------------------------------------------------------------

## 📧 Email Configuration

The script uses:

-   Gmail SMTP server (`smtp.gmail.com`)
-   Port 587 (TLS encryption)

To make this work:

1.  Enable 2-Step Verification in your Google account.
2.  Generate a Gmail App Password.
3.  Use the App Password instead of your regular Gmail password.
4.  Do NOT upload real passwords to public repositories.

Generate App Password here: https://myaccount.google.com/apppasswords

------------------------------------------------------------------------

## 🛠️ Technologies Used

-   Python 3
-   pynput
-   smtplib
-   email.mime
-   os

------------------------------------------------------------------------

## 📦 Installation

Install required library:

``` bash
pip install pynput
```

Make sure Python 3 is installed on your system.

------------------------------------------------------------------------

## 📂 Project Structure

    keylogger/
    │
    ├── keylogger.py
    ├── log.txt (generated automatically)
    └── README.md

------------------------------------------------------------------------

## ⚠️ Ethical & Legal Warning

This project is created only for learning purposes.

Keyloggers can be misused for illegal surveillance and privacy
violations.

Please follow these guidelines:

-   Use only on your own system.
-   Never install on someone else's device without explicit permission.
-   Unauthorized monitoring is illegal in many countries.
-   Misuse can lead to serious legal consequences.

We do not support or encourage unethical usage of this project.

------------------------------------------------------------------------

## 📚 What We Learned

By building this project, we understood:

-   How system-level input listeners work
-   How sensitive user data can be captured
-   Why cybersecurity awareness is important
-   The importance of ethical responsibility in programming

------------------------------------------------------------------------

## 👥 Authors

Developed by:

-   Eshwar G\
-   \[Your Friend's Name\]

BSc Statistics & Computer Science\
Python & Cybersecurity Learners

------------------------------------------------------------------------

## 🚨 Final Note

This repository is meant to demonstrate technical concepts and raise
awareness about security risks.

Please use responsibly and ethically.

