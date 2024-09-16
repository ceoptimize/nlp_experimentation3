#!/bin/bash

source /Users/christieentwistle/VsCodeProjects/nlp_experimentation3/venv/bin/activate

pip uninstall -y packageutilities
pip install /Users/christieentwistle/VsCodeProjects/temp_dir/packageutilities/packageutilities

pip install -e /Users/christieentwistle/VsCodeProjects/nlp_experimentation3

python -c "
import packageutilities.package_functions as pf
base_dir = '/Users/christieentwistle/VsCodeProjects'
package_dir = '/Users/christieentwistle/VsCodeProjects/nlp_experimentation3'
env_files = ['openai_env']
pf.copy_env_files(env_files, base_dir, package_dir)
"

echo "Dependencies and .env files updated successfully."
# To run in terminal:
# chmod +x /Users/christieentwistle/VsCodeProjects/nlp_experimentation3/refresh_dependencies.sh
# ./refresh_dependencies.sh
