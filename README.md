# Salon Marketing Documentation

A documentation website for salon marketing research and strategies, built with Sphinx and Markdown.

## Features

- Automatic rebuilding when content changes
- Markdown support
- Clean, modern theme
- Easy to maintain and update
- Poetry for dependency management
- GitHub Pages hosting



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

## GitHub Pages Deployment

The documentation is automatically deployed to GitHub Pages when you push to the main branch. You can also manually deploy using:

```bash
make deploy
```

The documentation will be available at: https://jangidmonika.github.io/salon-marketing/

### Automatic Deployment

The project uses GitHub Actions to automatically deploy to GitHub Pages. The workflow:
1. Triggers on pushes to the main branch
2. Builds the documentation
3. Deploys to the gh-pages branch

## Project Structure

- `research/` - Contains all research documentation
- `conf.py` - Sphinx configuration
- `index.md` - Main documentation page
- `watch.py` - File watcher for automatic rebuilding
- `pyproject.toml` - Poetry configuration and dependencies
- `Makefile` - Common tasks automation
- `.github/workflows/` - GitHub Actions workflows

## Adding New Content

1. Create new markdown files in the appropriate category under `research/`
2. Add the file to the category's `index.md`
3. The documentation will automatically rebuild when changes are detected
4. Push changes to GitHub to trigger automatic deployment

## Development

The project uses:
- Poetry for dependency management
- Sphinx for documentation generation
- MyST for Markdown support
- Watchdog for automatic rebuilding
- GitHub Pages for hosting
- GitHub Actions for CI/CD

## License

This project is licensed under the MIT License - see the LICENSE file for details. 