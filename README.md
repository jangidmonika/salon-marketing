# Salon Marketing Documentation

A documentation website for salon marketing research and strategies, built with Sphinx and Markdown.

## Features

- Automatic rebuilding when content changes
- Markdown support
- Clean, modern theme
- Easy to maintain and update
- Poetry for dependency management

## Setup

1. Install Poetry if you haven't already:
   ```bash
   curl -sSL https://install.python-poetry.org | python3 -
   ```

2. Install dependencies:
   ```bash
   make install
   ```

3. Initialize the Sphinx project (first time only):
   ```bash
   make init
   ```

4. Build the documentation:
   ```bash
   make build
   ```

## Usage

- To watch for changes and automatically rebuild:
  ```bash
  make watch
  ```

- To serve the documentation locally:
  ```bash
  make serve
  ```

- To clean build files:
  ```bash
  make clean
  ```

## Project Structure

- `research/` - Contains all research documentation
- `conf.py` - Sphinx configuration
- `index.md` - Main documentation page
- `watch.py` - File watcher for automatic rebuilding
- `pyproject.toml` - Poetry configuration and dependencies
- `Makefile` - Common tasks automation

## Adding New Content

1. Create new markdown files in the appropriate category under `research/`
2. Add the file to the category's `index.md`
3. The documentation will automatically rebuild when changes are detected

## Development

The project uses:
- Poetry for dependency management
- Sphinx for documentation generation
- MyST for Markdown support
- Watchdog for automatic rebuilding

## License

This project is licensed under the MIT License - see the LICENSE file for details. 