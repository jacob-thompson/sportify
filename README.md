# Sportify

Sportify is a Python-based command-line interface (CLI) application that fetches and displays real-time sports data. Whether you're interested in scores, team stats, player information, or upcoming fixtures, Sportify provides a convenient way to access the latest sports updates from your terminal.

## Features (Work-in-progress)

- Fetch live scores for various sports.
- Get detailed stats on teams and players.
- View schedules for upcoming matches and events.
- Filter data by league, team, or player.
- User-friendly CLI commands with customizable options.

## Installation

To install Sportify, ensure you have Python 3.7 or higher installed on your machine.

### Pip

Recommended:
```bash
pipx install sportify
```

Otherwise:
```bash
pip install sportify
```

### Source

> [!IMPORTANT]
> Requires `build`

1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/sportify.git
    cd sportify
    ```

2. Build the application:
    ```bash
    python3 -m build
    ```

3. Install the application:
    Recommended:
    ```bash
    pipx install dist/*.tar.gz
    ```
    Otherwise:
    ```bash
    pip install dist/*.tar.gz
    ```

4. Run the application:
    ```bash
    sportify
    ```

## Usage

```bash
sportify
```
