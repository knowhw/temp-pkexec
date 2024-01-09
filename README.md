
## Installation
~~~bash
git clone https://github.com/knowhw/temp-pkexec.git
~~~


## Content
~~~
[PlankDockItemPreferences]
Launcher=file:///usr/share/applications/geany.desktop
~~~

## Module usage
~~~python
import temp
path='/home/elementary/.config/plank/dock1/launchers/geany.dockitem'

tempfile, filename = temp.filetouch(content)
tempfile.mv2(path)

# tempfile.pkexec.mv2(path)
# tempfile.delete(filename)

~~~
## Parametres
~~~
# filetouch => parametres (content)
# pkexec.mv2 => parametres (path, deleted='true', user='root')
# mv2 => parametres (path, deleted='true', user='home')
# delete => parametres (filename)
# _save_directory => default: /tmp/temporary.save
~~~




