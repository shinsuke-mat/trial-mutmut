# resolve dependencies
uv sync

# run test
uv run pytest

# check coverages
uv run pytest --cov=src

# basic mutmut execution
uv run mutmut run

# interactive mode
uv run mutmut browse
