# Automated Cricket Score Notifier

Automated Cricket Score Notifier is a Python script that scrapes live cricket scores from ESPN Cricinfo and sends notifications about boundaries (fours and sixes) and wickets to a specified Telegram bot.

## Features

- Scrapes live cricket scores from ESPN Cricinfo.
- Sends notifications to a Telegram bot for:
  - Fours
  - Sixes
  - Wickets

## Prerequisites

- Python 3.x
- `requests`
- `beautifulsoup4`

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/automated-cricket-score-notifier.git
    cd automated-cricket-score-notifier
    ```

2. Install the required packages:
    ```bash
    pip install requests beautifulsoup4
    ```

## Configuration

1. Set up a Telegram bot and get the bot token and chat ID.
2. Replace the `bot_token` and `chat_id` variables in the script with your own values.

## Usage

1. Run the script:
    ```bash
    score_notifier.py
    ```

2. The script will scrape the live cricket score from the specified ESPN Cricinfo URL and send notifications to the Telegram bot whenever a boundary (four or six) is hit or a wicket falls.

Example:
```bash
A six has been hit!
A four has been hit!
A wicket has fallen!
