import subprocess
import json

package = {"name": "my-awesome-package", "version": "1.0.0", "type": "module", "dependencies":{}}

{% if cookiecutter.typescript == "Y" %}
{{ cookiecutter.update({ "ext": "ts" }) }}
{% else %}
version = subprocess.run("npm view uuid version",shell=True,capture_output=True,text=True).stdout.replace("\n", "")
package["dependencies"]["uuid"] = version
{{ cookiecutter.update({ "ext": "js" }) }}
{% endif %}

packageObj = json.dumps(package,indent=4)

with open("package.json","w") as file:
    file.write(packageObj)
