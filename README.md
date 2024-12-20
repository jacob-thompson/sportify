# Sportify

Sportify is an application for the command line interface (CLI) that fetches and displays real-time sports data. Whether you're interested in scores, team stats, player information, or upcoming fixtures, Sportify provides a convenient way to access the latest sports updates from your terminal.

## 🚀 Features (Work-in-progress)

- Fetch live scores for various sports.
- Get detailed stats on teams and players.
- View schedules for upcoming matches and events.
- Filter data by league, team, or player.
- User-friendly CLI commands with customizable options.

## 📦 Installation

To install Sportify, ensure you have Python 3.7 or higher installed on your machine.

### Pip

[Recommended](https://peps.python.org/pep-0668/):

```bash
pipx install sportify
```

Otherwise:

```bash
pip install sportify
```

### From Source

> [!IMPORTANT]
> Requires `build`
> ```
> pip install build
> ```

1. Clone the repository:

    ```bash
    git clone https://github.com/jacob-thompson/sportify.git
    cd sportify
    ```

2. Build the application:

    ```bash
    python3 -m build
    ```

3. Install the application:

    `pipx`:
    ```bash
    pipx install dist/*.tar.gz --force
    ```

    `pip`:
    ```bash
    pip install dist/*.tar.gz --force
    ```

## 🛠️ Usage

```bash
sportify
```
