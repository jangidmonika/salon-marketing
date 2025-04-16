.PHONY: install build clean watch serve help init

help:
	@echo "Available commands:"
	@echo "  make install    - Install dependencies using Poetry"
	@echo "  make init       - Initialize Sphinx project (first time only)"
	@echo "  make build      - Build the documentation"
	@echo "  make clean      - Clean build files"
	@echo "  make watch      - Watch for changes and rebuild automatically"
	@echo "  make serve      - Serve the documentation locally"
	@echo "  make help       - Show this help message"

install:
	poetry install

init:
	@echo "Initializing Sphinx project..."
	@if [ ! -f "conf.py" ]; then \
		poetry run sphinx-quickstart -q -p "Salon Marketing Documentation" -a "Monika Jangid" -v "0.1.0" .; \
		echo "Sphinx project initialized."; \
	else \
		echo "Sphinx project already initialized."; \
	fi

build:
	poetry run sphinx-build -b html . _build/html

clean:
	rm -rf _build/
	rm -rf _static/
	rm -rf _templates/

watch:
	poetry run python watch.py

serve:
	@echo "Serving documentation at http://localhost:8000"
	cd _build/html && python -m http.server 8000 