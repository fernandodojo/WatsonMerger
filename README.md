<a name="readme-top"></a>


[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]

<br />
<div align="center">  
  <h1 align="center">Watson Merger</h1>
</div>

## Table of content
- [About The Project](#about-the-project)
  - [Built With](#built-with)
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [Dependencies](#dependencies)
- [License](#license)
- [Acknowledgments](#acknowledgments)


About The Project
====================

Merge of intents and entities from different [IBM Watson Assistant Dialog Skill](https://www.ibm.com/products/watson-assistant) json to csv file.

## Built With

The following tools were used in building the project:

[![Python][python-shield]][python-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>

Features
========
 - Entities merge integrates entities of the primary and secondary skill.
 - Entities diff keeps only the new entities of the primary skill.
 - Intents merge merge integrates intents of the primary and secondary skill.
 - Intents diff keeps only the new intents of the primary skill.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

Prerequisites
=============
[Python](https://www.python.org/)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

Installation
============

1. Clone the repo:
   ```sh
   git clone https://github.com/fernandodojo/WatsonMerger.git
   ```
2. Install Python packages running bellow command inside the project root folder:
   ```sh
   pip install -r requirements.txt
   ```
<p align="right">(<a href="#readme-top">back to top</a>)</p>

Usage
=====

1. Insert primary main skill into the folder "WatsonMerger/skills/primary/" located onto project root folder.**

2. Insert secondary skill into the folder "WatsonMerger/skills/secondary/" located onto project root folder.**
  
3. Outside the root folder run:
   ```sh
   python WatsonMerger
   ```
4. The folder "WatsonMerger/export/" contains csv files resulting from the merge or diff operations

5. The folder "WatsonMerger/logs/" contains logs in json files resulting from the merge or diff operations.
   
** Only the latest file inside wich of the above folders will be executed.
<p align="right">(<a href="#readme-top">back to top</a>)</p>

Contributing
===============

If you have a suggestion that would make this better, please fork the repo and create a pull request.

1. Fork the Project.
2. Create your Feature Branch (`git checkout -b feature/new_feature`).
3. Commit your Changes (`git commit -m 'Add some new_feature'`).
4. Push to the Branch (`git push origin feature/new_feature`).
5. Open a Pull Request.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

Dependencies
==========
- attrs
- jsonschema
- numpy
- pandas
- pyrsistent
- python-dateutil
- pytz
- six
- tzdata

License
=======

Distributed under the MIT License. See [LICENSE](https://github.com/fernandodojo/WatsonMerger/blob/main/LICENSE) for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>


Acknowledgments
==================
* [jsonschema](https://python-jsonschema.readthedocs.io/en/stable/)
* [pandas](https://pandas.pydata.org/)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- MARKDOWN LINKS & IMAGES -->
[python-shield]: https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white
[python-url]: https://www.python.org/
[license-shield]: https://img.shields.io/github/license/fernandodojo/WatsonMerger.svg?style=for-the-badge
[license-url]: https://github.com/fernandodojo/WatsonMerger/blob/main/LICENSE
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/fernando-henrique-fernandes-leite