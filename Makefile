.PHONY: validate sync package clean

validate:
	python scripts/validate_repo.py

sync:
	python scripts/sync_plugin.py

package: validate
	mkdir -p dist
	zip -r dist/exam-construction-agent-skill.zip . -x "*.git*" "dist/*" "*/__pycache__/*" "*.pyc"

clean:
	rm -rf dist __pycache__ .pytest_cache
